from process import Process
from process_manager import ProcessFirstFitAlgorithm

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

process_manager = ProcessFirstFitAlgorithm([process_1, process_2, process_3, process_4])
process_manager.start()