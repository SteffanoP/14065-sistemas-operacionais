from process import HighLevelProcess
from process_manager import HighLevelProcessManagerRR, HighLevelProcessManagerSRTF

my_process_1 = HighLevelProcess(
    pid=1,
    name="Process 1",
    priority=0,
    is_io_bound=False,
    burst_time=7
)
my_process_2 = HighLevelProcess(
    pid=2,
    name="Process 2",
    priority=0,
    is_io_bound=False,
    burst_time=10
)
my_process_3 = HighLevelProcess(
    pid=3,
    name="Process 3",
    priority=0,
    is_io_bound=False,
    burst_time=5
)

process_manager = HighLevelProcessManagerSRTF([my_process_1,my_process_2,my_process_3])
process_manager.start()
