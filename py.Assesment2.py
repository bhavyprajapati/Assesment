orders = []
order_id = 1

parts = {"screen": 150, "battery": 80, "port": 45, "speaker": 35}
service_fee = 50
tax_rate = 0.10


def show_menu():
    print("\n1. New Order")
    print("2. View Orders")
    print("3. Complete Order")
    print("4. Generate Bill")
    print("5. Exit")


def new_order():
    global order_id
    
    name = input("\nCustomer Name: ")
    device = input("Device Type: ")
    issue = input("Issue: ")
    date = input("Due Date: ")
    
    order = {
        "id": order_id,
        "name": name,
        "device": device,
        "issue": issue,
        "date": date,
        "status": "pending",
        "parts": []
    }
    
    orders.append(order)
    print(f"\nOrder ID: {order_id}")
    order_id += 1


def view_orders():
    print("\n--- All Orders ---")
    for order in orders:
        print(f"\nID: {order['id']}")
        print(f"Customer: {order['name']}")
        print(f"Device: {order['device']}")
        print(f"Issue: {order['issue']}")
        print(f"Status: {order['status']}")


def complete_order():
    order_num = int(input("\nOrder ID: "))
    
    order = None
    for o in orders:
        if o['id'] == order_num:
            order = o
            break
    
    if not order:
        print("Order not found")
        return
    
    print("\nParts: screen, battery, port, speaker")
    
    while True:
        part = input("Part name (or done): ")
        if part == "done":
            break
        if part in parts:
            qty = int(input("Quantity: "))
            order['parts'].append((part, qty))
    
    order['status'] = "completed"
    print("Order completed")


def generate_bill():
    order_num = int(input("\nOrder ID: "))
    
    order = None
    for o in orders:
        if o['id'] == order_num:
            order = o
            break
    
    if not order:
        print("Order not found")
        return
    
    print("\n--- INVOICE ---")
    print(f"Order ID: {order['id']}")
    print(f"Customer: {order['name']}")
    print(f"Device: {order['device']}")
    
    parts_total = 0
    print("\nParts:")
    for part, qty in order['parts']:
        cost = parts[part] * qty
        parts_total += cost
        print(f"{part}: {qty} x ${parts[part]} = ${cost}")
    
    print(f"\nService Fee: ${service_fee}")
    
    subtotal = parts_total + service_fee
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")


while True:
    show_menu()
    choice = input("\nChoice: ")
    
    if choice == "1":
        new_order()
    elif choice == "2":
        view_orders()
    elif choice == "3":
        complete_order()
    elif choice == "4":
        generate_bill()
    elif choice == "5":
        print("Goodbye")
        break
