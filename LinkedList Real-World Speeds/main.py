#name: Harrison Olvera
#date: 5/18/2025

from LinkedList import LinkedList
from Client import Client
from datetime import date
import time
import random

#display name and date in output
name = "Harrison Olvera"
date = date.today()
print(name)
print(date)
print()

clients = []
#read records into client list
input_file_name = "ClientData.csv"
with open(input_file_name) as infile:
    for line in infile:
        s = line.split(',')
        client_id = int(s[0])
        f_name = s[1]
        l_name = s[2]
        phone = s[3]
        email = s[4]

        #create a client object
        clt = Client(client_id, f_name, l_name, phone, email)
        clients.append(clt)


#number of records
num_records = len(clients)

#create linked list object
my_linked_list = LinkedList()

#Scenario 1: Printer Queue
section_title = "Scenario: Printer Queue or Call Queue"
print(section_title)
print("-" * len(section_title))

#add records to linked list
start_time = time.time()
for i in range(num_records):
    my_linked_list.add_last(clients[i])
end_time = time.time()

total_time = end_time - start_time
print("Seconds to add records: {:.6f}".format(total_time))

#How long does it take to remove records from the front of the linked list
start_time = time.time()
for i in range(num_records):
    my_linked_list.remove_first()
end_time = time.time()

total_time = end_time - start_time
print("Seconds to remove records from front: {:.6f}".format(total_time))

#Scenario 2: Customer service center
section_title = "Scenario: Customer Service Center"
print(section_title)
print("-" * len(section_title))

#adding records back into linked list
for i in range(num_records):
    my_linked_list.add_last(clients[i])

#how long does it take to randomly display 1000 records
start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print(my_linked_list.search(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to display random records: {:.6f}".format(total_time))


#Scenario 3: call center
section_title = "Scenario: Call Center"
print(section_title)
print("-" * len(section_title))

#how long does it take to add records, randomly display 1000 records, and randomly remove 1000 records
start_time = time.time()

current_id = 100001 + num_records + 1
for i in range(1000):
    my_linked_list.add_last(Client(current_id))
    current_id = current_id + 1

#display random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print(my_linked_list.search(Client(random_num)))

#remove random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print(my_linked_list.remove(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to add, display, and remove records: {:.6f}".format(total_time))

