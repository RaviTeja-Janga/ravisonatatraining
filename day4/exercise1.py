dict={"ravi":'13-04-2001',"teja":'25-10-2000',"swathi":'3-09-2000',"chandu":'21-12-2000',"sreenu":"12-10-1999"}
print(">>>Welcome to bithdays dictionary.we know bithdays of :")
for name in dict:
    print(name)
print('Whos birthday do you want to look up?')
name = input()
if name in dict:
    print(name +' has birthday on ' + dict[name])
else:
     print('we dont have' + name + 'birthday' )