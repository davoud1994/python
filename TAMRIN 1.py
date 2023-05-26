r = float(input("RADIOS:"))
Area = 3.14 * r ** 2
perimeter = 2 * 3.14 * r
input(print("Area :", Area, "\ primer :", perimeter, sep="  "))
# ----------------------------------->
Number = int(input("Number:"))
Square = Number ** 2
Cube = Number ** 3
input(print("Square :", Square, "\ Cube :", Cube, sep=" "))
# -------------------------------------->
Number1 = int(input("Number1:"))
Number2 = int(input("Number2:"))
N_POWER_N = Number1**Number2
input(print("N1^N2:", N_POWER_N))
# --------------------------------->
Number1 = float(input("Number1:"))
Number2 = float(input("Number2:"))
Number3 = float(input("Number3:"))
M = (Number1 + Number2 + Number3)/3
input(print("average:", M))

# ------/{STRING}/----->[2]
s = input(" enter string:")
count = s.count(".")
print("number of sentence is :", count)
u = input(" enter string:")
count = u.count(" ")+1
print("number of word is :", count)
s = input(" enter string:")
count = len(s[:])
print("the total number of elements: ", count)
s = input(" enter string:")
count1 = s.count(" ")+1
count2 = len(s[:])
total = count2 - count1
print("the total number of letter: ", total)
# ---------------------->
S = int(input("enter chr:"))
print("%c" % S)
# ----------------------->
S = input("phone number:")
print(S.isnumeric())
# --------------------------->

