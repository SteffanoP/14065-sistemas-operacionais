from process import HighLevelProcess

class HighLevelProcessManager():
    def __init__(self, processes: list[HighLevelProcess]) -> None:
        self.queue_ready = processes
        self.processes_amount = len(processes)
        self.wainting_time = [0] * self.processes_amount
        self.turn_around_time = [0] * self.processes_amount

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

    def start(self):
        if self.queue_ready == []:
            print("No process in ready queue")
            return None

    def __find_waiting_time__(self, quantum):
        """ Function calculates the processes' waiting time """


    def __find_turn_around_time__(self):
        """ Function calculates the processes' turn around time """

        for i in range(self.processes_amount):
            self.turn_around_time[i] = self.queue_ready[i].burst_time + self.wainting_time[i]

    def __find_average_time__(self):
        """ Function calculates the processes' average time """
        
        waiting_total_time = 0
        ramaining_total_time = 0

        """ Caliing the function to calculate the waiting time """
        self.__find_waiting_time__(self, self.queue_ready[0].quantum_time)

        """ Caliing the function to calculate the turn around time """
        self.__find_turn_around_time__(self)

        for wt_time in self.wainting_time:
            waiting_total_time += wt_time

        for rm_time in self.turn_around_time:
            ramaining_total_time += rm_time

        """ Printing the average time """
        print("\nAverage waiting time = %.5f "%(waiting_total_time / self.processes_amount))
        print("Average turn around time = %.5f "% (ramaining_total_time / self.processes_amount))