
li=list()
li2=[]

li.append(3)
li.append(2)
li.append(4)

print(li)
print('Using traditional method for conditions with if\n\n')
x=True
# if x:
#     print('This is the true condtion')
# else:
#     print('this is the false condition')

print('This is the true condition ') if x else  print('this is the false condition')

for x in range(1,5):
    print(x)

l2=[x for x in range(0,101)]

print(l2)

print('even Values in the list from 0 to 100')
even_list=[]
for x in range(0,101):
    if x%2==0:
        even_list.append(x)
event_list_new=[ x  for x in range(0,101)  if x%2==0]


print('\neven Values in the comprehension list from 0 to 100')
print(event_list_new)
