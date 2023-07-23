import os
from process import Process

class ProcessManager():
    def __init__(self, processes: list[Process]) -> None:
        self.queue_ready = processes
        self.processes_amount = len(processes)
        self.main_memory_size = 1700 ## MB
        self.partitions_size = [100, 500, 200, 300, 600] ## It may be a variable number. processes_amount <= partitions_size_len

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
        print("Nome\tTamanho\tBloco_alocado\tFrag_Interna\tFrag_Externa") ## The professor want us to show these informations in the end
        print(f"{process.name}\t{process.size}\t")
        print("\n")
        [print(f"{pw.name}\t{pw.size}\t") for pw in queue]

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
        internal_fragmentation = [-1] * len(self.partitions_size)
        external_fragmentation = [0] * len(self.partitions_size)

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
                    if process.size[0] <= self.partitions_size[block]:
                        allocated_partition[process.pid[0]] = block
                        """
                            Since the block is available, it's size is reduced by the process' size.
                            If any amount of size remains (>0), then there's an internal fragmentation.
                        """
                        internal_fragmentation[block] = self.partitions_size[block] - process.size[0]
                        break

        print("Nu_Processo Tam_Processo   Bloco_Alocado")
        for process in self.queue_ready:

            ## self.__execute_process__(process, self.queue_ready)
            print(" ", process.pid[0] + 1, "         ", process.size[0],
                            "         ", end = " ")
            
            if allocated_partition[process.pid[0]] != -1:
                print(allocated_partition[process.pid[0]] + 1)
            else:
                print("Not allocated")
                external_fragmentation[process.pid[0]] = process.size[0]

        print("\n")
        print("Nu_Processo  Frag_Externa  Frag_Interna")
        for process, ex_f in zip(self.queue_ready, external_fragmentation):

            print(" ", process.pid[0] + 1, "         ", ex_f, "MB",
                            "         ", end = " ")

            if internal_fragmentation[process.pid[0]] > 0:
                print(internal_fragmentation[process.pid[0]], "MB")
            else:
                print(" ")


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