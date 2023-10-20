import random
import time
import pandas as pd
import timeit

class ScenarioBuilder:
    def __init__(self, times_to_run_method, scenario_method):
        # method information
        self.times_to_run_method = times_to_run_method
        self.scenario_method = scenario_method
        self.method_name = scenario_method.__name__

        # store the data
        self.list_results = []

        # timekeeping
        self.start_time = time.time()
        self.end_time = None


    def run_one_method(self):
        """Runs the stored scenario method once"""
        return self.scenario_method()


    def collect_scenario_data(self):
        """Runs the stored scenario method multiple times"""
        for each_scenario in range(self.times_to_run_method):
            scenario_result = self.run_one_method()

            # add each record to a single list
            self.list_results.append(scenario_result)


    def add_commas(self, number):
        return '{:,}'.format(number)


    def print_results_to_terminal_with_PANDAS(self):
        s = pd.Series(self.list_results)
        counts = s.value_counts(sort=False)
        counts = counts.sort_index()    

        total = s.count()
        percents = counts / total
        percents = percents.round(4) * 100

        
        df = pd.DataFrame({'count': counts, 'percent': percents})
        df['count'] = df['count'].apply(self.add_commas)


        print(
            '\n=================================================================='
            '\n=============== RUN MULTIPLE GAMES, RESULTS BELOW ================'
            '\n=================================================================='
            '\nTotal times ran: {0} \n'
            .format(self.times_to_run_method)
        )

        print(df)

        # print how long the code took to run
        #====================================
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time

        print(
            '\n==============EXECUTION TIMES=============='
            '\n    Time:   |   Seconds:   |   Miliseconds  '
            '\n  {tim:>8}  | {sec:^12.2f} | {mil:>11.2f}   '
            '\n                                            '
            .format(tim = time.strftime("%H:%M:%S", time.gmtime(elapsed_time)), 
                    sec = round(elapsed_time, 2), 
                    mil = round(elapsed_time * 1000, 2))) 
