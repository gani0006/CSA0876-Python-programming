def find_lsd_msd(number):
    number_str = str(number)

    lsd = int(number_str[-1])

    msd = int(number_str[0])
    
    return lsd, msd

number = 1010101
lsd, msd = find_lsd_msd(number)
print(f"The Least Significant Digit (LSD) of {number} is {lsd}")
print(f"The Most Significant Digit (MSD) of {number} is {msd}")
