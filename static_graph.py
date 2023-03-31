import matplotlib.pyplot as plt

# Read the data from the text file
with open("result.txt", "r") as file:
    data = [line.strip().split() for line in file.readlines()]

# # Separate the data into durations, video names, and their indices
# durations = [int(item[0]) for item in data]
# video_names = [item[2] for item in data]
# video_indices = range(len(video_names))

# # Create a bar graph using matplotlib
# plt.bar(video_indices, durations)
# plt.xticks(video_indices, video_names, rotation=45, ha="right")
# plt.xlabel("Video Names")
# plt.ylabel("Duration")
# plt.title("Duration of Videos")
# plt.tight_layout()

# # Save the graph to a file and display it
# plt.savefig("output_graph.png")
# plt.show()



import matplotlib.pyplot as plt

# Data
files = [item[2] for item in data]
actual = [int(item[0]) for item in data]
expected = [int(item[1]) for item in data]

# Calculate accuracy
accuracy = [a / e * 100 for a, e in zip(actual, expected)]

# Plot the bar graph
fig, ax = plt.subplots()
ax.bar(files, accuracy)

# Set labels and title
ax.set_ylabel('Accuracy (%)')
ax.set_xlabel('Files')
ax.set_title('Accuracy for Mating Files')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the graph
plt.show()