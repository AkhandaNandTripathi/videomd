import subprocess
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to install moviepy
def install_moviepy():
    logger.info("Checking if 'moviepy' is installed...")
    try:
        import moviepy.editor as mp
        logger.info("'moviepy' is already installed.")
    except ImportError:
        logger.info("'moviepy' not found. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "moviepy"])
        logger.info("'moviepy' installed successfully.")
        import moviepy.editor as mp
    return mp

# Install moviepy if not already installed
mp = install_moviepy()

from moviepy.editor import VideoFileClip, concatenate_videoclips

# List of MKV video files to merge
video_files = [
    "video1.mkv", "video2.mp4", "video3.mkv", "video4.mkv", "video5.mkv",
    "video6.mkv", "video7.mkv", "video8.mkv", "video9.mkv", "video10.mkv",
    "video11.mkv", "video12.mkv", "video13.mkv", "video14.mkv"  # Added video14.mkv
]

# Ensure all files are accessible
for video in video_files:
    try:
        open(video, 'r')
        logger.info(f"File '{video}' is accessible.")
    except IOError:
        logger.error(f"Error: File '{video}' not found or cannot be opened.")
        sys.exit(1)

# Load video clips
logger.info("Loading video clips...")
clips = [VideoFileClip(video) for video in video_files]

# Concatenate videos
logger.info("Concatenating video clips...")
final_clip = concatenate_videoclips(clips, method="compose")

# Write the final video to a file
output_file = "merged_video.mkv"
logger.info(f"Writing the final video to '{output_file}'...")
final_clip.write_videofile(output_file, codec="libx264", threads=4)
logger.info(f"Video merging complete. Output saved as '{output_file}'.")
