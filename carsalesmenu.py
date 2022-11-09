def return_data():
    global sales_list
    global customer_list
    global car_list

    with open("../cardealerdata.txt", "r") as file:
        txt = file.readlines()
        i = -1
        for line in txt:
            i = i + 1
            if line == "invoice\n":
                pass
            elif line == "customer\n":
                break
            else:
                line_list = line.split(",")
                invoice = {
                    "name": line_list[0],
                    "Surname": line_list[1],
                    "Address": line_list[2],
                    "model": line_list[3],
                    "price": line_list[4],
                    "ID": line_list[5],
                }
                sales_list.append(invoice)

        for line in txt[i + 1 :]:
            i = i + 1
            if line == "car\n":
                break
            else:
                line_list = line.split(",")
                new_customer = {
                    "Name": line_list[0],
                    "Surname": line_list[1],
                    "Address": line_list[2],
                    "Phone": line_list[3],
                    "Brand": line_list[4],
                }
                customer_list.append(new_customer)

        for line in txt[i + 1 :]:
            line_list = line.split(",")
            new_car = {
                "brand": line_list[0],
                "model": line_list[1],
                "year": line_list[2],
                "color": line_list[3],
                "price": line_list[4],
            }
            car_list.append(new_car)


def save_data():
    global sales_list
    global customer_list
    global car_list
    with open("../cardealerdata.txt", "w") as file:
        file.write("invoice\n")
        for invoice in sales_list:
            print(invoice)
            file.write(
                invoice["Name"]
                + ","
                + invoice["Surname"]
                + ","
                + invoice["Address"]
                + ","
                + invoice["model"]
                + ","
                + invoice["price"]
                + ","
                + invoice["ID"]
                + "\n"
            )
        file.write("customer\n")
        for customer in customer_list:
            print(customer)
            file.write(
                customer["Name"]
                + ","
                + customer["Surname"]
                + ","
                + customer["Address"]
                + ","
                + customer["Phone"]
                + ","
                + customer["Brand"]
                + "\n"
            )
        file.write("car\n")
        for car in car_list:
            print(car)
            file.write(
                car["brand"]
                + ","
                + car["model"]
                + ","
                + car["year"]
                + ","
                + car["color"]
                + ","
                + car["price"]
                + "\n"
            )


def sale():  # option 6
    global sales_list
    global customer_list
    global car_list
    customer_index = int(input("enter customer index"))
    car_index = int(input("enter car index"))
    invoice = {
        "Name": customer_list[customer_index]["Name"],
        "Surname": customer_list[customer_index]["Surname"],
        "Address": customer_list[customer_index]["Address"],
        "model": car_list[car_index]["model"],
        "price": car_list[car_index]["price"],
        "ID": str(len(sales_list)),
    }

    car_list.pop(car_index)

    sales_list.append(invoice)


def remove_customer():  # option 5
    global customer_list
    index = int(input("enter customer index to remove :"))
    customer_list.pop(index)


def add_customer():  # option 4
    global customer_list
    new_customer = {
        "Name": input("Please enter the name : "),
        "Surname": input("Please enter the surname : "),
        "Address": input("Please enter the address : "),
        "Phone": input("Please enter the phone: "),
        "Brand": input("Please enter the brand: "),
    }
    customer_list.append(new_customer)


def remove_car():
    # option 2
    global car_list
    index = int(input("enter car index to remove :"))
    car_list.pop(index)


def add_car():  # option 1
    global car_list
    new_car = {
        "brand": input("Please enter the brand : "),
        "model": input("Please enter the model : "),
        "year": input("Please enter the year : "),
        "color": input("Please enter the color : "),
        "price": input("Please enter the price : "),
    }
    car_list.append(new_car)


def print_menu():
    print("0= list of cars")
    print("1= add a car to list")
    print("2 =remove a car from list")
    print("3= list of customers")
    print("4= add the customers")
    print("5= remove the customer")
    print("6= sell car to customer")
    print("7= list of sales")
    print("e = exit program")
    print("8 = save data")
    print("9 = return data")


car_list = []
customer_list = []
sales_list = []

while True:
    print_menu()
    options = input("Choose number from menu !")
    if options == "0":
        print(car_list)
    elif options == "1":
        add_car()
    elif options == "2":
        remove_car()
    elif options == "3":
        print(customer_list)
    elif options == "4":
        add_customer()
    elif options == "5":
        remove_customer()
    elif options == "6":
        sale()
    elif options == "7":
        print(sales_list)
    elif options == "e":
        break
    elif options == "8":
        save_data()
    elif options == "9":
        return_data()

    else:
        print("Your input is wrong !")
