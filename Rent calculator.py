# input we need from the user
# total rent
# total food ordered for snacking'
# electricity units spend
# chagr per unit


# ouput
# total amount you wiil to pay is 

rent =int(input("enter your  flat/hostel rent = "))
food =int(input("enter the amount of food ordered = "))
electicity_spend = int(input("enter the total of electricity spend ="))
charge_per_unit =int(input("enter the charge per unit ="))
persons = int(input("enter the number of person living in room/flat ="))

total_bill = electicity_spend * charge_per_unit
output =(food + rent + total_bill) // persons
print("each person will pay = ",output)