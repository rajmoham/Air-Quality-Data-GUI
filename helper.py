def reorder_arguments(function):
    """Decorator to reorder arguments with smallest first.

    Args:
        function (callable): The function to be decorated.

    Returns:
        callable: Decorated function with reordered arguments.
    """

    def wrapper(arg1, arg2):
        big_val = max(arg1, arg2)
        small_val = min(arg1, arg2)

        def func(arg1, arg2):
            return function(small_val, big_val)

        return func(arg1, arg2)

    return wrapper


@reorder_arguments
def calculate_difference(data1, data2):
    """Calculate positive difference between two data points."""

    return data2 - data1


def average(nums):
    """Calculate the average from a list of numbers."""

    if (len(nums) == 0):
        return 0
    avg = sum(nums) / len(nums)
    return avg


def calculate_average_aqi(loc1_readings, loc2_readings):
    """Calculate the average Air Quality Index (AQI).

    Args:
        loc1_readings (list): readings from first location.
        loc2_readings (list): Readings from second location.
    Returns:
        float: The average AQI difference to three decimal places.
    """

    loc1_filtered = list(
        filter(lambda row: not isinstance(row, str), loc1_readings))

    loc2_filtered = list(
        filter(lambda row: not isinstance(row, str), loc2_readings))

    loc1_mean = average(loc1_filtered)
    loc2_mean = average(loc2_filtered)

    return calculate_difference(loc1_mean, loc2_mean)


def population_sd(data):
    """Calculate the population standard deviation for a dataset."""

    if len(data) == 0:
        return 0

    avg = average(data)
    data_sqr = map(lambda num: num**2, data)

    # Following is the formula for calculating SD
    s_xx = sum(data_sqr) - (avg**2) * len(data)
    variance = s_xx / len(data)
    sd = variance**(1 / 2)
    return sd


def separate_data(data):
    """Separate data by location keeping timeline information for both."""

    data1 = []
    data2 = []
    for _, row in enumerate(data):
        if isinstance(row[2], float):
            data1.append(row[0:3])
        if isinstance(row[3], float):
            data2.append([row[i] for i in (0, 1, 3)])

    return data1, data2

def get_three_point_window_data(data, start_row=0):
    """Returns only the readings in a three-point window"""
    readings = [data[start_row][2], 
                data[start_row + 1][2],
                data[start_row + 2][2]]

    return readings


def highest_three_point_sd(data):
    """Returns the three rows with the highest standard deviation

    Args:
        data (List): Dataset of readings for a location

    Returns:
        List: Contains list of length 3 of subset of 'data' with
            highest population standard deviation.
        None: if data does not have at least 3 readings
    """

    highest_sd = 0
    row = None

    for start_row in range(len(data) - 2):
        window_data = get_three_point_window_data(data, start_row)
        sd = population_sd(window_data)
        if sd > highest_sd:
            highest_sd = sd
            row = start_row

    if row is not None:
        return data[row:row + 3]

    return None