#set my user input to represent the temperature.

temperature = (input("Add a number for temeratue (e.g. 45F or 30C.) "))
degree = int(temperature[:-1])
intial_conversion = temperature[:-1]

if intial_conversion.upper == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_conversion = "fahrenheit"

elif intial_conversion.upper == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_conversion = "celcius"

else:
    print("input proper conversion")
    quit()

print("The temperature in", o_conversion, "is", result, "degrees.")



