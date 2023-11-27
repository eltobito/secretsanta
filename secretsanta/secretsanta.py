#!/usr/bin/env python

from random import randint
import settings as conf
import datetime

names_to_pick = []
result = {}
x = datetime.datetime.now()
anne = x.year
# Set list of name to pick Regular
for participant in conf.participants:
    i=0
    while i < conf.number_of_pick_by_person :
        names_to_pick.append(participant)
        i = i + 1

#Regular picker
for draw in conf.participants:
    count = 0
    listChoix=[]
    while (count < conf.number_of_pick_by_person):

        index = randint(0,len(names_to_pick)-1)
        if(draw != names_to_pick[index]):

            listChoix.append(names_to_pick[index])
            count = count + 1
            del names_to_pick[index]
    result[draw] = listChoix



#Put result in a file for each paticipant.
for key, value in result.items():
    file_ = open(key+'.txt', 'w')
    if(len(value) == 1):
        line  = "\nHOHOHO Vous avez  pigé pour NOËL "+ str(anne) +": "+str(value)
        line += "\nHOHOHO Vous avez  pigé pour NOËL "+ str(anne) +": "+str(value)
        line += "\nHOHOHO Vous avez  pigé pour NOËL "+ str(anne) +": "+str(value)
        line += "\nHOHOHO Vous avez  pigé pour NOËL "+ str(anne) +": "+str(value)
        receiver = ' '.join(line)
        file_.write(receiver)
        if conf.show_result:
            print(receiver)
    else:
        receiver = ' and '.join(value)
        file_.write(receiver)
        if conf.show_result:
            print(receiver)
    file_.close()
    print("File with name(s) picked successfully created for participant "+key)

print("\n\n** Now send the right file to the right participant by email manuelly **")
