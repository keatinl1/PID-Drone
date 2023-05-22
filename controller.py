'''PID class'''

class PID:
    def __init__(self, error, integral_error, prev_error):

        self.error = error
        self.integral_error = integral_error
        self.prev_error = prev_error

        self.kp = 1.1
        self.ki = 0.001
        self.kd = 0.275

    def get_velocity(self):
        return self.kp*self.error + self.ki*self.integral_error + self.kd*(self.error - self.prev_error)
    