def Celsius_to_fahrenheit(c):
    return (c*9/5)+32

def  fahrenheit_to_celsius(f):
    return (f-32)*5/9


print("1.convert celsius to fahrenheit")
print("2.convert fahrenheit to celsius")


choice = float(input("choose 1 or 2 :"))

if choice == 1 :
    c=float(input("enter the celsius temperatuer value :"))
    print("Temperature in fahrenheit is =",Celsius_to_fahrenheit(c))

elif choice==2:
    f=float(input("enter the fahrenheit temperature value  :"))
    print("Temperature in celsius is =",fahrenheit_to_celsius(f))

else:
    print("Invalid choice")    