def is_inside(point,rectangle):
    for i in point:
        x = i
        y = i
        if 140 <= x <= 240 and 60 <= y <= 260:
            return True
        else: 
            return False
check_inside = is_inside([200, 120],[140,60,100,200])
if check_inside == True:
    print('inside')
else:
    print('outside')

