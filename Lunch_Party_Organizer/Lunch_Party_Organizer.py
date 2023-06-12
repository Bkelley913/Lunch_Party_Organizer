# Define the initial menu item as "pizza"
menu_item = "pizza"

# Define the number of guests as 11
guests = 11

# Print the menu item and number of guests
print(menu_item)
print(guests)

# Update the menu item to "biryani"
menu_item = "biryani"

# Print the updated menu item
print("Updated menu item is: " + menu_item)

# Define the quantity of biryanu needed per person
biryani_per_person = 1

# Calculate the total quantity of biryani needed
biryani_needed = biryani_per_person * guests

# Define the quantity of biryani prepared
biryani_prepared = 10

# Check if there is enough biryanu prepared
enough_biryani = biryani_prepared == biryani_needed

# Increment the number of guests by 1
guests += 1

# Calculate the quantity of biryani per guest
biryani_per_guest = biryani_prepared / guests

# Print the quantity of biryani per guest
print(biryani_per_guest)
