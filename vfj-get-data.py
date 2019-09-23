import sys
import minimalmodbus
from time import sleep

if len(sys.argv) > 1:
    serial_port = sys.argv[1]
else:
    serial_port = 'COM3'

wind_speed_sensor = minimalmodbus.Instrument(serial_port, 1) # Serial port, slave address (dec)
wind_speed_sensor.serial.baudrate = 9600
wind_speed_sensor.serial.timeout = 0.5

wind_direction_sensor = minimalmodbus.Instrument(serial_port, 2) # Serial port, slave address (dec)
wind_direction_sensor.serial.baudrate = 9600
wind_direction_sensor.serial.timeout = 0.5


while True:
    try:
        wind_speed = str(wind_speed_sensor.read_register(0, 2)) + ' m/s'
    except OSError:
        wind_speed = 'Failed to read from instrument'

    try:
        wind_direction = str(wind_direction_sensor.read_register(0, 2)) + ' degrees'
    except OSError:
        wind_direction = 'Failed to read from instrument'

    html_code = """\
<html>
<body>
<h1>Vassfjellet weather sensors</h1>
<p>
Wind speed: {wind_speed_s}
<br>
Wind direction: {wind_direction_s}
</p>
</body>
</html>\
""".format(wind_speed_s = wind_speed, wind_direction_s = wind_direction)

    for attempt in range(5):
        try:
            f = open('vfj-weather-sensors.html','w+')
            f.write(html_code)
            f.close()
        except OSError:
            sleep(0.5)
            continue
        else:
            break


    sleep(1)