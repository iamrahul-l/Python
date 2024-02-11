hourly_salary= input("Please enter your hourly salary: ")
hours_per_week = input("How many hours do you work per week: ") 
if hourly_salary.isdigit() and hours_per_week.isdigit():
    oen_week_wage = int(hourly_salary)*int(hours_per_week)
    monthly_salary = oen_week_wage*4
    yearly_salary= oen_week_wage*52
    print(f"The monthly salary for ${hourly_salary}/hr fro {hours_per_week} hours in a week is:{monthly_salary}")
    print(f"The total yearly salary for ${hourly_salary}/hr for {hours_per_week} hours in a week is: {yearly_salary} ")
else:    
    print("The entered value is invalid ")