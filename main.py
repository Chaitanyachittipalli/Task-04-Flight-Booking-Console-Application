from abc import ABC, abstractmethod


# 1. Abstraction: Base class defining the template
class Booking(ABC):

    def __init__(
        self,
        booking_id: int,
        passenger_name: str,
        flight_number: str,
        base_fare: float,
    ):
        # 2. Encapsulation: Private attributes
        self.__booking_id = booking_id
        self.__passenger_name = passenger_name
        self.__flight_number = flight_number
        self.__base_fare = base_fare

    # Getters
    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def passenger_name(self) -> str:
        return self.__passenger_name

    @property
    def flight_number(self) -> str:
        return self.__flight_number

    @property
    def base_fare(self) -> float:
        return self.__base_fare

    # 4. Polymorphism: Abstract method to be overridden by subclasses
    @abstractmethod
    def calculate_discount(self) -> float:
        pass

    # Method to calculate final payable fare
    def calculate_final_fare(self) -> float:
        discount = self.calculate_discount()
        return round(self.__base_fare - discount, 2)

    # Display booking ticket details
    def display_details(self) -> None:
        print("\n" + "=" * 42)
        print("         BOOKING RECEIPT (TICKET)        ")
        print("=" * 42)
        print(f" Booking ID    : {self.booking_id}")
        print(f" Passenger     : {self.passenger_name}")
        print(f" Flight Number : {self.flight_number}")
        print(f" Base Fare (₹) : ₹{self.base_fare:.2f}")
        print(f" Discount (₹)  : ₹{self.calculate_discount():.2f}")
        print(f" Final Fare (₹): ₹{self.calculate_final_fare():.2f}")
        print("=" * 42 + "\n")


# 3. Inheritance: Subclass for Regular passengers
class RegularBooking(Booking):

    def calculate_discount(self) -> float:
        return 0.0


# 3. Inheritance: Subclass for Student passengers
class StudentBooking(Booking):

    def calculate_discount(self) -> float:
        return round(self.base_fare * 0.10, 2)


# Input Validation Helpers
def get_valid_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Field cannot be empty. Please try again.")


def get_valid_fare(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt).strip())
            if val > 0:
                return val
            print("Error: Fare must be greater than zero.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")


# Main Application Manager
class FlightApp:

    def __init__(self):
        self.bookings = []
        self.counter = 101

    def book_flight(self) -> None:
        name = get_valid_string("Enter Passenger Name: ")
        flight_no = get_valid_string(
            "Enter Flight Number (e.g., AI-202 / 6E-554): "
        )
        fare = get_valid_fare("Enter Base Fare (₹): ")

        print("\nSelect Passenger Category:")
        print("1. Regular (0% Discount)")
        print("2. Student (10% Discount)")

        while True:
            choice = input("Enter choice (1 or 2): ").strip()
            if choice == "1":
                booking = RegularBooking(self.counter, name, flight_no, fare)
                break
            elif choice == "2":
                booking = StudentBooking(self.counter, name, flight_no, fare)
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        self.bookings.append(booking)
        print("\nFlight booked successfully!")
        booking.display_details()
        self.counter += 1

    def view_all_bookings(self) -> None:
        if not self.bookings:
            print("\nNo bookings found.")
            return

        print("\n" + "-" * 55)
        print(
            f"{'ID':<6}{'Name':<18}{'Flight':<10}{'Final Fare (₹)':<15}"
        )
        print("-" * 55)
        for b in self.bookings:
            print(
                f"{b.booking_id:<6}{b.passenger_name:<18}{b.flight_number:<10}{b.calculate_final_fare():<15.2f}"
            )
        print("-" * 55)

    def run(self) -> None:
        while True:
            print("\n=== FLIGHT BOOKING SYSTEM ===")
            print("1. Book a Flight")
            print("2. View All Bookings")
            print("3. Exit")

            opt = input("Choose an option (1-3): ").strip()
            if opt == "1":
                self.book_flight()
            elif opt == "2":
                self.view_all_bookings()
            elif opt == "3":
                print("\nExiting system. Have a great day!")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    app = FlightApp()
    app.run()