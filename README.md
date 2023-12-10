# One-Click Dense Pose

## Overview

Video Credit: <a href"https://www.pexels.com/video/hip-hop-dancing-2795746/">cottonbro studio at pexels</a>

The One-Click Dense Pose project is designed to simplify the process of converting a regular input video into a DensePose-enhanced video with just a single command. DensePose is a method for mapping pixels in images of people to 3D surface coordinates and body part labels. This project streamlines the conversion process, making it accessible with minimal effort.

## Installation

To get started, follow these simple steps for setting up the One-Click Dense Pose project:

1. Clone the repository:

   ```bash
   git clone https://github.com/Pawandeep-prog/one-click-dense-pose.git
   cd one-click-dense-pose
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the pre-trained DensePose models:

   ```bash
   sh download-models.sh
   ```

4. Run the conversion script:

   ```bash
   python convert.py --input PATH_TO_INPUT_VIDEO --output OUTPUT_VIDEO_PATH
   ```

Replace `PATH_TO_INPUT_VIDEO` with the path to your input video file and `OUTPUT_VIDEO_PATH` with the desired path for the output DensePose video.

## Contributions Welcome

This project is in its initial stages, and contributions are highly encouraged. Feel free to fork the repository, make improvements, fix bugs, or add new features. Submit pull requests to contribute to the development of the One-Click Dense Pose tool. Your ideas and enhancements are welcome as we work together to make this tool even more powerful and user-friendly.
