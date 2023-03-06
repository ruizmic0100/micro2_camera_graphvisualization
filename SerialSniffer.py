# Simple Serial sniffer program to read all the values comming in from the serial communication.
import serial

ser = serial.Serial('COM12', 115200, timeout=2, bytesize=8, stopbits=1, parity=serial.PARITY_NONE, rtscts=0) # open serial port
print(f"Port used: {ser.name}") # Prints the port used to connect

while 1:
    print(ser.readline())