import os
import copy
import random
from time import sleep

from process import Process

class MemoryManager():
    def __init__(self, processes: list[Process]) -> None:
        self.queue_ready = processes
        self.processes_amount = len(processes)
        self.main_memory_size = 1700 ## MB
        self.partitions_size = [100, 500, 200, 300, 600] ## It may be a variable number. processes_amount <= partitions_size_len
        self.partitions = [(partition_size, None) for partition_size in self.partitions_size]
        self.swap = []

    def put_into_queue_ready(self, process: Process) -> None:
        """Put a process into the ready queue.

        Args:
            process (Process): the process to put into the queue.
        """
        self.queue_ready.append(process)

    """ Continuing the last part about showing the allocated block and is there's internal fragmentation """
    @staticmethod
    def __execute_process__(process: Process, queue: list[Process]):
        os.system('clear')
        print("Alocação da Memória")
        print("Nome\tTamanho\tBloco_alocado\tFrag_Interna") 
        print(f"{process.name}\t{process.size}\t")
        print("\n")
        [print(f"{pw.name}\t{pw.size}\t") for pw in queue]

""" Only SUGGESTIONS of algortihms to implement """

class MemoryFirstFitAlgorithm(MemoryManager):
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
        internal_fragmentation = [-1] * len(self.partitions_size)

        """
            No block is allocated in the beginning, so the algorithm searches for the first 
            space available that fits the process
        """
        for process in self.queue_ready:
            for block in range(len(self.partitions_size)):
                """
                    Verification if the block fits the process, but first checks if 
                    any process has passed leaving an internal fragmentation
                """
                if internal_fragmentation[block] < 0:
                    if process.size <= self.partitions_size[block]:
                        allocated_partition[process.pid] = block
                        """
                            Since the block is available, it's size is reduced by the process' size.
                            If any amount of size remains (>0), then there's an internal fragmentation.
                        """
                        internal_fragmentation[block] = self.partitions_size[block] - process.size
                        break

        print("Nu_Processo Tam_Processo   Bloco_Alocado")
        for process in self.queue_ready:

            print(" ", process.pid + 1, "         ", process.size,
                            "         ", end = " ")
            
            if allocated_partition[process.pid] != -1:
                print(allocated_partition[process.pid] + 1)
            else:
                print("Not allocated")

        print("\n")
        print("Nu_Processo     Frag_Interna")
        for process in self.queue_ready:

            print(" ", process.pid + 1,
                            "             ", end = " ")

            if internal_fragmentation[process.pid] > 0:
                print(internal_fragmentation[process.pid], "MB")
            else:
                print(" ")


class MemoryBestFitAlgorithm(MemoryManager):
    def __init__(self, processes) -> None:
        super().__init__(processes)

    def start(self):
        if self.queue_ready == []:
            print("No process in ready queue")
            return None

        for process in self.queue_ready:

            local_best = copy.deepcopy(process.size)
            can_allocate = False
            for partition in self.partitions:
                if can_allocate is True:
                    if partition[0] <= local_best and process.size <= partition[0]:
                        local_best = partition[0]
                    continue

                if partition[1] is None and local_best <= partition[0]:
                    local_best = partition[0]
                    can_allocate = True

            try:
                index = self.partitions.index((local_best, None))
            except ValueError as error:
                if can_allocate is True:
                    raise error

            while can_allocate is False:
                partition = random.choice(self.partitions)
                if process.size <= partition[0]:
                    self.swap.append(partition)
                    local_best = partition[0]
                    index = self.partitions.index(partition)
                    can_allocate = True

            self.partitions[index] = ((local_best, process.pid))
            # print(self.partitions)
            self.print_allocation()
            sleep(2)

        return None

    def print_allocation(self):
        os.system('clear')
        print("Alocação da Memória")
        print("Nome\tTamanho\tBloco_alocado\tFrag_Interna")
        for partition in self.partitions:
            if partition[1] is None:
                print(f"-\t000\t{partition[0]}\t000")
                continue
            process = self.__get_process__(partition[1])
            print(f"{process.pid}\t{process.size}\t{partition[0]}\t{partition[0] - process.size}")

        print("Swapping")
        print("Nome\tBloco alocado")
        for process in self.swap:
            print(f"{process[1]}\t{process[0]}")

    def __get_process__(self, pid) -> Process:
        return next((p for p in self.queue_ready if p.pid == pid), None)
