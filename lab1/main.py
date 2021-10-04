import math
import argparse
print("Рябова В.В. ИУ5-55Б")
complete = 'y'
parser = argparse.ArgumentParser()
parser.add_argument("--A", help="Коэффициент А Биквадратного уравнения", type=float)
parser.add_argument("--B", help="Коэффициент B Биквадратного уравнения", type=float)
parser.add_argument("--C", help="Коэффициент C Биквадратного уравнения", type=float)
args = parser.parse_args()
print ("Введите коэффициенты А, В, С биквадратного уравнения Ах^4+Bx^2+C=0\n")
while complete == 'y':
    A = args.A
    B = args.B
    C = args.C
    if A == None and B == None and C == None:
        A = input('A= ')
        B = input('B= ')
        C = input('C= ')
    try:
        A = float(A)
        B = float(B)
        C = float(C)
    except ValueError:
        print('Введены некорректные символы, повторите ввод.')
    enter = 1
    #while enter != "0":
    #A = float(input("A = "))
    #B = float(input("B = "))
    #C = float(input("C = "))
    if A == 0:
        if B == 0:
            if C == 0:
                print("x - любое число\n")
            else:
                print("Корней нет\n")
        else:
            discriminant = -C / B
            if discriminant > 0:
                print("x1 = ", -math.sqrt(discriminant))
                print("x2 = ", math.sqrt(discriminant))
            elif discriminant < 0:
                print("Корней нет\n")
            else:
                print("x1 = 0 \n")
                print("x2 = 0 \n")
    else:
        if B == 0:
            if C == 0:
                print("x1 = 0 \n")
                print("x2 = 0 \n")
            else:
                discriminant = -C / A
                if discriminant < 0:
                    print("Корней нет\n")
                else:
                    print("x1 = ", math.sqrt(discriminant))
                    print("x2 = ", -math.sqrt(discriminant))
        else:
            discriminant = B ** 2 - 4 * A * C
            if discriminant < 0:
                print("Корней нет\n")
            elif discriminant == 0:
                t = (- B + math.sqrt(discriminant)) / (2 * A)
                if t < 0:
                    print("Корней нет\n")
                elif t == 0:
                    print("x1 = 0 \n")
                    print("x2 = 0 \n")
                else:
                    print("x1 = ", math.sqrt(t))
                    print("x2 = ", -math.sqrt(t))
            else:
                t1 = (- B + math.sqrt(discriminant)) / (2 * A)
                t2 = (- B - math.sqrt(discriminant)) / (2 * A)
                if t1 > 0:
                    print("x1 = ", math.sqrt(t1))
                    print("x2 = ", -math.sqrt(t1))
                    if t2 > 0:
                        print("x3 = ", math.sqrt(t2))
                        print("x4 = ", -math.sqrt(t2))
                    elif t2 == 0:
                        print("x3 = 0")
                        print("x4 = 0")
                elif t1 == 0:
                    print("x1 = 0")
                    print("x2 = 0")
                    if t2 > 0:
                        print("x3 = ", math.sqrt(t2))
                        print("x4 = ", -math.sqrt(t2))
                    elif t2 == 0:
                        print("x3 = 0")
                        print("x4 = 0")
                    else:
                        if t2 > 0:
                            print("x1 = ", math.sqrt(t2))
                            print("x2 = ", -math.sqrt(t2))
                        elif t2 == 0:
                            print("x1 = 0")
                            print("x2 = 0")
                        else:
                            print("Корней нет")
        #enter = input("Продолжить? 1.да 0.нет")
