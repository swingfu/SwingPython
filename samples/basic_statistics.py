import statistics as st
from tabulate import tabulate

    
# Function to calcuate the statistics
def calculate_stats(data) -> str:

    _count = len(data)

    if (_count == 0) :
        # Special log to handle edge case without any data
        data = [0]

    _sum = sum(data)
    _max = max(data)
    _min = min(data)
    _mean = st.mean(data)
    _median = st.median(data)

    rows = [
        ["Count",   _count],
        ["Sum",     _sum],
        ["Max",     _max], 
        ["Min",     _min],
        ["Mean",    _mean], 
        ["Median",  _median]]

    tab = tabulate(rows, headers = ['Calculation', 'Result'])
    return tab


# Define the list to store valid numbers
cal_list = []

# Loop flag used for while control
loop = True

print("Please input a list of numbers:")

while loop: 

    # Take input from user line by line
    inputStr = input()

    if len(inputStr) > 0: 
       
        # User input some non-empty text
        try:
            # Conver to float, note that this may fail due to invalid input
            inputNum = float(inputStr)

            # Valid input and add to list
            cal_list.append(inputNum)

        except ValueError:
            # Invaid input
            print("Invalid number. Please input again.")

    else:
        # User pressed the enter key without typing anything in this line
        # Done with populating the list
        # Calcuate the stats and output
        print(calculate_stats(cal_list))

        # Break from the loop and exit the program
        loop = False
