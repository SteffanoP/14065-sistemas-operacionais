import time
from process import HighLevelProcess
import copy

class HighLevelProcessManager():
    def __init__(self, processes: list[HighLevelProcess]) -> None:
        self.queue_ready = processes
        self.processes_amount = len(processes)
        self.waiting_time = [0] * self.processes_amount
        self.turn_around_time = [0] * self.processes_amount
        self.current_time = 0

    def put_into_queue_ready(self, process: HighLevelProcess) -> None:
        """Put a process into the ready queue.

        Args:
            process (HighLevelProcess): the process to put into the queue.
        """
        self.queue_ready.append(process)


class HighLevelProcessManagerSRTF(HighLevelProcessManager):
    def __init__(self, processes) -> None:
        super().__init__(processes)
        self.current_process_executing = None


    def start(self):
        if self.queue_ready == []:
            print("No process in ready queue")
            return None

        self.__schedule_new_process__()
        self.__execute__()

        return None

    def __execute__(self):
        while self.current_process_executing is not None:
            # Execute process
            print(f"Executing Process {self.current_process_executing.name}")
            self.current_process_executing.execute()
            self.current_time += 1

            cond1 = self.current_process_executing.get_remaining_burst_time() == 0
            cond2 = self.queue_ready == []
            if cond1 and cond2:
                self.current_process_executing = None
                break

            if cond1:
                self.__schedule_new_process__()

            if self.queue_ready != [] and self.current_process_executing is not None:
                # Check for if any new process on ready queue has better burst time
                bt_current_p = self.current_process_executing.get_remaining_burst_time()
                p_minimal_bt_on_q = self.__get_process_minimal_burst_time__()
                if p_minimal_bt_on_q.burst_time < bt_current_p:
                    self.queue_ready.append(self.current_process_executing)
                    self.__schedule_new_process__()
            time.sleep(1)

        self.__end__()

    def __end__(self):
        print("Program has finished!")

    def __get_process_minimal_burst_time__(self) -> HighLevelProcess:
        return min(self.queue_ready, key=lambda p: p.get_remaining_burst_time())

    def __schedule_new_process__(self):
        self.current_process_executing = self.__get_process_minimal_burst_time__()
        self.queue_ready.remove(self.current_process_executing)

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
        self.__find_average_time__()

    def __find_waiting_time__(self, quantum):
        """ Function calculates the processes' waiting time """

        current_time = 0
        remaining_burst_time = copy.deepcopy(self.queue_ready)
        
        """ The while loop keeps flowing untill all the processes are completed """
        while(1):
            processes_completed = True
           
            for process, i in zip(remaining_burst_time, range(self.processes_amount)):
                
                """ Verification if there's any remaining time to the current process """
                if(process.burst_time > 0):
                    processes_completed = False

                    if(process.burst_time > quantum):
                        current_time += quantum
                       
                        """ The remaining time decreases acordding to quantum time untill it's over """
                        process.burst_time -= quantum
                    else:
                        current_time += process.burst_time

                        self.waiting_time[i] = current_time + self.queue_ready[i].burst_time

                        process.burst_time = 0

            if processes_completed:
                break

    def __find_turn_around_time__(self):
        """ Function calculates the processes' turn around time """

        for i in range(self.processes_amount):
            self.turn_around_time[i] = self.queue_ready[i].burst_time + self.waiting_time[i]

        # Trying to rewrite the for loop above, but I ain't sure if it is correct logically...
        #for process in self.queue_ready:
        #    self.turn_around_time = process.burst_time + self.wainting_time

    def __find_average_time__(self):
        """ Function calculates the processes' average time """

        waiting_total_time = 0
        remaining_total_time = 0

        """ Caliing the function to calculate the waiting time """
        self.__find_waiting_time__(self.queue_ready[0].quantum_time)

        """ Caliing the function to calculate the turn around time """
        self.__find_turn_around_time__()

        for wt_time in self.waiting_time:
            waiting_total_time += wt_time

        for rm_time in self.turn_around_time:
            remaining_total_time += rm_time

        """ Printing the average time """
        print("\nAverage waiting time = %.5f "%(waiting_total_time / self.processes_amount))
        print("Average turn around time = %.5f "% (remaining_total_time / self.processes_amount))