import logging
import time 

import cflib.crtp
from cflib.utils import uri_helper
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

logging.basicConfig(level=logging.ERROR)

URI = uri_helper.uri_from_env(default='radio://0/80/2M/A7A7A7A7A7')
DEFAULT_HEIGHT = 0.5

prev_error = 0
integral_error = 0

#------------------------------------------------------------------#


def log_pos_callback(timestamp, data, logconf):
    # print('[%d][%s]: %s' % (timestamp, logconf.name, data))

    global Z

    Z = data['range.zrange'] / 1000 #  z ranger is in mm for some reason



def main(scf):

    kp = 2.
    ki = 0.001
    kd = 1.

    global prev_error 
    global integral_error 

    with MotionCommander(scf, default_height=0.1) as mc:
        
        # endtime = time.time() + 10

        # while time.time() < endtime:
        while True:

            error = 0.5 - Z

            print(f"Error: {error}m")

            velocity = kp*error + ki*integral_error + kd*(error - prev_error)

            print(f"Velocity: {velocity}m/s")

            # if velocity < 0:
            #     velocity = 0

            mc.start_linear_motion(0, 0, velocity)

            prev_error = error
            integral_error += prev_error

            print("-------------")

            time.sleep(0.1)



if __name__ == '__main__':

    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        logconf = LogConfig(name='Range', period_in_ms=100)
        logconf.add_variable('range.zrange', 'float')

        cf = scf.cf
        cf.log.add_config(logconf)
        logconf.data_received_cb.add_callback(log_pos_callback)

        logconf.start()
        
        main(scf)
        
        logconf.stop()
