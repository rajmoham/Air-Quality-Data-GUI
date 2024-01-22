def calculate_average_aqi(loc1_readings, loc2_readings):
    """Calculate the average Air Quality Index (AQI).

    Args:
        readings (list): List of tuples representing pairs of readings.

    Returns:
        float: The average AQI difference to three decimal places.
    """

    loc1_filtered = []
    for row in loc1_readings:
        if not isinstance(row, str):
            loc1_filtered.append(row)

    loc2_filtered = []
    for row in loc2_readings:
        if not isinstance(row, str):
            loc2_filtered.append(row)

    loc1_mean = sum(loc1_filtered) / len(loc1_filtered)
    loc2_mean = sum(loc2_filtered) / len(loc2_filtered)

    return max(loc1_mean, loc2_mean) - min(loc1_mean, loc2_mean)