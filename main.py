import time
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def type_effect(message, second,end="", flush=True):
    for char in message:
        time.sleep(second)
        print(char, end=end, flush=flush)
    #print()

def check_winnings(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
                winning += values[symbol] * bet
                winning_lines.append(line + 1)
    
    return winning, winning_lines
    

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #.items() gives key : value pair in dictionary
        for _ in range(symbol_count): # _ is anonymous variable , use when we don't need variable to loop through
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # [:] is copy the list 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): # need at least one columns, otherwise breakout
        for i, column in enumerate(columns): # enumerate gives index and value
            if i != len(columns) - 1:
                type_effect(column[row], second=0.7,end="|")
            else:
                type_effect(column[row], second=0.7)
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            message = f">>You do not have enough to bet on that amount, your current balance is: ${balance}\n>>You need another ${total_bet - balance} to be able to bet on that amount \n"
            type_effect(message, second=0.03)
        else:
            break
    message = f">>You are betting ${bet} on {lines} lines with the balance of ${balance}.\n>>Total bet is equal to ${total_bet}\n"
    type_effect(message, second=0.03)
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    type_effect(f">>You won ${winnings}\n", second=0.03)
    print(f">>You won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        type_effect(f"Current balance is ${balance}\n", second=0.05)
        answer = input("Press Enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    type_effect(f">>You left with ${balance}\n", second=0.05)
    
main()