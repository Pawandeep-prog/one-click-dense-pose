import cv2
from utils.helper import GetLogger, Predictor
from argparse import ArgumentParser
import sys


parser = ArgumentParser()
parser.add_argument("--input", type=str, help="Set the input path to the video", required=True)
parser.add_argument("--out", type=str, help="Set the output path to the video", required=True)
args = parser.parse_args()


logger = GetLogger.logger(__name__)
predictor = Predictor()

# Open video file
video_path = args.input
cap = cv2.VideoCapture(video_path)

# Get video information
fps = cap.get(cv2.CAP_PROP_FPS)
n_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
logger.info(f"No of frames {n_frames}")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter for output
output_path = args.out
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Process each frame
done = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    out_frame, out_frame_seg = predictor.predict(frame)

    # Write the frame to the output video
    out.write(out_frame_seg)

    done += 1
    percent = int((done/n_frames)*100)
    sys.stdout.write("\rProgress: [{}{}] {}%".format("="*percent, " "*(100-percent), percent))
    sys.stdout.flush()

# Release video capture and writer
cap.release()
out.release()
