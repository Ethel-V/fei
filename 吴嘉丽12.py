welcome = '\n 欢迎玩家来到英雄的世界！\n 剑之所指，邪魔尽退！'
mapmsg = '-------'
mapins = "\n 这是世界地图 \n %s \n 绿标是玩家本人 " %(mapmsg,)
worldmap = ['-','-','-','-','-','-','-']
instruction = '''
contrl your hero:|'a'for left |'d' for right |'w' for fly |'s' for down |'''

print(welcome)

n = input('input your name:')
hp = 100

if not n:
    n = '玩家一'

usermsg = {'n':n,'hp':hp}

print("Hi!",usermsg['n'],'You Hp is : ',usermsg['hp'])
print(mapins,instruction)

point = 0
while 1:
    worldmap[point] = "*"
    print('你在这里',"".join(worldmap))
    userinput = input('go or q:')

    if userinput == 'd' and point < 6:
        worldmap[point] = "-"
        print += 1
    elif userinput == 'a' and point > 0:
        worldmap[point] = "-"
        print -= 1
    elif userinput == 'q':
        print("goodbye!!")
        break
    else:
        print(instruction)
