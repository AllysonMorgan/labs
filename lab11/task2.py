def group_by(f, target_list):
    result={}
    for item in target_list:
        key=f(item)
        if key not in result:
            result[key]=[]
        result[key].append(item)
    return result

def main():
    print(group_by(len, ["hi","dog","me","bad","good"])) 
    print(group_by(len, ["chicken","frogs","cookie","puppy","laptop","chicken nuggets","ketchup"]))
    group_by_type = group_by(type, [1, "word", 3.27, [1,2], "other word", 27, 352525, 6.14153, (1,2,3), ["this","is","a","list"], (5,6,1)])
    print(group_by_type)

if __name__ == "__main__":
    main()