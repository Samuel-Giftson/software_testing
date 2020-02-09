import os
#
#
def retirement():
    while(True):
        try:
            user_age=int(input("Enter your age: "))
            if(user_age>100):
                print(" ")
                print("Retirement calculator is not valid for age over 100 years")
                print(" ")
                continue
            user_annual_salary=int(input("Enter your annual salary: "))
            percentage_saved=int(input("Enter percentage Saved of your monthly salary: "))
            desired_goal=int(input("Enter savings goal: "))
            break

        except:
            print("Enter valid values.")
            print("")
            exi=input("Do you want to exit out of BMI calculator, type \"yes\" to exit, or type \"no\" to continue: ")
            exi=exi.lower()
            if(exi=="yes"):
                print("")
                main()
            continue
    monthly_salary=user_annual_salary/12
    monthly_saving=monthly_salary*(percentage_saved/100)
    monthly_saving=monthly_saving+(monthly_saving*(35/100))
    yearly_saving=monthly_saving*12
    years_to_achieve=desired_goal/yearly_saving

    if(years_to_achieve+user_age>100):
        print("Can't achieve this with your age less than 100 years. ")
    else:
        print("Numbers of years to achieve your goal: "+str(years_to_achieve))
        print("Age where the goal will be met: "+str(years_to_achieve+user_age))
    return 0,0
        
    
        
    
            
    
def body_mass_index():
    print("Welcome to Body mass index calculator. ")
    while(True):
        try:
            print("")
            weight_pounds=int(input("Enter weight in pounds: "))
            height_feet_inches=input("Enter height in format feet\'inches\" ")
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
            exi=input("Do you want to exit out of BMI calculator, type \"yes\" to exit, or type \"no\" to continue: ")
            exi=exi.lower()
            if(exi=="yes"):
                main()
 
            continue
    weight_kilograms=weight_pounds*0.45
    height_meters=((height_feet*12)+(height_inches))*0.025
    BMI_=""
    BMI=(weight_kilograms)/(height_meters**2)
    if(BMI<=18.5):
        BMI_="underweight"
    elif(BMI>18.5 and BMI<24.9):
        BMI_="normal weight"
    elif(BMI>25 and BMI<29.9):
        BMI_="over weight"
    elif(BMI>=30):
        BMI_="obese"
    return BMI, BMI_

    


def main():
    print(" ")
    print("Welcome to the command-line interface")
    while(True):
        print(" ")
        print("""

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
                print("Type in a number within the range of the options given.")
                continue
        BMI, BMI_ = eval(options[user_choice])
        if(BMI and BMI_):
            print("Your BMI: "+str(round(BMI,2)))
            print("Your BMI category: "+str(BMI_))   
    
        
main()
