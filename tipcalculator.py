Base_Value = input("Please enter your total bill amount: ")
Tip_value = input("Please enter your tip value in percentage: ")

if Base_Value.isdigit() and Tip_value.isdigit() :
    Base_Value = int(Base_Value) 
    Tip_value = (int(Tip_value)/100)
    Tip_value = (Base_Value*Tip_value)
    Sum_of_Tip = (Base_Value+Tip_value)
    print(f"The Total amount to be paid is: {Sum_of_Tip}")
else:
    print(f"The {Base_Value} and {Tip_value} enterd are invalid")    
    

    