def is_leap(year):
    leap = False
    if 1900 <= year <= (10**5):
        if year % 4 == 0:
            b = year / 100
            c = year / 400
            if b == 0:
                leap = False
                elif c == 0:
                 leap = True

    # Write your logic here
    return leap

year = int(input())
print(is_leap(year))