import os
from process import Process

class ProcessManager():
    def __init__(self, processes: list[Process]) -> None:
        self.queue_ready = processes
        self.processes_amount = len(processes)
        self.main_memory_size = 12 ## MB
        self.partitions_size = [3, 5, 3, 1] ## It may be a variable number. processes_amount <= partitions_size_len
        self.is_fe_fi = str

    def put_into_queue_ready(self, process: Process) -> None:
        """Put a process into the ready queue.

        Args:
            process (Process): the process to put into the queue.
        """
        self.queue_ready.append(process)

    """ Continuing the last part about showing the allocated block and is there's internal and/or external fragmentation """
    @staticmethod
    def __execute_process__(process: Process, queue: list[Process]):
        os.system('clear')
        print("Alocação da Memória")
        print("Nome\tTamanho\tFE_FI\tBloco_alocado")
        print(f"{process.name}\t{process.size}\t")
        print("\n")
        [print(f"{pw.name}\t{pw.size}\t") for pw in queue]
        process.execute()

""" Only SUGGESTIONS of algortihms to implement """

class ProcessFirstFitAlgorithm(ProcessManager):
    def __init__(self, processes) -> None:
        super().__init__(processes)

    def start(self):
        if self.queue_ready == []:
            print("No process in ready queue")
            return None

        self.__first_fit_algorithm__()

        return None
    
    def __first_fit_algorithm__(self):
        """
            Function that selects the first partition possible to receive the ready process
        """
        allocated_partition = [-1] * self.processes_amount
        fragmentation = []
        """
            No block is allocated in the beginning, so the algorithm searches for the first space available that fits the process
        """
        for process in self.queue_ready:
            for block_size in self.partitions_size:

                """
                    Verification if the block fits the process
                """
                if process.size <= block_size:
                    allocated_partition[process.pid] = self.partitions_size.index(block_size)

                    """
                        Since the block is available, it's size is reduced by the process' size.
                        If any amount of size remains (>0), then there's an internal fragmentation.
                    """
                    self.partitions_size[self.partitions_size.index(block_size)] = block_size - process.size

                    break

        for block in self.partitions_size:

            if block > 0:
                fragmentation[self.partitions_size.index(block)] = "I"
               
            else:
                fragmentation[self.partitions_size.index(block)] = " "

        ## TODO: self.__execute_process__(self.queue_ready)

        print(" Process No. Process Size      Block no.")
        for process in self.queue_ready:
            print(" ", process.pid + 1, "         ", process.size,
                            "         ", end = " ")
            
            if allocated_partition[process.pid] != -1:
                print(allocated_partition[process.pid] + 1)
            else:
                print("Não alocado")


class ProcessBestFitAlgorithm(ProcessManager):
    def __init__(self, processes) -> None:
        super().__init__(processes)

    def start(self):
        if self.queue_ready == []:
            print("No process in ready queue")
            return None

        self.__schedule_new_process__()
        self.__execute__()

        return None