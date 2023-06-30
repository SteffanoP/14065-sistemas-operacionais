from process import HighLevelProcess
from queue import Queue

class HighLevelProcessManager():
    def __init__(self) -> None:
        self.queue_ready = Queue(maxsize=10)

    def put_into_queue_ready(self, process: HighLevelProcess) -> None:
        """Put a process into the ready queue.

        Args:
            process (HighLevelProcess): the process to put into the queue.
        """
        self.queue_ready.put(process)

    
class HighLevelProcessManagerSRTF(HighLevelProcessManager):
    def __init__(self) -> None:
        super().__init__()

class HighLevelProcessManagerRR(HighLevelProcessManager):
    def __init__(self) -> None:
        super().__init__()