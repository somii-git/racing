
total_race_time= input ("What is the total race time in seconds? : ")
num_pit_stops= input ("How many pit stops were made? : ")
avg_pit_stop_duration= input ("What is the average pit stop duration (in seconds)? : ")
#
total_pit_stop_time = int(num_pit_stops) * int(avg_pit_stop_duration)
percentage_pit_time = int(total_pit_stop_time) / int(total_race_time)   * 100
percentage_pit_time = round(percentage_pit_time, 2)
print("Total pit stop time in seconds:", total_pit_stop_time)
print("Percentage of race time spent in pits:", percentage_pit_time, "%")
if percentage_pit_time > 5:
    print("You need a new pit crew!")
