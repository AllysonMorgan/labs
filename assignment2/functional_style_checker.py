import ast
from typing import List, Tuple, Union


def parse_file(filename: str) -> ast.AST:
    with open(filename, "r") as file:
        return ast.parse(file.read())


def count_lines(tree: ast.AST) -> int:
    return max((getattr(node, "lineno", 0) for node in ast.walk(tree)), default=0)


def list_imports(tree: ast.AST) -> List[str]:
    return [alias.name if isinstance(node, ast.Import) else node.module
            for node in tree.body
            if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in getattr(node, 'names', []) or [None]] or ["None"]


def list_functions(tree: ast.AST) -> List[str]:
    def collect_functions(nodes, current_class=None):
        return [
            f"{current_class}_{node.name}" if current_class else node.name
            for node in nodes if isinstance(node, ast.FunctionDef)
        ] + sum([
            collect_functions(node.body, node.name)
            for node in nodes if isinstance(node, ast.ClassDef)
        ], [])

    return collect_functions(tree.body)


def list_classes(tree: ast.AST) -> List[str]:
    return [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]


def list_docstrings(tree: ast.AST) -> List[str]:
    return [
        ast.get_docstring(node) or f"{node.name}: docstring not found"
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.ClassDef))
    ]


def check_type_annotations(tree: ast.AST) -> Tuple[List[str], List[str]]:
    annotated, not_annotated = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            has_annotation = bool(node.returns) or any(arg.annotation for arg in node.args.args)
            (annotated if has_annotation else not_annotated).append(node.name)
    return annotated, not_annotated


def check_naming_conventions(tree: ast.AST) -> str:
    def is_camel_case(name: str) -> bool:
        return name[0].isupper() and all(part.istitle() for part in name.split('_'))

    def is_valid_function_name(name: str) -> bool:
        return name.islower() and ('_' in name or name.isidentifier())

    classes = [node.name for node in ast.walk(tree)
               if isinstance(node, ast.ClassDef) and not is_camel_case(node.name)]
    functions = [node.name for node in ast.walk(tree)
                 if isinstance(node, ast.FunctionDef) and not is_valid_function_name(node.name)]

    report = []
    if classes:
        report.append("Classes that are not adhering to CamelCase: " + ", ".join(classes))
    if functions:
        report.append("Functions that are not adhering to lower_case: " + ", ".join(functions))

    return "\n".join(report) if report else "All names adhere to the specified naming convention."


def generate_report(tree: ast.AST) -> str:
    annotated, not_annotated = check_type_annotations(tree)

    full_report = {
        "Line Count": count_lines(tree),
        "Imported Packages": list_imports(tree),
        "Classes": list_classes(tree),
        "Functions": list_functions(tree),
        "Docstrings": list_docstrings(tree),
        "Non-Type Annotated Functions": not_annotated or ["All functions use type annotation."],
        "Naming Convention Check": check_naming_conventions(tree)
    }

    report = "File Structure:\n"
    for key, value in full_report.items():
        report += f"{key}:\n"
        report += ("\n".join(f"  - {item}" for item in value) if isinstance(value, list) else f"{value}") + "\n\n"
    return report


def write_report(filename: str, report: str) -> None:
    output_filename = f"style_report_{filename}.txt"
    with open(output_filename, 'w') as output_file:
        output_file.write(report)


def main(filename: str) -> None:
    tree = parse_file(filename)
    report = generate_report(tree)
    write_report(filename, report)
    print("Report has been generated!")


if __name__ == "__main__":
    pyfile=input("Enter the Python file you'd like to generate a report for: ")
    main(pyfile)