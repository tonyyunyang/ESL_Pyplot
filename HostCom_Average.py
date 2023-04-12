file_path = 'HostCom/receive_time_difference.txt'  # Replace with the actual file path
with open(file_path, 'r') as f:
    lines = f.readlines()
    data = [float(line.strip()) for line in lines]

# Calculate the average of data
average = sum(data) / len(data)

# Print the average
print(f'The average of the data in {file_path} is: {average}')

file_path = 'HostCom/send_message_count.txt'  # Replace with the actual file path
with open(file_path, 'r') as f:
    lines = f.readlines()
    data = [float(line.strip()) for line in lines]

# Calculate the average of data
average = sum(data) / len(data)

# Print the average
print(f'The average of the data in {file_path} is: {average}')

file_path = 'HostCom/send_time_difference.txt'  # Replace with the actual file path
with open(file_path, 'r') as f:
    lines = f.readlines()
    data = [float(line.strip()) for line in lines]

# Calculate the average of data
average = sum(data) / len(data)

# Print the average
print(f'The average of the data in {file_path} is: {average}')