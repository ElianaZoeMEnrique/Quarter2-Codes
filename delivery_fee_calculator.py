def delivery_fee(distance, rate):
    fee = distance * rate
    return fee

distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

total_fee = delivery_fee(distance, rate)
print(f"Total Delivery Fee: ₱{total_fee:.2f}")