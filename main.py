larger_number = int(input("ENTER A LARGE NUMBER: "))
smaller_number = int(input("ENTER A SMALL NUMBER: "))
def calculate_lcm(larger_number, smaller_number):
    original_larger = larger_number
    original_smaller = smaller_number
    while smaller_number:
        number_store = smaller_number
        smaller_number = larger_number % smaller_number
        larger_number = number_store
    lcm = abs(original_larger * original_smaller) // number_store
    return lcm
lcm_result = calculate_lcm(larger_number, smaller_number)
print("THE LCM IS >>>", lcm_result)