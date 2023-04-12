import matplotlib.pyplot as plt

# Read data from the first .txt file
file1 = 'HostCom/receive_period.txt'
with open(file1, 'r') as f1:
    lines1 = f1.readlines()
    data1 = [float(line.strip()) for line in lines1]

# Read data from the second .txt file
file2 = 'HostCom/send_period.txt'
with open(file2, 'r') as f2:
    lines2 = f2.readlines()
    data2 = [float(line.strip()) for line in lines2]

# Get the number of lines as x-axis
x = range(1, len(lines1) + 1)

# Plot data from the first .txt file
plt.plot(x, data1, label='Time duration between two received messages')

# Plot data from the second .txt file
plt.plot(x, data2, label='Time duration between performing two send operations')

# Add labels and legend
plt.xlabel('Number of Operations')
plt.ylabel('Time (ms)')
plt.legend()

# Show the plot
plt.show()