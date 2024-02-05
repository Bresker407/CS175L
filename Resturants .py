#CS175L
#Benedetto Aiello
#Restaurant
 
vegetarian = input("Is anyone in your party vegetarian? (yes/no): ")
vegan = input("Is anyone in your party vegan? (yes/no): ")
gluten_free = input("Is anyone in your party gluten-free? (yes/no): ")
 
print("\nHere are the suitable restaurants for your group:")
if vegetarian == 'yes' and vegan == 'no' and gluten_free == 'no':
    print("- Mama’s Fine Italian")
    print("- Main Street Pizza Company")
    print("- Corner Café")
    print("- The Chef’s Kitchen")
elif vegetarian == 'yes' and vegan == 'no' and gluten_free == 'yes':
    print("- Corner Café")
    print("- Mama’s Fine Italian")
    print("- The Chef’s Kitchen")
elif vegetarian == "no" and vegan == 'no' and gluten_free == "yes":
    print("- Corner Café")
    print("- The Chef’s Kitchen")
    print("- Main Street Pizza Company")
elif vegetarian == "yes" and vegan == 'no' and gluten_free == "yes":
    print("- Corner Café")
    print("- The Chef’s Kitchen")
    print("- Main Street Pizza Company")
elif vegetarian == "no" and vegan == 'no' and gluten_free == 'no':
    print("- Joe's Gorumet Burgers")
    print("- Main Street Pizza Company")
    print("- Corner Café")
    print("- Mama’s Fine Italian")
    print("- The Chef’s Kitchen")
else:
    print("- Corner Café")
    print("- The Chef’s Kitchen")
       
