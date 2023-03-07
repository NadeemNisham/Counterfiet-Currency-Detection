import cv2

# List of video filenames to process
video_files = ['10a.mp4', '10b.mp4', '10c.mp4', 'cent_10b.mp4', 'cent_50.mp4', 'cent_50b.mp4']

# Loop through each video file
for video_file in video_files:
    # Open the video file
    cap = cv2.VideoCapture(video_file)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print(f"Error opening video file: {video_file}")
        continue

    # Initialize a frame counter
    frame_count = 0

    # Loop through each frame of the video
    while cap.isOpened():
        # Read the next frame from the video
        ret, frame = cap.read()

        # Check if a frame was successfully read
        if not ret:
            break

        # Save the frame as an image file
        cv2.imwrite(f"{video_file}_frame_{frame_count}.jpg", frame)

        # Increment the frame counter
        frame_count += 1

    # Release the video file
    cap.release()

# Close all windows
cv2.destroyAllWindows()


