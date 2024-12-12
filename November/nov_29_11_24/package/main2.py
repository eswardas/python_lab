from Graphics.circle import *
from Graphics.rectangle import *
from Graphics.Graphics_3d import cuboid
from Graphics.Graphics_3d import sphere

while True:

    option = int(input("1.Area of circle\n2.Perimeter of circle\n3.Area of Rectangle\n4.Perimeter of rectangle\n5.Total surface area of cuboid\n6.Volume of cuboid\n7.Total surface area of sphere\n8.Volume of sphere\n9.Exit\nSelect an option: "))
    if option == 1:
        radius = float(input("Enter the radius of the circle: "))
        circle_area(radius)
        print()
    elif option == 2:
        radius = float(input("Enter the radius of the circle: "))
        circle_perimeter(radius)
        print()
    elif option == 3:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        rect_area(length, width)
        print()
    elif option == 4:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        rect_perimeter(length, width)
        print()
    elif option == 5:
        length = float(input("Enter the length of the cuboid: "))
        breadth = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        cuboid.cuboid_area(length,breadth,height)
        print()
    elif option == 6:
        length = float(input("Enter the length of the cuboid: "))
        breadth = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        cuboid.cuboid_volume(length,breadth,height)
        print()
    elif option == 7:
        radius = float(input("Enter the radius of the sphere: "))
        sphere.sphere_area(radius)
        print()
    elif option == 8:
        radius = float(input("Enter the radius of the sphere: "))
        sphere.sphere_volume(radius)
        print()
    elif option == 9:
        break



