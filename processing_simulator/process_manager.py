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
        pass

    def __find_turn_around_time__(self):

        for i in range(self.processes_amount):

            self.turn_around_time[i] = self.queue_ready[i].burst_time + self.wainting_time[i]

    def __find_average_time__(self):
        waiting_total_time = 0
        ramaining_total_time = 0

        self.__find_waiting_time__(self, self.queue_ready[0].quantum_time)
        self.__find_turn_around_time__(self)

        for i in range(self.processes_amount):
            waiting_total_time += self.wainting_time[i]
            ramaining_total_time += self.turn_around_time[i]

        print("\nAverage waiting time = %.5f "%(waiting_total_time / self.processes_amount) )
        print("Average turn around time = %.5f "% (ramaining_total_time / self.processes_amount))