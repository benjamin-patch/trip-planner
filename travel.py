# print welcome message
def trip_planner_welcome(name):
    print("Welcome to Trip Planner v1.0", name)

trip_planner_welcome("Ben")

# estimated time
def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time

estimate = estimated_time_rounded(3.5)
