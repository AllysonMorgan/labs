def make_set(data):
    integers_list=data.split()
    set_list=[]
    for integer in integers_list:
        if integer not in set_list:
            set_list.append(integer)
    return set_list

def is_set(data):
    integers_list=data.split()
    set_list=[]
    for integer in integers_list:
        if integer not in set_list:
            set_list.append(integer)
    if len(set_list) == len(integers_list):
        return True
    else:
        return False

def union(setA,setB):
    setA_list=setA.split()
    setB_list=setB.split()
    setA_set=[]
    setB_set=[]
    for integer in setA_list:
        if integer not in setA_set:
            setA_set.append(integer)
    for integer in setB_list:
        if integer not in setB_set:
            setB_set.append(integer)
    if len(setA_list)!=len(setA_set) or len(setB_list)!=len(setB_set):
        union=[]
    else:
        for integer in setA_set:
            if integer not in setB_set:
                setB_set.append(integer)
        union=setB_set
    return union

def intersection(setA,setB):
    setA_list=setA.split()
    setB_list=setB.split()
    setA_set=[]
    setB_set=[]
    for integer in setA_list:
        if integer not in setA_set:
            setA_set.append(integer)
    for integer in setB_list:
        if integer not in setB_set:
            setB_set.append(integer)
    if len(setA_list)!=len(setA_set) or len(setB_list)!=len(setB_set):
        intersection=[]
    else:
        intersection=[]
        for integer in setA_set:
            if integer in setB_set:
                intersection.append(integer)
    return intersection

def main():
    integers=input("Enter a list of integers separated by spaces: ")
    print("Is a set:", is_set(integers))
    print("The set is:", make_set(integers))
    print("Now enter two lists. If either is not a set, a union or intersection cannot be made and an empty list will be returned.")
    input_A=input("Enter the first list of integers separated by spaces: ")
    input_B=input("Enter the second list of integers separated by spaces: ")
    print("Union:", union(input_A,input_B))
    print("Intersection:", intersection(input_A,input_B))
main()
