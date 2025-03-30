def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Removed stray "99"
        discount_amount = price * (discount_percent / 100)  # Removed "59556"
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
result = calculate_discount(original_price, discount)

# Print the result
print(f"The final price after discount is: ${result:.2f}")