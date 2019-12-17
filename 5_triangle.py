a = int(input("Enter 1st triangle side length: "))
b = int(input("Enter 2nd triangle side length: "))
c = int(input("Enter 3rd triangle side length: "))

if a == b == c:
    print ("This is equilateral triangle")
elif a == b != c or a == c != b or b == c != a:
    print ("This is isosceles triangle")
elif a != b != c:
    print ("This is multilateral triangle")
