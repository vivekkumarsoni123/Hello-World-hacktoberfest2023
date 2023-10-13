import random
from random import randint
option = ['rock' , 'paper' , 'scissor']
while(True):
    ask = input("Your Turn")
    ans = option[randint(0,2)]
    print(ans)
    if(ask == ans):
        print('Draw!')
        again_play = input('want to play more?(y/n)')
        if(again_play == 'y'):
            continue
        else :
            break
    elif(ask=='paper' and ans=='rock'):
        print('You Win!')
        again_play = input('want to play more?(y/n)')
        if(again_play == 'y'):
            continue
        else :
            break 
    elif(ask=='scissor' and ans=='paper'):
        print('You Win!')
        again_play = input('want to play more?(y/n)')
        if(again_play == 'y'):
            continue
        else :
            break 
    elif(ask=='paper' and ans=='scissor'):
        print('You Lose!')
        again_play = input('want to play more?(y/n)')
        if(again_play == 'y'):
            continue
        else :
            break 
    elif(ask=='rock' and ans=='scissor'):
        print('You Win!')
        again_play = input('want to play more?(y/n)')
        if(again_play == 'y'):
            continue
        else :
            break 
    elif(ask=='scissor' and ans=='rock'):
        print('You Lose!')
        again_play = input('want to play more?(y/n)')
        if(again_play == 'y'):
            continue
        else :
            break 
    elif(ask=='rock' and ans=='paper'):
        print('You Lose!')
        again_play = input('want to play more?(y/n)')
        if(again_play == 'y'):
            continue
        else :
            break 
