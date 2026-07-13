
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def prime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"

    return "Prime"


number = int(input("Enter a number: "))

print("The number is", even_odd(number))
print("The number is", prime(number))