import os
from process import Process

class ProcessManager():
    def __init__(self, processes: list[Process]) -> None:
        self.queue_ready = processes
        self.processes_amount = len(processes)
        self.main_memory_size = 12 ## MB
        self.partitions_size = list[int] ## It may be a variable number. processes_amount <= partitions_size_len

    def put_into_queue_ready(self, process: Process) -> None:
        """Put a process into the ready queue.

        Args:
            process (Process): the process to put into the queue.
        """
        self.queue_ready.append(process)

    def split_partitions(self) -> None:
        self.partitions_size = [2, 5, 4, 1] ## Sizes in MB

    ## Continuing the last part about showing the allocated block and is there's internal and/or external fragmentation
    @staticmethod
    def __execute_process__(process: Process, queue: list[Process]):
        os.system('clear')
        print("Alocação da Memória")
        print("Nome\tTamanho\tFE_FI\tBloco_alocado")
        print(f"{process.name}\t{process.size}\t")
        print("\n")
        [print(f"{pw.name}\t{pw.size}\t") for pw in queue]
        process.execute()

## Only SUGGESTIONS of algortihms to implement

class ProcessFirstFitAlgorithm(ProcessManager):
    pass


class ProcessBestFitAlgorithm(ProcessManager):
    pass