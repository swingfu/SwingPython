import statistics as st
from tabulate import tabulate

cal_list = []

def is_float_digit(n: str) -> bool:
    try:
        float(n)
        return True
    except ValueError:
        return False

print("Please input a list of numbers:\n")

while True: 
    x = input()
    if len(x) == 0 : 
        Count = len(cal_list)
        Sum = sum(cal_list)
        Max = max(cal_list)
        Min = min(cal_list)
        Mean = st.mean(cal_list)
        Median = st.median(cal_list)
        print(tabulate([["Count",Count],["Sum",Sum],["Max",Max],["Min",Min],["Mean",Mean],["Median",Median]],headers=['Calculation','Result']))
        break
    else :
        if is_float_digit(x) == False :
            print("Invalid number.")
        else:
            y = float(x)
            cal_list.append(y)
            # print(cal_list)
