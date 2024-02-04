def reorder_arguments(function):
    """Decorator to reorder arguments with smallest first.

    Args:
        function (callable): The function to be decorated.

    Returns:
        callable: Decorated function with reordered arguments.
    """
    def wrapper(arg1, arg2):
        func = lambda arg1, arg2 : function(arg1, arg2) if (arg1 < arg2) \
              else function(arg2, arg1)
        return func(arg1, arg2)

    return wrapper

@reorder_arguments
def calculate_difference(data1, data2):
    """Calculate the difference between two data points.

    Args:
        data1: The first data point.
        data2: The second data point.

    Returns:
        float: The positive difference between the two data points.
    """
    return data2 - data1

def average(nums):
    """Calculates the average of a list of numbers"""
    if (len(nums) == 0):
        return 0
    avg = sum(nums) / len(nums)
    return avg

def calculate_average_aqi(loc1_readings, loc2_readings):
    """Calculate the average Air Quality Index (AQI).

    Args:
        readings (list): List of tuples representing pairs of readings.

    Returns:
        float: The average AQI difference to three decimal places.
    """

    loc1_filtered = list(filter(lambda row: 
                    not isinstance(row, str), loc1_readings))

    loc2_filtered = list(filter(lambda row: 
                    not isinstance(row, str), loc2_readings))

    loc1_mean = average(loc1_filtered)
    loc2_mean = average(loc2_filtered)

    return calculate_difference(loc1_mean, loc2_mean)

def population_sd(data):
    """Calculates the population standard deviation for a set of data"""
    
    if len(data) == 0:
        return 0

    avg = average(data)
    data_sqr = map(lambda num: num**2, data)

    # Following is the formula for calculating SD
    s_xx = sum(data_sqr) - (avg**2)*len(data)
    variance = s_xx / len(data)
    sd = variance**(1/2)
    return sd

def separate_data(data):
    """
    Separates the readings but keeps timeline data for each reading
    while also filtering invalid data
    """
    data1 = []
    data2 = []
    for _, row in enumerate(data):
        if isinstance(row[2], float):
            data1.append(row[0:3])
        if isinstance(row[3], float):
            data2.append([row[i] for i in (0, 1, 3)])

    return data1, data2
