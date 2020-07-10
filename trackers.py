"""1 tracker set = all 5 points with correct color"""

class tracker():
    def __init__(self, x_base, y_base, x_sting, y_sting, x_petiole, y_petiole, x_right_ant, y_right_ant, x_left_ant, y_left_ant):
        self.x_base = x_base
        self.y_base = -y_base
        self.x_sting = x_sting
        self.y_sting = -y_sting
        self.x_petiole = x_petiole
        self.y_petiole = -y_petiole
        self.x_right_ant = x_right_ant
        self.y_right_ant = -y_right_ant
        self.x_left_ant = x_left_ant
        self.y_left_ant = -y_left_ant
