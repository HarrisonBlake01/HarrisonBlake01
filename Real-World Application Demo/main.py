#Name: Harrison Olvera
#Date: 5/24/2025

from Queue import Queue
from Call import Call
from datetime import date
import time
import random

name = "Harrison Olvera"
date = date.today()
print("Name: ", name)
print("Date: ", date)

#create a calls list
calls = []

#file name as input
input_file_name = "CallsData.csv"
with open(input_file_name) as infile:
    for line in infile:
        #split the line based on commas
        s = line.split(',')
        client_id = int(s[0])
        client_name = s[1]
        client_phone = s[2]
        #Create a call object
        a_call = Call(client_id, client_name, client_phone)
        calls.append(a_call)


#queue object for our calls
calls_waiting = Queue()
call_number = 0

seconds = 5

for i in range(seconds):
    print("-"*40)
    time.sleep(2) #pause for 2 seconds
    random_event = random.randint(1,3)
    #do an event based on random_event
    if random_event == 1:
        print("Call received. Caller added to the queue")
        calls_waiting.enqueue(calls[call_number])
        call_number += 1 #to set up the next call
        print("\tNumber of calls waiting in the queue: ", calls_waiting.get_length())
    elif random_event == 2:
        print("Call sent to service representative")
        if calls_waiting.get_length() > 0:
            print("Caller information")
            print(calls_waiting.dequeue())
        else:
            print("The call waiting queue is empty")
        print("\tNumber of calls waiting in the queue: ", calls_waiting.get_length())
    else:
        print("Nothing happened during this time")
        print("\tNumber of calls waiting in the queue: ", calls_waiting.get_length())
print("\nThe Automatic Call Distributor simulation has completed")
