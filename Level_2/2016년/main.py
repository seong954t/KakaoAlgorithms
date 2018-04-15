def getDayName(a,b):
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return days[(sum(month_day[:a])+b)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5, 24))