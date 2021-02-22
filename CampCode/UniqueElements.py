# Unique elements with Dictionary

'''
There are four collection data types in the Python programming language:
1. List is a collection which is ordered and changeable. Allows duplicate members: e.g. l = [1,2,3], l = [] for empty list
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members: e.g. t = (1,2,3), t = () for empty tuple
3. Set is a collection which is unordered and unindexed. No duplicate members: e.g. s = {1,2,3}, s = set() for empty set
4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members: e.g. d = {"One": 1, "Two": 2, "Three": 3}, d = {} for empty dictionary

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
'''

def UniqueDictionary(myList = [], *args):
    dic = {}
    for x in myList:
        if dic.__contains__(x):
            dic[x] += 1     # dic[x]++ is not working because ++ in python is not an operator
        else:
            dic[x] = 1

    result = ""
    for key in dic.keys():
        if dic[key] == 1: result += str(key) + ", "

    return result[:len(result) - 2]     # Characters from the beginning to position len(result) - 2 (excluded)

l = [7, 7, 3, 8, 1, 9, 10, 9, 9, 10, 10, 9]

print("# Unique elements with Dictionary (No Hashtable in Python)")
result = UniqueDictionary(l)
print("Dictionary: {0} => {1}".format(", ".join(map(str, l)), result))  # Equivalent to print("Dictionary: " + ", ".join(map(str, l)) + " => " + result)
print()


