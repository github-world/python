#.__author__.=,"likeu"
#.Date:

# y1= 1999
# print(y1 % 200 ==0)
# y2=2300
# print(y2 %4 == 0 and y2 % 100 !=0)
#闰年计算

year = 2005
if year % 400 == 0:
    print('case1:%d is leap year' % year)
elif year % 4 == 0 and year % 100 != 0:
    print('case2:%d is leap year' % year)
else:
    print('cast3:%d is not leap year' % year)