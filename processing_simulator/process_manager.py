from process import HighLevelProcess

class HighLevelProcessManager():
    def __init__(self, processes: list[HighLevelProcess]) -> None:
        self.queue_ready = processes

    def put_into_queue_ready(self, process: HighLevelProcess) -> None:
        """Put a process into the ready queue.

        Args:
            process (HighLevelProcess): the process to put into the queue.
        """
        self.queue_ready.append(process)


class HighLevelProcessManagerSRTF(HighLevelProcessManager):
    def __init__(self, processes) -> None:
        super().__init__(processes)

    def start(self):
        if self.queue_ready == []:
            print("No process in ready queue")
            return None

        return None

    def __find_waiting_time__(self):
        pass

    def __find_turn_around_time__(self):
        pass

    def __find_average_time__(self):
        pass


class HighLevelProcessManagerRR(HighLevelProcessManager):
    def __init__(self, processes) -> None:
        super().__init__(processes)

