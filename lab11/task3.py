from functools import reduce

def filter_using_reduce(predicate, iterable):
    return reduce(lambda acc, x: acc + [x] if predicate(x) else acc, iterable, [])

def main():
    print(filter_using_reduce(lambda x:x>2, [1,2,3,4,5])) 
    is_even=lambda x:x%2==0
    print(filter_using_reduce(is_even, [1,2,3,4,5,6]))
    is_odd=lambda x:x%2!=0
    print(filter_using_reduce(is_odd, [1,2,3,4,5,6,7,8,9]))

if __name__=="__main__":
    main()

#I really hope I did this one right, the task description was kind of vague and I wasn't totally sure which example from class I'm supposed to base it off of