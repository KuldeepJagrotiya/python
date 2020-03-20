## Q3 validate input from user to check input string is alphanumeric or not

inp = input("Enter any string : ")
if inp.isdigit()==False and inp.isalpha()==False:
    print("string is alphanumeric ")
else:
    print("string is not alphanumeric ")