from multiprocessing import Process
import time

class HighLevelProcess(Process):
    def __init__(self,
                 target,
                 args,
                 pid: int,
                 name: str,
                 priority: int,
                 is_io_bound: bool,
                 burst_time: int
    ) -> None:
        super().__init__(target=target, args=args, name=name)
        self.false_pid = pid
        self.priority = priority
        self.is_io_bound = is_io_bound
        self.burst_time = burst_time
        self.quantum_time = 0.002 # in seconds
        self.arrival_time = 0 # Can also be called as start_time
    
    def set_arrival_time(self):
        """Set arrival time as current time
        """
        self.arrival_time = time.time()
        
    def get_execution_time(self) -> float:
        """Get execution time based on current time subtracted to arrival_time
        (start_time)
        TODO: Consider execution time when the process is paused/wait

        Returns:
            float: the execution time the process has been running
        """
        return time.time() - self.arrival_time

    def get_remaining_burst_time(self) -> float:
        """Get remaining burst time based on arrival_time (start_time) 
        subtracted to current time
        TODO: Consider execution time when the process is paused/wait

        Returns:
            float: remaining burst time left
        """
        return (self.burst_time + self.arrival_time) - time.time()