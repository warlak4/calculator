import math

def cal():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    
    choice = input("Введите номер операции")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
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
                print("Это не выш мат")
            else:
                result = num1 / num2
                print(result)
                
    elif choice in ['5', '6', '7', '8', '9', '10']:
        num = float(input("Введите число: "))
        
        if choice == '5':
            power = float(input("Введите степень: "))
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
            
    else:
        print("Подумай ещё раз и введи правильно ")