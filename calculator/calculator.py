from ast import While
import math

a = 1
while a == 1:
    print("Select operation:")
    print("1. plusik")
    print("2. minus")
    print("3. umnogenie")
    print("4. delenie")
    print("5. ctepen")
    print("6. koren kavdrat")
    print("7. faktorial")
    print("8. sin")
    print("9. cos")
    print("10. tan")
    print("0. exit")
    
    choice = input("Select number operation: ")
    
    if choice in ['1', '2', '3', '4']:
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
        
         if choice == '1':
            result = num1 + num2
            print(result)
         elif choice == '2':
            result = num1 - num2
            print(result)
         elif choice == '3':
            result = num1 * num2
            print(result)
         elif choice == '4':
            if num2 == 0:
               print("IT IS NO HIGHER MATH")
            else:
               result = num1 / num2
               print(result)
                
    elif choice in ['5', '6', '7', '8', '9', '10']:
         num = float(input("Enter number: "))
        
         if choice == '5':
             power = float(input("Kakaya stepen: "))
             result = num ** power
             print(result)
         elif choice == '6':
             result = math.sqrt(num)
             print(result)
         elif choice == '7':
             result = math.factorial(int(num))
             print(result)
         elif choice == '8':
             result = math.sin(num)
             print(result)
         elif choice == '9':
             result = math.cos(num)
             print(result)
         elif choice == '10':
             result = math.tan(num)
             print(result)
    elif choice in ['0']:
        if choice == '0':
            break
   
            
