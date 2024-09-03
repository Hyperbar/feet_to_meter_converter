def make_conversion(feet, inches):
    """
    Convert measurements from feet and inches to meters.

    Args:
    feet (float): The length in feet.
    inches (float): The length in inches.

    Returns:
    float: The equivalent length in meters.
    """
    # Convert feet to meters (1 foot = 0.3048 meters)
    # Convert inches to meters (1 inch = 0.0254 meters)
    meter_conversion = feet * 0.3048 + inches * 0.0254

    # Return the total length in meters
    return meter_conversion