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

        current_time = 0
        remaining_burst_time = [0] * self.processes_amount

        for process in self.queue_ready:
            remaining_burst_time = process.burst_time
        
        """ The while loop keeps flowing untill all the processes are completed """
        while(1):
            processes_completed = True

            for i in range(self.processes_amount):

                """ Verification if there's any remaining time to the current process """
                if(remaining_burst_time[i] > 0):
                    processes_completed = False

                    if(remaining_burst_time[i] > quantum):
                        current_time += quantum

                        """ The remaining time decreases acordding to quantum time untill it's over """
                        remaining_burst_time[i] -= quantum
                    else:
                        current_time += remaining_burst_time[i]

                        self.waiting_time[i] = current_time + self.queue_ready[i].burst_time

                        remaining_burst_time[i] = 0

            if processes_completed:
                break

    def __find_turn_around_time__(self):
        """ Function calculates the processes' turn around time """

        for i in range(self.processes_amount):
            self.turn_around_time[i] = self.queue_ready[i].burst_time + self.wainting_time[i]

        # Trying to rewrite the for loop above, but I ain't sure if it is correct logically...
        #for process in self.queue_ready:
        #    self.turn_around_time = process.burst_time + self.wainting_time

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