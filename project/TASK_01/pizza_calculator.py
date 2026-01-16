def get_valid_price(pizza_number):
    while True:
        try:
            price_input = input(f"Enter Price of Pizza #{pizza_number}: ")
            price = float(price_input)
            
            # Check if price is positive
            if price <= 0:
                print("Please enter a valid price!")
                continue
            
            return price
            
        except ValueError:
            # Handle non-numeric input
            print("Please enter a valid price!")


def calculate_order(prices):
    # Sort prices to find the cheapest one
    sorted_prices = sorted(prices)
    
    # Calculate total without discount
    original_total = sum(prices)
    
    # Calculate total with discount (remove cheapest pizza)
    discounted_total = sum(sorted_prices[1:])  # Skip the first (cheapest) item
    
    # Calculate discount amount and percentage
    discount_amount = original_total - discounted_total
    discount_percentage = (discount_amount / original_total) * 100
    
    return discounted_total, discount_percentage


def main():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    
    # Collect prices for 4 pizzas
    prices = []
    for i in range(1, 5):
        price = get_valid_price(i)
        prices.append(price)
    
    # Calculate the order total and discount
    total, discount = calculate_order(prices)
    
    # Display the results
    print(f"Order Total is £{total:.2f}, a fabulous discount of {discount:.0f}%!")


# Run the program
if __name__ == "__main__":
    main()