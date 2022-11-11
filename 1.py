chisla = (input("ЧИСЛА НА БОЧКУ\n")).split(' ')
number = [int(x) for x in chisla]
suy = list(filter(lambda x: (x > 0), number))
n = 1
proiz = lambda suy:suy[0] * proiz(suy[1:]) if suy else 1
print(proiz(suy))
