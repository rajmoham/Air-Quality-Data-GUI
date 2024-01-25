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

    return max(loc1_mean, loc2_mean) - min(loc1_mean, loc2_mean)