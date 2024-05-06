class Checkbook:
    def __init__(self):
        """
        Initialize a Checkbook object with a balance of 0.0.

        Function Description:
        - This method initializes a Checkbook
        object with an initial balance of $0.0.

        Parameters:
        - self: The instance of the Checkbook class being initialized.
        """
        self.balance = 0.0

    def handle_num_input(self, prompt):
        """
        Prompt the user for numeric input.

        Function Description:
        - This function prompts the user to enter a numeric value.

        Parameters:
        - prompt (str): The prompt to display to the user.

        Returns:
        - float: The numeric value entered by the user.
        """
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def deposit(self, amount):
        """
        Deposit funds into the checkbook.

        Function Description:
        - This method deposits a specified amount of
        funds into the checkbook.
        - It updates the balance and prints a
        confirmation message with the updated balance.

        Parameters:
        - self: The instance of the Checkbook class.
        - amount (float): The amount to deposit into the checkbook.

        Returns:
        - None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw funds from the checkbook.

        Function Description:
        - This method withdraws a specified amount of funds from the checkbook.
        - It checks if the withdrawal amount exceeds the current balance.
        - If there are sufficient funds, it updates
        the balance and prints a confirmation message with the updated balance.
        - If there are insufficient funds, it prints a message indicating so.

        Parameters:
        - self: The instance of the Checkbook class.
        - amount (float): The amount to withdraw from the checkbook.

        Returns:
        - None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Get the current balance of the checkbook.

        Function Description:
        - This method prints the current balance of the checkbook.

        Parameters:
        - self: The instance of the Checkbook class.

        Returns:
        - None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook.

    Function Description:
    - This function creates an instance of the
    Checkbook class and allows the user to perform
    various actions such as depositing funds,
    withdrawing funds, checking the balance, or exiting the program.

    Parameters:
    - None

    Returns:
    - None
    """
    cb = Checkbook()
    while True:
        action = (input("What would you like to do? "
                        "(deposit, withdraw, balance, exit): "))
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = cb.handle_num_input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = cb.handle_num_input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
