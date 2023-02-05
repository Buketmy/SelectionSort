int_list:list = [5,1,3,2,7,4]
for i in range(len(int_list)):
    next_element:int = min(int_list[i:])
    min_next_element_index:int = int_list[i:].index(next_element)
    int_list[i + min_next_element_index]:int = int_list[i]
    int_list[i] = next_element
print(int_list)
    







     
        


