def zipmap(key_list, value_list, override=False):
    if not override:
        if len(key_list) != len(set(key_list)):
            return {}

    result = {}
    for i, key in enumerate(key_list):
        if i<len(value_list):
            value=value_list[i]
        else:
            value=None
        if override or key not in result:
            result[key]=value
    return result

def main():
    print(zipmap(['a','b','c','d','e','f'], [1,2,3,4,5,6]))
    print(zipmap([1,2,3,2], [4,5,6,7], True))
    print(zipmap([1,2,3], [4,5,6,7,8])) 
    print(zipmap([1,3,5,7], [2,4,6]))

if __name__=="__main__":
    main()