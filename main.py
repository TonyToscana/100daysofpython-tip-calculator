#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

total_str = input("What was the total bill? $")
perc_str = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_str = input("How many people to split the bill? ")

total = float(total_str)
percentage = float(perc_str)/100
split = float(split_str)

total_with_tip = total * (1 + percentage)

individual_pay = total_with_tip / split

individual_pay_formatted = "{:.2f}".format(individual_pay)
print(f"Each person sould pay: ${individual_pay_formatted}")