list_of_number =  [i for i in range(1, 11)]
print("Orginal list: ",list_of_number) 
first_five = list_of_number[0:5]
print("Extracted first five elements: ", first_five)
reverse = first_five[::-1]
print("Reversed extracted elements: ", reverse)