# Program To Read video
# and Extract Frames
import cv2
import os.path
import os


# Function to extract frames
def dump_video_frames(path_to_video_file, folder_for_frames):
    # get filename w/o extension
    video_file_name = os.path.basename(path_to_video_file)
    video_file_name = os.path.splitext(video_file_name)[0].lower()

    # setup frame folders
    os.mkdir(os.path.join(folder_for_frames, video_file_name))

    # read video using opencv
    video = cv2.VideoCapture(path_to_video_file)

    # frame counter
    count = 0

    # checks whether frames were extracted
    success = 1

    # loop
    while success:
        # get a frame
        success, image = video.read()

        # save frame
        the_frame = os.path.join(folder_for_frames, f"frame{count}.jpg")
        try:
            cv2.imwrite(the_frame, image)
            count += 1
        except Exception:
            # we continue looping till the end
            pass


def main():
    data_path = "./data"
    frame_path = "./data/frames"
    support_extensions = [".mp4", ".avi"]

    for root, dirs, files in os.walk(data_path):
        basename = os.path.basename(root)

        for video in files:
            filename, ext = os.path.split(video)

            if ext.lower() not in support_extensions:
                continue

            dump_video_frames(
                os.path.join(root, video), os.path.join(frame_path, basename)
            )


if __name__ == "__main__":
    # FrameCapture("/home/fengxia/Downloads/Sniffing_537.mp4", "./tmp")
    main()
