import math

def cal():
    print("�������� ��������:")
    print("1. ��������")
    print("2. ���������")
    print("3. ���������")
    print("4. �������")
    print("5. ���������� � �������")
    print("6. ���������� ������")
    print("7. ���������")
    print("8. �����")
    print("9. �������")
    print("10. �������")
    
    choice = input("������� ����� ��������")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("������� ������ �����: "))
        num2 = float(input("������� ������ �����: "))
        
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
                print("��� �� ��� ���")
            else:
                result = num1 / num2
                print(result)
                
    elif choice in ['5', '6', '7', '8', '9', '10']:
        num = float(input("������� �����: "))
        
        if choice == '5':
            power = float(input("������� �������: "))
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
        print("������� ��� ��� � ����� ��������� ")