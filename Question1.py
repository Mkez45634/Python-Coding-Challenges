# Question 1
import math


#Rectangular Prism side1 x side2 x side3
side1Prism = int(input("Please enter side 1 of the rectangular prism."))
side2Prism = int(input("Please enter side 2 of the rectangular prism."))
side3Prism = int(input("Please enter side 3 of the rectangular prism."))
Prism = side1Prism*side2Prism*side3Prism
print("The volume of the Rectangular Prism is " + str(Prism) + ".")


#Cylinder pi x radius x radius x height
radiusCylinder = int(input("Please enter the radius of the Cylinder."))
heightCylinder = int(input("Please enter the height of the Cylinder."))
Cylinder = math.pi*radiusCylinder*radiusCylinder*heightCylinder
print("The volume of the Cylinder is " + format(Cylinder,'.2f')+ " to 2dp.")

#Sphere 4/3 x pi x radius x radius
radiusSphere = int(input("Please enter the radius of the Sphere."))
Sphere = (4/3)*math.pi*radiusSphere*radiusSphere
print("The volume of the Sphere is " + format(Sphere,'.2f')+ " to 2dp." )
