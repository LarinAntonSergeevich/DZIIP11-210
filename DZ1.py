countp = 0
countn = 0
count = 0
stop = 0
nums = []
from random import randint
while stop ==0:
    x= randint (0, 9)
    nums.append(x)
    print ('Угадай число : ')
    y = int (input())
    if x == y:
        countp +=1
        print ('Угадал, ЧИТЕР!!! ')
    else:
        countn += 1
        print('Неправильно, ЛООООООООХ')
    print ('Попробуешь ещё?')
    no = str (input())
    if no == 'q' :
        print ('% твоих првильных ответов = ', countp/(countn + countp) * 100)
        for i in range(len(nums)) :
            print(nums[i])
            print(count)
        stop += 1
