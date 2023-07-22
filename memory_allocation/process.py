class Process():
    def __init__(self,
                 pid: int,
                 name: str,
                 size: int, ## MB
                 arrival_time: int,
                 burst_time: int,
    ) -> None:
        self.pid = pid,
        self.name = name,
        self.size = size,
        self.arrival_time = arrival_time,
        self.burst_time = burst_time,

    ## I guess we won't need this...
    def set_arrival_time(self, arrival_time: int):
        """Set arrival time
        """
        self.arrival_time = arrival_time