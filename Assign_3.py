def calculate_discount(price, discount_percent):
    # function to calculate the final price after applying a discount
    if discount_percent >= 20:
        discount_amount =price * (discount_percent/100)
        
        final_price = price - discount_amount
        return final_price
    else:
        return price
# User input section
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")

    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numerical values for the price and discount percentage.")