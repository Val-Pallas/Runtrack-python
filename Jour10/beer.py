# Import necessary libraries
import random

# Define the style of beer
style = input("What style of beer do you want to make? ")

# Define the base ingredients
base_grain = "2-row malt"
specialty_grain = "Crystal 60"
hops = "Cascade"
yeast = "California Ale yeast"

# Determine the amount of each ingredient based on the style of beer
if style == "IPA":
    base_grain_amount = random.uniform(10, 15)
    specialty_grain_amount = random.uniform(0.5, 1)
    hops_amount = random.uniform(1, 2)
    yeast_amount = random.uniform(1, 2)
elif style == "Stout":
    base_grain_amount = random.uniform(11, 16)
    specialty_grain_amount = random.uniform(1, 2)
    hops_amount = random.uniform(0.5, 1)
    yeast_amount = random.uniform(1, 2)
else:
    print("Sorry, that style is not currently supported.")

# Print out the recipe
print(f"Here's your {style} recipe:")
print(f"{base_grain_amount} lbs. of {base_grain}")
print(f"{specialty_grain_amount} lbs. of {specialty_grain}")
print(f"{hops_amount} oz. of {hops}")
print(f"{yeast_amount} packages of {yeast}")
