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