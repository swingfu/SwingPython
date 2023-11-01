import string 

# to build the dialpad dataset.
ori_dialpad = {'0':['0','+'],
               '1':['1'], 
               '2':['A','B','C'], 
               '3':['D','E','F'], 
               '4':['G','H','I'],
               '5':['5','J','K','L'],
               '6':['6','M','N','O'], 
               '7':['7','P','Q','R','S'], 
               '8':['8','T','U','V'], 
               '9':['9','W','X','Y','Z'],
               '*':['*'],
               '#':['#']}


# to check the user's input is in right format.
def phone_format(input_number) -> string:
    new_number = input_number.replace("-","").replace("(","").replace(")","").replace(" ","")
    try:
        intphone = int(new_number)
        len(new_number) == 10
        return new_number
    except ValueError:
        print("invalid format")

# calculate the permutation of the phone numbers.
def permutation(new_number) -> list:
    final_combo=[]
    new_loop = []
    last_round = []
    last_round.append(new_number)
    for i in range(0,10):
        x = new_number[i]
        y = ori_dialpad[x]
        for k in range(len(y)):
            z = y[k]
            for n in range(len(last_round)):
                current_job = last_round[n].replace(last_round[n][i],z)
                new_loop.append(current_job)
        last_round.extend(new_loop)
        new_loop.clear()
    final_combo.extend(last_round)
    #print(final_combo)
    return final_combo
       

# Main operation function. 
def dialPad() -> list:
    #print("please input 10 number: \n")
    input_number = input()
    new_number = phone_format(input_number)
    permutation(new_number)

dialPad()
