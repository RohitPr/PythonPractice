# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcisstic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


def narcissistic(value):
    temp_value = value
    sum = 0

    while temp_value > 0:
        temp = temp_value % 10
        sum += temp**3
        temp_value //= 10

    if sum == value:
        return True
    else:
        return False
