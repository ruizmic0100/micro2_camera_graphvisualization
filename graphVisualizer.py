import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
import time
import os

# TODO(MSR): Add clear and concise errors to each step with resolution messages.
# TODO(MSR): Make Graph better or whatever...
# TODO(MSR): Add parsearg to have the user be able to change certain paremeters of the script.
# TODO(MSR): Create an averaging line algorithm to help with 'jumpy' graphs.
# TODO(MSR): Create an executable using pyinstaller.
# TODO(MSR): Create a GUI implementation of this.
# BUG(MSR): Fix it not closing

ser = serial.Serial('COM12', 115200, timeout=2, bytesize=8, stopbits=1, parity=serial.PARITY_NONE, rtscts=0) # open serial port
print(f"Port used: {ser.name}") # Prints the port used to connect

# Holds the data from the camera
sampleCount = list(range(128))
samples = []

""" 
    This is ran every 50ms(interval) so that it displays
    the updates the graph.

    The update rate can be changed by editting the FuncAnimation
    parameter interval to any millisecond value.
"""
def animate(i):
    global samples, sampleCount

    # Grabs the next 128 samples
    while len(samples) != 128:
        s = ser.readline().decode("UTF-8").strip() # reads the buffer and strip newline char.
        if (s != b''): # Only save non-empty buffers.
            samples.append(s)
    samples = list(map(int, samples)) # convert the (str)elements to ints.
    os.system('cls' if os.name == 'nt' else 'clear')
    print(samples)

    plt.cla() # Clear the plot
    plt.plot(sampleCount, samples, 'ro') # Plot red circles
    plt.axis([min(sampleCount),max(sampleCount),min(samples),max(samples)]) # Auto scale the plot
    plt.ylabel('Camera Values')
    plt.xlabel('Samples')
    samples.clear() # clear the data buffer so that new fresh data can come in


ani = FuncAnimation(plt.gcf(), animate, interval=50) # animation function that handles the refreshing of the plot

plt.show()

""" Necessary so that the graph is populated first """
def graphInit():
    global samples, sampleCount
    while len(samples) != 128:
        s = ser.readline().decode("UTF-8").strip()
        if (s != b''):
            samples.append(s)
            if (len(samples) > 129):
                samples.clear()
    samples = list(map(int, samples))

""" Leaving both of these here incase it ever becomes a library or something... """
def main():
    """ Start of script """
    graphInit()
    print(f"Port used: {ser.name}") # Prints the port used to connect
    plt.close()
    ser.close()

if __name__ == "__main__":
    """ Execution from command line """
    main()