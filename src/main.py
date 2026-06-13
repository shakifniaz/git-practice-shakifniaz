from datetime import datetime
from utils import add, subtract, multiply, divide

print("Name: Your Name")
print("Date:", datetime.today().strftime("%d-%m-%Y"))

print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))
print("Division:", divide(15, 3))