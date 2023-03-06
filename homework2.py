#homework2
#saerin bong

# problem 1
def print_name(name):
    print("The name is", name)

# print_name("saerin")

# problem 2
def ninety(a,b,c):
    d = 360 -(a+b+c)
    return d

# print(ninety(80,90,100))

# problem 3
def miles_per_hour(miles, hours, minutes, seconds):
    hourtime = hours + (1/60) * minutes + (1/3600)*seconds
    speed = miles / hourtime
    return speed

# print(miles_per_hour(20,2,21,16))

# problem 4
def greeting(name):
    if name == "Chris":
        print("Hello Chris")
    else:
        print("Goodbye")

# greeting("Chris")
# greeting("saerin")

# problem 5
def convert_temperature(temp, units):
    if units == "celsius":
        ftemp = temp*(9/5) + 32
        return ftemp
    elif units == "fahrenheit":
        ctemp = (temp - 32) * (5/9)
        return ctemp

#
# print(convert_temperature(50, "celsius"))
# print(convert_temperature(32, "fahrenheit"))

# problem 6
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif score < 60:
        return "F"

# print(calculate_grade(100))
# print(calculate_grade(90))
# print(calculate_grade(80))
# print(calculate_grade(70))
# print(calculate_grade(60))
# print(calculate_grade(50))
