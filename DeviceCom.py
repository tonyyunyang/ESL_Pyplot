import matplotlib.pyplot as plt

# Read data from the first .txt file
file1 = 'DeviceCom/device_ack_count.txt'
with open(file1, 'r') as f1:
    lines1 = f1.readlines()
    data1 = [float(line.strip()) for line in lines1]

# Read data from the second .txt file
file2 = 'DeviceCom/device_drop_count.txt'
with open(file2, 'r') as f2:
    lines2 = f2.readlines()
    data2 = [float(line.strip()) for line in lines2]
    
# Read data from the second .txt file
file3 = 'HostCom/send_message_count.txt'
with open(file3, 'r') as f3:
    lines3 = f3.readlines()
    data3 = [float(line.strip()) for line in lines3]

# Get the number of lines as x-axis
x = range(1, len(lines1) + 1)

# Plot data from the first .txt file
plt.plot(x, data1, label='Messages received and acknowledged by the device')

# Plot data from the second .txt file
plt.plot(x, data2, label='Messages dropped by the device')

# Plot data from the second .txt file
plt.plot(x, data3, label='Messages sent by the host')

# Add labels and legend
plt.xlabel('Time (Host receives a message))')
plt.ylabel('Number of Messages')
plt.legend()

# Show the plot
plt.show()