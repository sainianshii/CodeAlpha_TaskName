#  Task: 2 Stock Portfolio Tracker

# Predefined stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 310,
    "GOOGL": 140,
    "AMZN":135

}

# Dictionary to store user's stock portfolio
portfolio = {}

print("Welcome to Stock Portfolio Tracker\n")
print("Available stocks and prices (in USD):")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Taking user input for portfolio
while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish):").upper()

    if stock_name == "DONE":
        break
    elif stock_name not in stock_prices:
        print("Invalid stock symbol! Please chose from the available list.")
        continue

    try:
        quantity =  int(input(f"Enter quantity of  {stock_name}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0!")
            continue 
    except ValueError:
        print("Invalid input! Please enter  a number. ")
        continue

    # Add to portfolio 
    if stock_name in portfolio:
        portfolio[stock_name] += quantity 
    else:
        portfolio[stock_name] = quantity 

    # Calculate total investment

    total_investment = 0 
    
    with open("portfolio_summary.text", "w") as file:

     
        file.write("Stock Portfolio Summary\n")

        file.write("------------------------------------\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity 
            total_investment += investment
            file.write(f"{stock} - {quantity} shares x ${price} = ${investment}\n")

          
        file.write("---------------------------------------------\n")
        file.write(f" Total Investment Value: ${total_investment}\n")
    
    
    print("\n Your Stock Portfolio Summary ")
    print("------------------------------------------")
    print(f"Total Investment Value: ${total_investment}")
    print("\n Portfolio saved successfully in 'portfolio_summary.txt'")

    
        



        



