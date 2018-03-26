from collections import namedtuple

from RPi import GPIO

# STAPPENPLAN: ZIE SYLLABUS!

MPU6050_DEFAULT_ADDRESS = 0x68

# useful registers
MPU6050_REG_GYRO_CONFIG = 0x1B  # [ XG_ST | YG_ST | ZG_ST | FS_SEL[1:0] | [2:0] ]
MPU6050_REG_ACCEL_CONFIG = 0x1C  # [ XA_ST | YA_ST | ZA_ST | AFS_SEL[1:0] | [2:0] ]
MPU6050_REG_INT_ENABLE = 0x38
MPU6050_REG_ACCEL_OUT = 0x3B  # 3x 2 bytes little endian
MPU6050_REG_TEMP_OUT = 0x41  # 2 bytes little endian
MPU6050_REG_GYRO_OUT = 0x43  # 3x 2 bytes little endian
MPU6050_REG_MOTION_DETECT_STATUS = 0x61
MPU6050_REG_PWR_MGMT_1 = 0x6B  # [ DEVICE_RESET | SLEEP | CYCLE | - | TEMP_DIS | CLKSEL[2:0] ]
MPU6050_REG_PWR_MGMT_2 = 0x6C
MPU6050_REG_WHO_AM_I = 0x75  # [ - | I2C_ADDR[6:1] | - ]

# range setting
MPU6050_GYRO_RANGE_250 = MPU6050_ACCEL_RANGE_2G = 0
MPU6050_GYRO_RANGE_500 = MPU6050_ACCEL_RANGE_4G = 1
MPU6050_GYRO_RANGE_1000 = MPU6050_ACCEL_RANGE_8G = 2
MPU6050_GYRO_RANGE_2000 = MPU6050_ACCEL_RANGE_16G = 3

# scale values
MPU6050_GYRO_MAX_SCALE = 131
MPU6050_ACCEL_MAX_SCALE = 16384
MPU6050_TEMP_SCALE = 340
MPU6050_TEMP_OFFSET = 36.53

Measurement = namedtuple('MPU6050Measurement', 'ax ay az t gx gy gz')


def check_connection(sensor_address):
    ...


class MPU6050:
    def setup(self):
        ...

    def get_raw_data(self):
        """
        Read raw accelerometer data
        :return: list[int] with 14 register values
        """
        ...

    @staticmethod
    def restore_2complement(msb, lsb):
        """
        Restore 16-bit 2's complement value from 2 measurement register values
        :param msb: most significant byte
        :param lsb: least significant byte
        :return: 16-bit signed integer
        """
        ...

    def get_measurements(self):
        """
        Get 3-axis acceleration, temperature, and 3-axis gyroscope measurement
        :return: Measurement(ax, ay, az, t, gx, gy, gz)
        """
        ...


def main():
    GPIO.setmode(GPIO.BCM)
    try:
        # Hier kan je jouw functies/klassen oproepen om ze te testen
        ...
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.setwarnings(False)  # get rid of warning when no GPIO pins set up
        GPIO.cleanup()


if __name__ == '__main__':
    main()
