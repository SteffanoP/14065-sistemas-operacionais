from multiprocessing import Process
from queue import Queue

class HighLevelProcess(Process):
    def __init__(self,
                 target,
                 args,
                 pid: int,
                 name: str,
                 priority: int,
                 is_io_bound: bool,
                 total_cpu_time: int
    ) -> None:
        super().__init__(target=target, args=args, name=name)
        self.false_pid = pid
        self.priority = priority
        self.is_io_bound = is_io_bound
        self.total_cpu_time = total_cpu_time
        self.quantum_time = 2 #TODO: Should all process starts at 2 ms?

class HighLevelProcessManager():
    def __init__(self,
        scheduler_algorithm: str
    ) -> None:
        self.queue_ready = Queue(maxsize=10)
        self.scheduler = self.SCHEDULER_ALGORITHMS.get(scheduler_algorithm)

    def put_into_queue_ready(self, process: HighLevelProcess) -> None:
        """Put a process into the ready queue.

        Args:
            process (HighLevelProcess): the process to put into the queue.
        """
        self.queue_ready.put(process)

    def __shortest_job_first__(self):
        pass

    def __first_come_first_serve__(self):
        pass

    SCHEDULER_ALGORITHMS = {
        'fcfs': __first_come_first_serve__,
        'sjb': __shortest_job_first__
    }
