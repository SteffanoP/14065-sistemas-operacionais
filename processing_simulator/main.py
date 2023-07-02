import threading
import time
from process import HighLevelProcess
from process_manager import HighLevelProcessManagerRR, HighLevelProcessManagerSRTF

my_process_1 = HighLevelProcess(
    pid=1,
    name="P1",
    priority=0,
    is_io_bound=False,
    burst_time=3,
    arrival_time=0
)
my_process_2 = HighLevelProcess(
    pid=2,
    name="P2",
    priority=0,
    is_io_bound=False,
    burst_time=8,
    arrival_time=0
)
my_process_3 = HighLevelProcess(
    pid=3,
    name="P3",
    priority=0,
    is_io_bound=False,
    burst_time=6,
    arrival_time=0
)
my_process_4 = HighLevelProcess(
    pid=4,
    name="P4",
    priority=0,
    is_io_bound=False,
    burst_time=4,
    arrival_time=0
)
my_process_5 = HighLevelProcess(
    pid=5,
    name="P5",
    priority=0,
    is_io_bound=False,
    burst_time=2,
    arrival_time=0
)

process_manager = HighLevelProcessManagerSRTF([my_process_1])
x = threading.Thread(target=process_manager.start)
x.start()
process_manager.put_into_queue_ready(my_process_2)
time.sleep(1)
process_manager.put_into_queue_ready(my_process_3)
time.sleep(1)
time.sleep(1)
process_manager.start()

process_manager = HighLevelProcessManagerRR([my_process_4,my_process_5])
process_manager.put_into_queue_ready(my_process_4)
time.sleep(1)
process_manager.put_into_queue_ready(my_process_5)