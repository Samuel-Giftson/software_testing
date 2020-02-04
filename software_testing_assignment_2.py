import os
def retirement():
    while(True):
        try:
            user_age=int(input("Enter your age: "))
            user_annual_salary=int(input("Enter your annual salary: "))
            percentage_saved=int(input("Enter percentage Saved: "))
            desired_goal=int(input("Enter savings goal: "))
            break

        except:
            print("Enter valid values.")
            print("")
            continue
    monthly_salary=user_annual_salary/12
    monthly_saving=monthly_salary*(percentage_saved/100)
    yearly_saving=monthly_saving*12
    years_to_achieve=desired_goal/yearly_saving

    if(years_to_achieve+user_age>100):
        print("Can't achieve this with your age less than 100 years. ")
    else:
        print("NUmbers of years to achieve your goal: "+str(years_to_achieve))
        
    
        
    
            
    
def body_mass_index():
    print("Welcome to Body mass index calculator. ")
    while(True):
        try:
            print("")
            weight_pounds=input("Enter weight in pounds: ")
            height_feet_inches=input("Enter height in format feet\'inches\" ")

            if(weight_pounds=="main menu" or height_feet_inches=="main menu"):
                main()
            height_feet=int(height_feet_inches[:height_feet_inches.find("\'")])
            height_inches=int(height_feet_inches[(int(height_feet_inches.find("\'"))+1):height_feet_inches.index("\"")])
#            print(height_feet)
#            print(height_inches)
        
#            if(True):
#                continue
#            else:
            break
        
        except:
            print("Enter valid values")
            continue
    weight_kilograms=weight_pounds*0.45
    height_meters=((height_feet*12)+(height_inches))*0.025

    BMI=(weight_kilograms)/(height_meters**2)
    print("Your BMI: "+str(BMI))

    

    


def main():
    print("""
Welcome to the command-line interface

    1) Body Mass Index
    2) Retirement
    3) exit()

""")

    options=["","body_mass_index()","retirement()","os._exit(0)"]
    while(True):
        try:
            user_choice=int(input("Enter opition number: "))
            break
        except:
            print("Type in a number within the range of the number.")
            continue
    eval(options[user_choice])
    
        
main()
