import threading
import time
from process import HighLevelProcess
from process_manager import HighLevelProcessManagerRR, HighLevelProcessManagerSRTF

print("Welcome to the JS Simulator! To create the process(es), pelase, enter the informations below\n")

amount = int(input("Process amount: "))
processes_created = []

for i in range(amount):
    process =  HighLevelProcess(
        pid = input("Process id: "),
        name = input("Process name: "),
        priority = input("Process priority: "),
        is_io_bound = input("Is this an I/O bound process? (True or False) "),
        burst_time = int(input("Process burst time: ")),
        arrival_time = int(input("Process arrival time: "))
    )
    processes_created.append(process)
    print("\n")

print("Now choose the scaling algorithm to run the processes")
print("1.Shortest Remaining Time First")
print("2.Round robin")
algorithm = input("Select a number: ")

if(algorithm == "1"):
    process_manager = HighLevelProcessManagerSRTF([processes_created[0]])
else:
    process_manager = HighLevelProcessManagerRR([processes_created[0]])

x = threading.Thread(target=process_manager.start)
x.start()

for my_process in processes_created:
    if(my_process != processes_created[0]):
        process_manager.put_into_queue_ready(my_process)
        time.sleep(1)