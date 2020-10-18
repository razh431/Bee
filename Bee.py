"""creates the bee class-- body parts labeled with left right positions"""

class Bee():
    def __init__(self, x_base, y_base, x_sting, y_sting, x_petiole, y_petiole, x_right_ant, y_right_ant, x_left_ant, y_left_ant):
        self.x_base = x_base
        self.y_base = -y_base #negative because of coordinate systems
        self.x_sting = x_sting
        self.y_sting = -y_sting
        self.x_petiole = x_petiole
        self.y_petiole = -y_petiole
        self.x_right_ant = x_right_ant
        self.y_right_ant = -y_right_ant
        self.x_left_ant = x_left_ant
        self.y_left_ant = -y_left_ant

    def cba(self):
        '''returns 2points on cba'''

        y = np.array([self.y_base, self.y_sting, self.y_petiole])
        x = np.array([self.x_base, self.x_sting, self.x_petiole])

        #https://jcornford.github.io/2017-01-02-lines-of-best-fit/
        m, b  = np.polyfit(x,y,deg=1)
        print(str(m) + "x + " + str(b))

        #just 2 points I chose, where x is x_sting and x_base-- fit to line
        y_b = m*self.x_base + b
        y_s = m*self.x_sting + b


        return y_b, y_s
