meter_reading = int(input("enter your meter reading :-"))

while meter_reading < 200:
    print(f"no need to pay any electricity bills")
    meter_reading+=1
if meter_reading > 200:
    print("pls pay the bill")