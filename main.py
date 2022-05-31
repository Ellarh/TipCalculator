print("Welcome to the Tip Calculator!")

total_bill = float(input("What is the total bill? $"))
percentage_tip = int(input("What percentage tip will you like to give? 10, 12 or 15: "))
number_of_people = int(input("How many people will split the bill? "))

bill_with_tip = percentage_tip * total_bill / 100
new_bill = bill_with_tip + total_bill

final_amount = new_bill / number_of_people
bill_per_person = round(final_amount, 2)
bill_per_person = "{:.2f}".format(final_amount)

print(f"Each person will pay ${bill_per_person}")
