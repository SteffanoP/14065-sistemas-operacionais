class Process():
    def __init__(self,
                 pid: int,
                 name: str,
                 size: int ## MB
    ) -> None:
        self.pid = pid
        self.name = name
        self.size = size