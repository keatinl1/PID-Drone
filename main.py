import logging
import time 
import csv
import cflib.crtp

from cflib.utils import uri_helper
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

from controller import PID

logging.basicConfig(level=logging.ERROR)

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
DEFAULT_HEIGHT = 0.5


def log_pos_callback(timestamp, data, logconf):
    global Z
    Z = data['range.zrange'] / 1000 #  z ranger is in mm for some reason


def main(scf):

    error = 0
    prev_error = 0
    integral_error = 0

    Z_list = []

    with MotionCommander(scf, default_height=0.1) as mc:
        
        endtime = time.time() + 10

        while time.time() < endtime:

            error = 0.3 - Z

            print(f"Error: {error}m")

            controller = PID(error, integral_error, prev_error)
            velocity = controller.get_velocity()

            print(f"Velocity: {velocity}m/s")

            mc.start_linear_motion(0, 0, velocity)

            prev_error = error
            integral_error += prev_error

            print("-------------")

            Z_list.append(Z)

            time.sleep(0.1)

        mc.stop
    
    return Z_list


if __name__ == '__main__':

    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        logconf = LogConfig(name='Range', period_in_ms=100)
        logconf.add_variable('range.zrange', 'float')

        cf = scf.cf
        cf.log.add_config(logconf)
        logconf.data_received_cb.add_callback(log_pos_callback)

        logconf.start()

        output_list = main(scf)

        logconf.stop()

        with open('file.csv', 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(output_list)
