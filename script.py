import math
power_time_factor = 20

Total_time = 99
comp_time = round(Total_time / power_time_factor, 2 )

str_ct = list(str(comp_time))
print("Computing time is:", comp_time)

str_ct.remove(".")
fine_str_ct = ["0", ".", "0"] + str_ct

new = ""

for char in fine_str_ct:
    new = new + char
print(new)

