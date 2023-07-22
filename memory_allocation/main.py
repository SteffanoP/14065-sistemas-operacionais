from process import Process
from process_manager import ProcessManager

process_1 = Process(
    pid=1,
    name="P1",
    size=3,
    burst_time=0
)

process_2 = Process(
    pid=1,
    name="P2",
    size=4,
    burst_time=0
)

process_3 = Process(
    pid=1,
    name="P3",
    size=2,
    burst_time=0
)

process_4 = Process(
    pid=1,
    name="P4",
    size=1,
    burst_time=0
)

process_manager = ProcessManager([process_1, process_2, process_3, process_4])
process_manager.start()