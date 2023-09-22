import calculation
import sys

input_a = int(input("Enter a: "))
input_b = int(input("Enter b: "))

print("Addition: ", calculation.add(input_a, input_b))
print("Subtraction: ", calculation.sub(input_a, input_b))
print("Multiplication: ", calculation.mul(input_a, input_b))
print("Division: ", calculation.div(input_a, input_b))


def list_installed_modules():
    print(sys.modules.keys())


list_installed_modules()
