from process import HighLevelProcess, HighLevelProcessManager

process_manager_fcfs = HighLevelProcessManager(scheduler_algorithm='fcfs')

# TODO: Create object process
my_process = HighLevelProcess()
process_manager_fcfs.put_into_queue_ready(my_process)
