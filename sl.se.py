def fares(age, student=False, senior=False):
    if student or senior:
        return 'halv'
    else:
        if age <20 or age >65:
            return 'halv'
        else:
            return 'hel'


print 'child 20', fares(20)
print 'student 10',fares(10)
print 'vuxen 35', fares(35)
print 'senior 65', fares(15)

print 'Hej'