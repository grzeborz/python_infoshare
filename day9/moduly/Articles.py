

bike_types = {"cross":"Cross bicycle", "road":"Road bicycle", "MTB":"Off road"}

class Bike(object):
    def __init__(self, color, type, front_wheel, back_wheel, frame, handlebar = "fitness", seat = "classic, stock, seat"):
        """

        :param color:
        :param type:
        :param front_wheel:
        :param back_wheel:
        :param frame:
        """
        self.color = color
        self.type = type
        self.handlebar = handlebar
        self.seat = seat
        self.front_wheel = front_wheel
        self.back_wheel = back_wheel
        self.frame = frame

class Wheel(object):
    """Producing bicycle wheels"""
    def __init__(self, wheel_size, wheel_material, wheel_color, spokes):
        self.wheel_size = wheel_size
        self.material = wheel_material
        self.wheel_color = wheel_color
        self.spokes_num = spokes

class Frame(object):
    """
    Producing a bicycle frame
    """
    def __init__(self, size, color, geometry):
        self.size = size
        self.color = color
        self.geometry = geometry