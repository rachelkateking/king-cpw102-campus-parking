# use a named constant
# by using 2.0 as its value, it is automatically stored as a float
# because we defined it at the top level, it is available to any function
# in our program
COST_PER_HOUR = 2.0

def calculate_estimated_parking_cost(hours):
    estimated_cost = hours * COST_PER_HOUR
    return estimated_cost

# define the main logic of my program
def main():
    # (input)
    # create a variable in which I will store user-entered parked hours
    # a variable is a named space in memory
    parked_hours = float(input("How many hours will you be / have you parked? "))

    # call our function (processing)
    cost = calculate_estimated_parking_cost(parked_hours)

    # (output)
    print(cost)

# call my main function and execute the logic of the program
main()