#!/bin/bash

# Define the input file and the checkpoint model path
input_file="data/ucfTrainTestlist/testlist01.txt"
checkpoint_model="model_checkpoints/ConvLSTM_195.pth"
video_path_prefix="data/UCF-101/"

# Check if the file exists
if [ -f "$input_file" ]; then
  # Read and process each video path in the input file
  while IFS= read -r video_path; do
    # Remove the '\r' character from the video path
    video_path=$(echo "$video_path" | tr -d '\r')
    # Add the video path prefix
    full_video_path="${video_path_prefix}${video_path}"
    # Execute the Python script with the video path and checkpoint model
    python3 test_on_video.py --video_path "$full_video_path" --checkpoint_model "$checkpoint_model"
  done < "$input_file"
else
  echo "Error: File '$input_file' does not exist."
fi