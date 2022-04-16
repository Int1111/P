from random import*
# лайки и дизлайки ответов 35%
# кол вопросов которое задал пользователь 18%
# кол ответов которое дал пользователь 30%
# колличетво лайков/д на вопрос 17%
Matrix={}
import json
f=open('123.json','w')

def summary():
    answer_like=randint(0,100)
    answer_dis=randint(0,100)
    quest=randint(0,100)
    answer=randint(0,100)
    quest_like=randint(0,100)
    quest_dis=randint(0,100)
    return {
        'answer_like':answer_like,
        'answer_dis':answer_dis,
        'quest' : quest,
        'answer' :answer,
        'quest_like' :quest_like,
        'quest_dis' : quest_dis
    }
users=[summary() for i in range(4)]
print(users)
json.dump(users,f)
#f.close()
def T(users):
    for i in users:
       print(i)
       for i2 in i.keys():
            if i2 not in Matrix:
                Matrix[i2] = []
            Matrix[i2].append(i[i2])
    print(Matrix)


T(users)


