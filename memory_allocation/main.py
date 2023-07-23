import threading
import time
from process import Process
from memory_manager import MemoryBestFitAlgorithm, MemoryFirstFitAlgorithm

processes_created = []

process_1 = Process(
    pid=0,
    name="P1",
    size=212,
    arrival_time=0,
    burst_time=0
)

process_2 = Process(
    pid=1,
    name="P2",
    size=417,
    arrival_time=0,
    burst_time=0
)

process_3 = Process(
    pid=2,
    name="P3",
    size=112,
    arrival_time=0,
    burst_time=0
)

process_4 = Process(
    pid=3,
    name="P4",
    size=426,
    arrival_time=0,
    burst_time=0
)

memory_manager_first_fit = MemoryFirstFitAlgorithm([process_1, process_2, process_3, process_4])
memory_manager_first_fit.start()
memory_manager_best_fit = MemoryBestFitAlgorithm([process_1, process_2, process_3, process_4])
memory_manager_best_fit.start()