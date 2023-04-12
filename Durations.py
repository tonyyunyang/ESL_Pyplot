import matplotlib.pyplot as plt

# Read data from the first .txt file
file1 = 'Durations/safety.txt'
with open(file1, 'r') as f1:
    lines1 = f1.readlines()
    data1 = [float(line.strip()) for line in lines1]

# Read data from the first .txt file
file2 = 'Durations/manual.txt'
with open(file2, 'r') as f2:
    lines2 = f2.readlines()
    data2 = [float(line.strip()) for line in lines2]

# Read data from the first .txt file
file3 = 'Durations/calibration.txt'
with open(file3, 'r') as f3:
    lines3 = f3.readlines()
    data3 = [float(line.strip()) for line in lines3]

# Read data from the first .txt file
file4 = 'Durations/yaw.txt'
with open(file4, 'r') as f4:
    lines4 = f4.readlines()
    data4 = [float(line.strip()) for line in lines4]

# Read data from the first .txt file
file5 = 'Durations/full.txt'
with open(file5, 'r') as f5:
    lines5 = f5.readlines()
    data5 = [float(line.strip()) for line in lines5]

# Read data from the first .txt file
file6 = 'Durations/raw.txt'
with open(file6, 'r') as f6:
    lines6 = f6.readlines()
    data6 = [float(line.strip()) for line in lines6]

# Read data from the first .txt file
file7 = 'Durations/height.txt'
with open(file7, 'r') as f7:
    lines7 = f7.readlines()
    data7 = [float(line.strip()) for line in lines7]


# Get the number of lines as x-axis
x = range(1, len(lines1) + 1)

# Plot data from the first .txt file
plt.plot(x, data1, label='Loop duration of Safety Mode') 

# Plot data from the first .txt file
plt.plot(x, data2, label='Loop duration of Manual Mode') 

# Plot data from the first .txt file
plt.plot(x, data3, label='Loop duration of Calibration Mode') 

# Plot data from the first .txt file
plt.plot(x, data4, label='Loop duration of Yaw Control Mode') 

# Plot data from the first .txt file
plt.plot(x, data5, label='Loop duration of Full Control Mode') 

# Plot data from the first .txt file
plt.plot(x, data6, label='Loop duration of Raw Mode') 

# Plot data from the first .txt file
plt.plot(x, data7, label='Loop duration of Height Control Mode') 

# Add labels and legend
plt.xlabel('Time (one tick on the device)')
plt.ylabel('Time (ms)')
plt.legend()

# Show the plot
plt.show()