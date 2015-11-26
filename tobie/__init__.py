from random import randint
import smtplib

list1 = ['TOBIE', 'KIM', 'JEFF', 'MORGAN','RAY','PEPET']
list2 = ['TOBIE', 'KIM', 'JEFF', 'MORGAN','RAY','PEPET','TOBIE', 'KIM', 'JEFF','RAY','PEPET']
dict = {}
for pigeur in list1:
    
    count = 0
    if('MORGAN'== pigeur):
        count = 1
    listChoix=['','']
    while (count < 2):
        
        
        index = randint(0,len(list2)-1)
        if(pigeur != list2[index]):
            print count, index
            listChoix[count] = list2[index]
            count = count + 1
            del list2[index]
    dict[pigeur] = listChoix

for key, value in dict.iteritems():
    file_ = open(key+'.txt', 'w')
    if('MORGAN'== key):
        file_.write(''.join(value))
    else:    
        file_.write(' et '.join(value))
    file_.close()        
    print "Successfully save"