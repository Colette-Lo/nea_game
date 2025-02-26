# # import all classes/methods
# # from the tkinter module
# import time
#
# # Global variables
# active = False
# period_duration = None
# start_time = 0
# total_periods = None
# efficiency = 0.3
# total_time = 60
# total_collected = 0.0
#
# # Subroutines
# def click_start():
#     if not active:
#         # record start time
#         start_time = int(time.time())
#         return start_time
#
#
# def progress(amount):
#     current = int(time.time())
#     if (current - start_time) >= total_time:
#         return(total_collected + amount)
#     # for i in range(total_collected):
#     #     while (time.time()-period_start) >= self.period_duration:
#     #         self.period_output *= (1 - self.efficiency)
#     #         # adding what has been collected to total output of one op
#     #         total_collected += self.period_output
#     #         # start time for the next period
#     #         period_start = time.time()
#     # return total_collected
#
# def click_collect():
#     pass
#
#
# # Main
# click_start()
# new_output = progress(50)
# print(new_output)
