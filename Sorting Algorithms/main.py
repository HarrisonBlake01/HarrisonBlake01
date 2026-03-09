#name: Harrison Olvera
#date: 6/1/2025

from MergeSort import MergeSort
from Client import Client
from datetime import date
import time

name = "Harrison Olvera"
date = date.today()
print("Name: ",name)
print("Date: ",date)
#input_file_name = 'ClientData100.csv'
#input_file_name = 'ClientData1000.csv'
#input_file_name = 'ClientData10000.csv'
input_file_name = 'ClientData100000.csv'

#create a list called clients
clients = []
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

#Scenario: Sorting records from a datafile
section_title = "Scenario: Sorting "+str(num_records) + " Records"
print(section_title)
print("-"*len(section_title))

#how long does it take?
start_time = time.time()

MergeSort.sort(clients)
end_time = time.time()

total_time = end_time - start_time
print("Seconds to sort {} records: {:.6f}".format(num_records, total_time))

#display the sorted list
#for clt in clients:
#    print(clt)
