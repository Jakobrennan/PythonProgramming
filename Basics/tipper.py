# small program that determines how much you should tip
bill = int(raw_input("in numbers, type the total of your bill : "))
response = int(raw_input("do you want to tip 5, 10, 15 or 20 percent? (make sure answer is a number)"))

if response == 20:
    bill *= 0.2
    print(bill)
elif response == 15:
    bill *= 0.15
    print(bill)
elif response == 10:
    bill *= 0.10
    print(bill)
elif response == 5:
    bill *= 0.05
    print(bill)
else:
    bill *= 0.025
    print("the least you can do it pay ", bill)
