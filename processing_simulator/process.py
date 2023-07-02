class HighLevelProcess():
    def __init__(self,
                 pid: int,
                 name: str,
                 priority: int,
                 is_io_bound: bool,
                 burst_time: int
    ) -> None:
        self.pid = pid
        self.name = name
        self.priority = priority
        self.is_io_bound = is_io_bound
        self.burst_time = burst_time
        self.quantum_time = 0.002 # in seconds
        self.arrival_time = 0 # Can also be called as start_time

    def set_arrival_time(self, arrival_time: int):
        """Set arrival time
        """
        self.arrival_time = arrival_time

    def get_execution_time(self, current_time: int) -> int:
        """Get execution time based on current time
        TODO: Consider execution time when the process is paused/wait

        Returns:
            int: the execution time the process has been running
        """
        return current_time - self.arrival_time

    def get_remaining_burst_time(self, current_time) -> int:
        """Get remaining burst time based on arrival_time (start_time) 
        subtracted to current time
        TODO: Consider execution time when the process is paused/wait

        Returns:
            int: remaining burst time left
        """
        return (self.burst_time + self.arrival_time) - current_time
