from lab_oop.rectangle import Rectangle
from lab_oop.circle import Circle
from lab_oop.square import Square
#import arrow

def main():
    r = Rectangle("синего", 5,6)
    c = Circle("красного",11)
    s = Square("желтого",11)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()