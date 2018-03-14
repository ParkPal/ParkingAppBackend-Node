from envirophat import light, motion
from time import localtime, strftime
import time

light_file_name = "light_sensor_output.txt"
mag_file_name = "mag_sensor_output.txt"

def get_current_time():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())


def write_to_file(line, file_name):
    f = open(file_name, "a")
    f.write(str(line) + "----")
    f.write(str(get_current_time())+ "\n")
    f.close
    print("Wrote to file " + file_name)


try:
    while True:
        light_v = light.light()
        mag_v = motion.magnetometer()
        write_to_file(light_v, light_file_name)
        write_to_file(mag_v, mag_file_name)
        time.sleep(1)
#        print(light_v)
#        print(mag_v)
except KeyboardInterrupt:
    pass
