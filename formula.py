import json
f=open('123.json','r')
g=json.load(f)
print(g)
def sum(user):
    a=35*(user['answer_like']/user['answer']-user['answer_dis']/user['answer'])
    b=18*user['quest']
    c=30*user['answer']
    d=17*(user['quest_like']-user['answer_dis'])
    y=a+b+c+d
    return y
y=0
for i in g:
    y=sum(i)
    print(y,i)

def Lambda():

