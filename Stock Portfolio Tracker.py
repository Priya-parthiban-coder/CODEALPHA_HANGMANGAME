def main():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2700, "MSFT": 300}

    stock_name = input("Enter stock name (e.g. AAPL, TSLA): ").upper()
    if stock_name not in stock_prices:
        print("Stock not found in the price list.")
        return

    try:
        quantity = int(input("Enter quantity of stocks: "))
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    total_investment = stock_prices[stock_name] * quantity
    print(f"Total investment for {quantity} shares of {stock_name}: ${total_investment}")

    save_option = input("Do you want to save the result to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        filename = input("Enter filename (with .txt or .csv extension): ").strip()
        try:
            with open(filename, "w") as file:
                if filename.endswith(".csv"):
                    file.write("Stock,Quantity,Price per Share,Total Investment\n")
                    file.write(f"{stock_name},{quantity},{stock_prices[stock_name]},{total_investment}\n")
                else:
                    file.write(f"Stock: {stock_name}\nQuantity: {quantity}\nPrice per Share: ${stock_prices[stock_name]}\nTotal Investment: ${total_investment}\n")
            print(f"Result saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main() 