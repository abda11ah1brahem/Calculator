def add(x, y):
    return  x + y
def subt(x, y):
    return x - y
def multip(x,y):
    return x*y
def div(x, y):
    return x/y
available_num=[1,2,3,4]
while True:
    print("""
    1.add
    2.subtract
    3. multiple
    4.divide""")
    user_input=int(input("Please enter process number : "))
    if user_input in available_num:
        firs_num=float(input("Please enter First number : "))
        sec_num=float(input("Please enter socend number : "))
        if user_input == 1:
            print(add(firs_num, sec_num))
        elif user_input == 2:
            print(subt(firs_num, sec_num))
        elif user_input == 3:
            print(multip(firs_num, sec_num))
        elif user_input == 4:
            print(div(firs_num, sec_num))
        choice = input("Do you want cont. ?? [yes \ no ]")
        if choice == "no":
            break
    else:
        print("invalid number ")
