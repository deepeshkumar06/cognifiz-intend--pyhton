temp = float(input("Enter the Temperature value : "))
unit = (input("Enter the Unit of the Temperature : "))

def CelsiustoFahrenhiet(temp):
    return (temp * 9/5) + 32

def FahrenhiettoCelsius(temp):
    return (temp - 32) * 5/9

if( unit == "c" or unit == "C"):
    # print("Celcius")
    value = CelsiustoFahrenhiet(temp)
    print(f"{temp}°C is equal to {value:.2f}°F")


elif(unit == "f" or unit == "F") :
    # print("Farenhiet")
    value = FahrenhiettoCelsius(temp)
    print(f"{temp}°F is equal to {value:.2f}°C")

