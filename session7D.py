from session7B import flights


def search_by_carrier(flights, carrier):
    found = False

    for flight in flights:
        if flight['carrier'].lower() == carrier.lower():
            print(flight)
            found = True

    if not found:
        print("No Matching Flights Found")

def search_price_less_than(flights, price):
    found = False

    for flight in flights:
        if flight['fare'] < price:
            print(flight)
            found = True

    if not found:
        print("No Matching Flights Found")

def search_price_greater_than(flights, price):
    found = False

    for flight in flights:
        if flight['fare'] > price:
            print(flight)
            found = True

    if not found:
        print("No Matching Flights Found")

def search_duration_less_than(flights, duration):
    found = False

    for flight in flights:
        if flight['duration'] < duration:
            print(flight)
            found = True

    if not found:
        print("No Matching Flights Found")

def search_duration_greater_than(flights, duration):
    found = False

    for flight in flights:
        if flight['duration'] > duration:
            print(flight)
            found = True

    if not found:
        print("No Matching Flights Found")


def main():

    while True:

        print("\n========== Flight Search ==========")
        print("1. Search by Carrier")
        print("2. Search by Price Less Than")
        print("3. Search by Price Greater Than")
        print("4. Search by Duration Less Than")
        print("5. Search by Duration Greater Than")
        print("6. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            carrier = input("Enter Carrier Name: ")
            search_by_carrier(flights, carrier)

        elif choice == 2:
            price = int(input("Enter Maximum Price: "))
            search_price_less_than(flights, price)

        elif choice == 3:
            price = int(input("Enter Minimum Price: "))
            search_price_greater_than(flights, price)

        elif choice == 4:
            duration = float(input("Enter Maximum Duration (Hours): "))
            search_duration_less_than(flights, duration)

        elif choice == 5:
            duration = float(input("Enter Minimum Duration (Hours): "))
            search_duration_greater_than(flights, duration)

        elif choice == 6:
            print("Thank You!")
            break

        else:
            print("Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()