import math
import array

sample_rate = 1000  # Sample rate in Hz
duration = 1        # Duration in seconds
frequency = 2       # Frequency of the sine wave in Hz

num_samples = int(sample_rate * duration)

buffer_list = []
for i in range(num_samples):
    t = i / sample_rate  # Time in seconds
    sample = 0.5 * (1 + math.sin(2 * math.pi * frequency * t))  # Generate a sine wave between 0 and 1
    buffer_list.append(sample)

print ("Generated audio buffer with {} samples.".format(num_samples))
print ("First 10 samples: ", buffer_list[:10])  

# Convert the list to an array for more efficient storage
buffer_array = array.array('f', buffer_list)
print("Buffer (array) has {} samples".format(len(buffer_array)))
print("First 10 samples (array): ", buffer_array[:10])  # Display first 10 samples of the array

buffer_view = memoryview(buffer_array)
print("Buffer view has {} samples".format(len(buffer_view)))
print("First 10 samples (view): ", buffer_view[:10].tolist())  # Display first 10 samples of the memory view

scaled_buffer_array = array.array('f', (sample * 2.0 for sample in buffer_array))  # Scale the buffer by a factor of 2
print("Scaled buffer (array) has {} samples".format(len(scaled_buffer_array)))
print("First 10 samples (scaled array): ", scaled_buffer_array[:10])  # Display first 10 samples of the scaled array