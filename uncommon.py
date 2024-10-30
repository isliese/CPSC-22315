s1 = input("Enter the first sentence : ")
s2 = input("Enter the second sentence : ")

word_list = s1.split() + s2.split()

def remove_duplicates(lst):
    seen = set()  # save elements that already appear
    duplicates = set()  # save duplicated elements

    # check list sequentially 
    for x in lst:
        if x in seen:
            duplicates.add(x)  # if duplicated elements are detected, add to duplicates
        else:
            seen.add(x)  # if element first appears, add to seen
    
    # only non-duplicated elements 
    return [x for x in lst if x not in duplicates]

result = remove_duplicates(word_list)

print(result)  
