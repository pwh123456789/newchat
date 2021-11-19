'''
name = 'pwh'
age = 18
print('我的名字是：'+ name +  ',年龄：'+str(18))
print('我的名字是%s，年龄：%d' %(name,age))
print('名字{1}，年龄{0}'.format(name,age))
'''

score = int(input('请输入你的成绩：'))
if score >= 90:
    print('%d，你的成绩很优秀'% score)
elif score >= 80:
    print('%d，你的成绩良好'% score)
elif score >= 60:
    print('%d，你的成绩及格'% score)
else:
    print('%d，不及格'% score)