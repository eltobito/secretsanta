from random import randint
import smtplib

#####Settings 
participants = ['TOBIE', 'KIM', 'JEFF', 'RAY','PEPET']
participants_exception = ['MORGAN']
number_of_pick_by_person = 2
number_of_pick_by_person_exception = 1
#####

names_to_pick = []
result = {}

# Set list of name to pick Regular
for participant in participants:
    i=0
    while i < number_of_pick_by_person :
        names_to_pick.append(participant)
        i = i + 1

# Set list of name to pick Exception
for participant in participants_exception:
    i=0
    while i < number_of_pick_by_person_exception :
        names_to_pick.append(participant)
        i = i + 1    

#Exception pick first
for draw in participants_exception:   
    count = 0
    listChoix=[]
    while (count < number_of_pick_by_person_exception):

        index = randint(0,len(names_to_pick)-1)
        if(draw != names_to_pick[index]):
            listChoix.append(names_to_pick[index])
            count = count + 1
            del names_to_pick[index]
    result[draw] = listChoix

#Regular picker    
for draw in participants:   
    count = 0
    listChoix=[]
    while (count < number_of_pick_by_person):

        index = randint(0,len(names_to_pick)-1)
        if(draw != names_to_pick[index]):

            listChoix.append(names_to_pick[index])
            count = count + 1
            del names_to_pick[index]
    result[draw] = listChoix

#Put result in a file for each paticipant. 
for key, value in result.iteritems():
    file_ = open(key+'.txt', 'w')
    if(len(value) == 1):
        receiver = ''.join(value)
        file_.write(receiver)
        #print receiver
    else:    
        receiver = ' and '.join(value)
        file_.write(receiver)
        #print receiver
    file_.close()        
    print "File with name(s) picked successfully created for partipant "+key
    
print "\n\n** Now send the right file to the right participant by email manuelly **"
