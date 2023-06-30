from multiprocessing import Process

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
