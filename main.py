#coding challenge 1

print("This program will calculate the McPython bill for a couple with a gift certificate, with a VAT of 20.0%.")

gift_Certificate_Value = float(input("Enter gift certificate value: "))
print("Enter ordered items for person 1.")
app_1 = float(input("Appetiser: "))
ent_1 = float(input("Entree: "))
dri_1 = float(input("Drinks: "))
des_1 = float(input("Dessert: "))


print("\nEnter ordered items for person 2.")
app_2 = float(input("Appetiser: "))
ent_2 = float(input("Entree: "))
dri_2 = float(input("Drinks: "))
des_2 = float(input("Dessert: "))

total = app_1 + app_2 + ent_1 + ent_2 + dri_1 + dri_2 + des_1 + des_2
print("Ordered items:", total)
print("Restaurant tax:", total*0.2)
print("Bill:", gift_Certificate_Value -(total*1.2))