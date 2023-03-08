#2007 1월 1일 -> MON

# 3 14 WED

if __name__ == '__main__':
    a,b = map(int, input().split())

    if a == 1 :
        full_days = b
    if a == 2 :
        full_days = 31 + b
    if a == 3 :
        full_days = 59 + b
    if a == 4 :
        full_days = 90 + b
    if a == 5 :
        full_days = 120 + b
    if a == 6 :
        full_days = 151 + b
    if a == 7 :
        full_days = 181 + b
    if a == 8 :
        full_days = 212 + b
    if a == 9 :
        full_days = 243 + b
    if a == 10 :
        full_days = 273 + b
    if a == 11 :
        full_days = 304 + b
    if a == 12 :
        full_days = 334 + b

    day = full_days % 7

    if day == 1 :
        day_str = 'MON'
    if day == 2 :
        day_str = 'TUE'
    if day == 3 :
        day_str = 'WED'
    if day == 4 :
        day_str = 'THU'
    if day == 5 :
        day_str = 'FRI'
    if day == 6 :
        day_str = 'SAT'
    if day == 0 :
        day_str = 'SUN'

    print(day_str)

