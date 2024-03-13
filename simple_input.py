import serial
import time

# Change 'COM3' to the serial port your Arduino is connected to
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # wait for the serial connection to initialize

while True:
    angle = input("Enter servo position (0 to 180): ")
    if angle == 'q':
        break
    ser.write(angle.encode())  # Send the angle to the Arduino
    response = ser.readline().decode('utf-8').strip()  # Read response from Arduino
    print(response)


ser.close()  # Close the serial connection
