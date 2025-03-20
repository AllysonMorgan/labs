import ast

def parse_file(filename):
    with open(filename,"r") as file:
        return ast.parse(file.read())

def count_lines(tree):
    line_count=0
    for node in ast.walk(tree):
        if hasattr(node,"lineno"):
            line_count=max(line_count,node.lineno)
    return line_count

def list_imports(tree):
    package_list=[]
    for node in tree.body:
        if isinstance(node,(ast.Import,ast.ImportFrom)):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    package_list.append(alias.name)
            elif isinstance(node,ast.ImportFrom):
                package_list.append(node.module)
    if package_list:
        return package_list
    else:
        return "None"

class FunctionLister(ast.NodeVisitor):
    def __init__(self):
        self.function_list=[]
        self.current_class=None
    def visit_ClassDef(self,node):
        previous_class=self.current_class
        self.current_class=node.name
        self.generic_visit(node)
        self.current_class=previous_class
    def visit_FunctionDef(self,node):
        if self.current_class:
            function_name=f"{self.current_class}_{node.name}"
        else:
            function_name=node.name
        self.function_list.append(function_name)

def list_functions(tree):
    lister=FunctionLister()
    lister.visit(tree)
    return lister.function_list

class ClassLister(ast.NodeVisitor):
    def __init__(self):
        self.class_list=[]
    def visit_ClassDef(self,node):
        self.class_list.append(node.name)

def list_classes(tree):
    lister=ClassLister()
    lister.visit(tree)
    return lister.class_list

def list_docstrings(tree):
    docstring_list=[]
    for node in ast.walk(tree):
        if isinstance(node,(ast.FunctionDef,ast.ClassDef)):
            docstring=ast.get_docstring(node)
            if docstring:
                docstring_list.append(docstring)
            else:
                docstring_list.append(f"{node.name}: docstring not found")
    return docstring_list

class TypeAnnotationChecker(ast.NodeVisitor):
    def __init__(self):
        self.type_annotated_functions=[]
        self.non_type_annotated_functions=[]

    def visit_FunctionDef(self,node):
        has_annotation=False
        if node.returns:
            has_annotation=True
        for arg in node.args.args:
            if arg.annotation:
                has_annotation = True
                break
        if has_annotation:
            self.type_annotated_functions.append(node.name)
        else:
            self.non_type_annotated_functions.append(node.name)
        self.generic_visit(node)

def check_type_annotations(tree):
    checker=TypeAnnotationChecker()
    checker.visit(tree)
    return checker.type_annotated_functions, checker.non_type_annotated_functions

class NamingConventionChecker(ast.NodeVisitor):
    def __init__(self):
        self.classes = []
        self.functions = []

    def visit_ClassDef(self, node):
        if not self.is_camel_case(node.name):
            self.classes.append(node.name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if not self.is_valid_function_name(node.name):
            self.functions.append(node.name)
        self.generic_visit(node)

    def is_camel_case(self, name):
        return name[0].isupper() and all(part.isalpha() and part[0].isupper() for part in name.split('_'))

    def is_valid_function_name(self, name):
        return name.islower() or (name.islower() and '_' in name)

    def report(self):
        if not self.classes and not self.functions:
            return "All names adhere to the specified naming convention."
        else:
            report = []
            if self.classes:
                report.append("Classes that are not adhering to CamelCase: " + ", ".join(self.classes))
            if self.functions:
                report.append("Functions that are not adhering to lower_case: " + ", ".join(self.functions))
            return "\n".join(report)

def check_naming_conventions(tree):
    checker = NamingConventionChecker()
    checker.visit(tree)
    return checker.report()

def analyze_file(filename):
    tree=parse_file(filename)
    output_filename=f"style_report_{filename}.txt"
    output_file=open(output_filename,'w')
    type_annotated_functions,non_type_annotated_functions=check_type_annotations(tree)
    if not non_type_annotated_functions:
        type_annotated_functions= "All functions use type annotation."
    else:
        type_annotated_functions=non_type_annotated_functions
    full_report={
        "Line Count":count_lines(tree),
        "Imported Packages":list_imports(tree),
        "Classes":list_classes(tree),
        "Functions":list_functions(tree),
        "Docstrings":"\n\n".join(list_docstrings(tree)),
        "Non-Type Annotated Functions":type_annotated_functions,
        "Naming Convention Check":check_naming_conventions(tree)}
    report_string = "File Structure:\n"
    for key, value in full_report.items():
        report_string += f"{key}:\n"
        if isinstance(value, list):
            report_string += "\n".join(f"  - {item}" for item in value) + "\n"
        else:
            report_string += f"{value}\n"
        report_string += "\n\n"
    output_file.write(report_string)
    output_file.close()
    
def main():
    py_file=input("Enter the name of the file you want to check. Be sure to include the .py: ")
    analyze_file(py_file)
    print("Report has been generated!")

main()