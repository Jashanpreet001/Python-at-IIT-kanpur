#Assignment 4
#1
total_cost=float(input("Enter the total cost of your dream house"))
portion_down_payment=0.25
down_payment=portion_down_payment*total_cost
current_savings=0
r=0.04# annual interest rate

annual_salary=float(input("Enter your annual salary"))
monthly_salary=annual_salary/12
portion_saved= float(input("Enter the portion, in decimals of the monthly salary you save"))

months=0
monthly_interest=0

while(current_savings<down_payment):
    current_savings=current_savings + monthly_salary*portion_saved + monthly_interest
    monthly_interest= current_savings*r/12
    months=months+1
    
print(months)
    

#2
total_cost=float(input("Enter the total cost of your dream house"))
portion_down_payment=0.25
down_payment=portion_down_payment*total_cost
current_savings=0
r=0.04# annual interest rate

annual_salary=float(input("Enter your annual salary"))
monthly_salary=annual_salary/12
portion_saved= float(input("Enter the portion, in decimals of the monthly salary you save"))

months=0
monthly_interest=0

semi_annual_raise= float(input("Enter the percentage of your salary increased every 6 months as a decimal"))

while(current_savings<down_payment):
    current_savings=current_savings + monthly_salary*portion_saved + monthly_interest
    monthly_interest= current_savings*r/12
    months=months+1
    if(months%6==0):
        monthly_salary+=monthly_salary*semi_annual_raise
print(months)

#3
semi_annual_raise = 0.07
r= 0.04
portion_down_payment = 0.25
house_cost=100000
down_payment=portion_down_payment*house_cost
total_months=36

annual_salary = float(input("enter the current annual salary"))

## current_savings should be within 100 of down_payment in 36 moonths.

## This while loop iterates over different values of portion_saved
lower_lim_ps = 0 ##lower limit of search space for portion_saved, initializing
upper_lim_ps = 10000 ## upper limit of search space for portion_saved, initializing
ps = 0
numGuess = 0
portion_saved_prev = -999
current_savings=0.0
portion_saved = 0.0
months = 0
monthly_interest=0
starting_annual_salary = annual_salary

while(abs(down_payment - current_savings)>100):
    portion_saved_prev = portion_saved
    numGuess = numGuess + 1
    
    print(abs(down_payment - current_savings)>100)
    ##updating portion_saved using bisection search.
    if(down_payment>current_savings):
        lower_lim_ps = ps
    else:
        upper_lim_ps = ps
    ps = int((lower_lim_ps + upper_lim_ps)/2)    
    portion_saved = ps/10000

    if(portion_saved == portion_saved_prev):
        print("It is not possible to pay the down payment in three years")
        break

    print(current_savings)
    for i in range(total_months):
        current_savings=current_savings + current_savings*r/12 + (annual_salary/12)*portion_saved

        if(i%6==0 and not i==0):
            annual_salary = annual_salary + annual_salary*semi_annual_raise


print('portion_saved:{}, numGuess:{}'.format(portion_saved, numGuess))
    
