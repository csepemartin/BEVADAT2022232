#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

def contains_odd(input_list):
    i = 0
    while(i < len(input_list)):
        if(input_list[i]%2 == 1):
            return True
        else:
            i = i + 1
    return False

#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list
def is_odd(input_list):
    bool_list = []
    for number in input_list:
        if(number%2==1):
            bool_list.append(True)
        else:
            bool_list.append(False)
    for bools in bool_list:
    return bool_list
     
#Create a function that accpects 2 lists of integers and returns their element wise sum. 
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

def element_wise_sum(input_list_1,input_list_2):
    i = 0
    j = 0
    output_list=[]
    while(i < len(input_list_1) and j < len(input_list_2)):
          output_list.append(input_list_1[i] + input_list_2[j])
          i = i +1
          j = j +1
    while(i < len(input_list_1)):
          output_list.append(input_list_1[i])
          i = i +1
    while(j < len(input_list_2)):
          output_list.append(input_list_2[j])
          j = j +1
    return output_list

#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict
def dict_to_list(input_dict):
    output_list=[]
    for key,value in input_dict.items():
        output_list.append((key,value))
    return output_list          

#If all the functions are created convert this notebook into a .py file and push to your repo
