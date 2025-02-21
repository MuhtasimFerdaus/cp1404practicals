# Using f-string formatting
guitar_name = "Gibson L-5 CES"
guitar_price = 16036
print(f"{1922} {guitar_name} for about ${guitar_price:,}!")

# Using a for loop to format power of 2 outputs
for i in range(11):
    print(f"2 ^ {i:2} is {2**i:4}")