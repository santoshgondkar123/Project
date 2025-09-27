import json
import os
from datetime import datetime

PRODUCTS_FILE = 'products.json'
SALES_FILE = 'sales.json'

def load_data(file):
    if not os.path.exists(file):
        return []
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
        
def add_product():
    products = load_data(PRODUCTS_FILE)
    product_id = input("Enter Product ID: ").strip()
    
    if any(p['product_id'] == product_id for p in products):
        print("Error: Product ID already exists!")
        return
    name = input("Enter Product Name: ").strip()
    try:
        price = float(input("Enter Price: "))
        stock_quantity = int(input("Enter Stock Quantity: "))
    except ValueError:
        print("Error: Invalid input for price or quantity.")
        return
    product = {
        'product_id': product_id,
        'name': name,
        'price': price,
        'stock_quantity': stock_quantity
    }
    products.append(product)
    save_data(PRODUCTS_FILE, products)
    print("Product added successfully.")
def view_products():
    products = load_data(PRODUCTS_FILE)
    if not products:
        print("No products available.")
        return
    print("Available Products:")
    print("-" * 50)
    for p in products:
        print(f"ID: {p['product_id']} | Name: {p['name']} | Price: {p['price']} | Stock: {p['stock_quantity']}")
    print("-" * 50)

def sell_product():
    products = load_data(PRODUCTS_FILE)
    sales = load_data(SALES_FILE)
    product_id = input("Enter Product ID to sell: ").strip()
    product = next((p for p in products if p['product_id'] == product_id), None)

    if not product:
        print("Error: Product not found.")
        return

    try:
        quantity = int(input(f"Enter Quantity to sell (Available: {product['stock_quantity']}): "))
    except ValueError:
        print("Error: Invalid quantity.")
        return
    if quantity <= 0 or quantity > product['stock_quantity']:
        print("Error: Insufficient stock or invalid quantity.")
        return
    total_price = quantity * product['price']
    product['stock_quantity'] -= quantity
    sale = {
        'sale_id': f"SALE{len(sales)+1:04}",
        'product_id': product_id,
        'quantity': quantity,
        'total_price': total_price,
        'date_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    sales.append(sale)
    save_data(PRODUCTS_FILE, products)
    save_data(SALES_FILE, sales)
    print(f"Sale successful! Total price: {total_price}")

def view_sales():
    sales = load_data(SALES_FILE)
    if not sales:
        print("No sales recorded yet.")
        return
    print("Sales Records:")
    print("-" * 80)
    for s in sales:
        print(f"Sale ID: {s['sale_id']} | Product ID: {s['product_id']} | Quantity: {s['quantity']} | Total Price: {s['total_price']} | Date: {s['date_time']}")
    print("-" * 80)
    
def stock_report():
    products = load_data(PRODUCTS_FILE)
    if not products:
        print("No products available.")
        return
    print("Current Stock Report:")
    print("-" * 50)
    for p in products:
        print(f"ID: {p['product_id']} | Name: {p['name']} | Stock: {p['stock_quantity']}")
    print("-" * 50)


def top_selling_product():
    sales = load_data(SALES_FILE)
    products = load_data(PRODUCTS_FILE)

    if not sales:
        print("No sales data available.")
        return

    product_sales = {}
    for sale in sales:
        pid = sale['product_id']
        product_sales[pid] = product_sales.get(pid, 0) + sale['quantity']

    top_product_id = max(product_sales, key=product_sales.get)
    top_product = next(p for p in products if p['product_id'] == top_product_id)
    print("Top-Selling Product:")
    print(f"ID: {top_product['product_id']} | Name: {top_product['name']} | Units Sold: {product_sales[top_product_id]}")


def search_product():
    products = load_data(PRODUCTS_FILE)
    query = input("Enter product name or ID to search: ").strip().lower()
    found = [p for p in products if query in p['product_id'].lower() or query in p['name'].lower()]
    if not found:
        print("No matching product found.")
        return
    print("Search Results:")
    for p in found:
        print(f"ID: {p['product_id']} | Name: {p['name']} | Price: {p['price']} | Stock: {p['stock_quantity']}")


def daily_sales_summary():
    sales = load_data(SALES_FILE)
    today = datetime.now().strftime("%Y-%m-%d")
    today_sales = [s for s in sales if s['date_time'].startswith(today)]

    total_revenue = sum(s['total_price'] for s in today_sales)
    total_products_sold = sum(s['quantity'] for s in today_sales)

    print("Daily Sales Summary:")
    print(f"Date: {today}")
    print(f"Total Revenue: {total_revenue}")
    print(f"Total Products Sold: {total_products_sold}")

def main_menu():
    while True:
        print(" Mini Inventory & Sales Tracker")
        print("1. Add New Product")
        print("2. View All Products")
        print("3. Sell Product")
        print("4. View Sales Records")
        print("5. View Stock Report")
        print("6. Top-Selling Product")
        print("7. Search Product")
        print("8. Daily Sales Summary")
        print("9. Exit")

        choice = input("Enter choice (1-9): ").strip()
        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            sell_product()
        elif choice == '4':
            view_sales()
        elif choice == '5':
            stock_report()
        elif choice == '6':
            top_selling_product()
        elif choice == '7':
            search_product()
        elif choice == '8':
            daily_sales_summary()
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
    
view_products()
sell_product()
view_sales()
stock_report()
top_selling_product()
search_product()
daily_sales_summary()

