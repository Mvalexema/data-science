# calculation of the square of a triangle
import math
side1 = int(input("Please enter the lengths of side 1 of a triangle :"))
side2 = int(input("Please enter the lengths of side 2 of a triangle :"))
side3 = int(input("Please enter the lengths of side 3 of a triangle :"))
s = ((side1+side2+side3)/2)
areasqr = s*(s-side1)*(s-side2)*(s-side3)
area = math.sqrt(areasqr) 
print(area)