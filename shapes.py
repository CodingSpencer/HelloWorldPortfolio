
def calc_rect_area(l, w):
    area = l * w
    return area


def calc_circle_area(r):
    area = 3.14 * r * r

def main():
    tri_area = calc_tri_area(20,79)
    print(tri_area)

    rect_area = calc_rect_area(20,79)

    print(rect_area)

    circle_area = calc_circle_area(20)

    print(circle_area)
def print_intro() :
    print("Hello World!")

def calc_tri_area(height,base):
    area = 1/2 * base * height
    return area

def main():
    print_intro()

    area = calc_tri_area(20, 40)
    print("The area of the triangle is: ", area)

if __name__ == "__main__":
    main()
