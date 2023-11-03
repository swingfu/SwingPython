# Define the dial pad
key_map : dict[str, str] = {

 # Number key section
 '0': "0+",
 '1': "1",
 '2': "2ABC",
 '3': "3DEF",
 '4': "4GHI",
 '5': "5JKL",
 '6': "6MNO",
 '7': "7PQRS",
 '8': "8TUV",
 '9': "9WXYZ",

# Special sign keys on dial pad
 '+': "+",
 '*': "*",
 '#': "#",

# Other valid chars for phone number
 ' ': " ",
 '-': "-",
 '(': "(",
 ')': ")",
}

def dialpad(phone: str):
    if (phone == None or len(phone) == 0): 
        raise ValueError("Invalid phone number.")

    current_list = []

    # Loop through the phone number from left to right
    for key in phone:

        # Look up the map
        chars = key_map.get(key)
        if (chars == None):
            # Invalid character found
            raise ValueError("Invalid phone number.")

        # New temp set to be built for current key
        new_list = []

        for char in chars:
            # Loop through the existing left strings
            if (len(current_list) > 0):
                for left in current_list:
                    new_list.append(left + char)
            else:
                # First time case
                new_list.append(char)

        # Swap the two list for the next iteration
        current_list = new_list

    return current_list
