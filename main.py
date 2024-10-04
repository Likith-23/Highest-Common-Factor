larger_number = int(input("ENTER A LARGE NUMBER"))
smaller_number = int(input("ENTER A SMALL NUMBER"))
while (smaller_number):
    number_store = smaller_number
    smaller_number = larger_number % smaller_number
    larger_number = number_store
print("HCF is...", larger_number)
    