import threading
import time
from process import Process
from process_manager import ProcessFirstFitAlgorithm

processes_created = []

process_1 = Process(
    pid=0,
    name="P1",
    size=3,
    arrival_time=0,
    burst_time=0
)

process_2 = Process(
    pid=1,
    name="P2",
    size=4,
    arrival_time=0,
    burst_time=0
)

process_3 = Process(
    pid=2,
    name="P3",
    size=2,
    arrival_time=0,
    burst_time=0
)

process_4 = Process(
    pid=3,
    name="P4",
    size=1,
    arrival_time=0,
    burst_time=0
)

processes_created.append(process_1)
processes_created.append(process_2)
processes_created.append(process_3)
processes_created.append(process_4)

process_manager = ProcessFirstFitAlgorithm([process_1])

x = threading.Thread(target=process_manager.start)
x.start()

for my_process in processes_created:
    if(my_process != processes_created[0]):
        process_manager.put_into_queue_ready(my_process)
        time.sleep(1)

# process_manager = ProcessFirstFitAlgorithm([process_1, process_2, process_3, process_4])
# process_manager.start()