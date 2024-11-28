# YouTube Live Stream Downloader

This Python script allows you to download YouTube live streams in the best available quality (e.g., 1080p60) by dynamically selecting the formats and merging video and audio streams using `ffmpeg`. The script includes an interactive interface for entering the YouTube URL, selecting the cookies file, and choosing the output directory.

## Features
- Downloads YouTube live streams from the start of the DVR buffer.
- Supports 1080p60 quality (if available).
- Merges video and audio streams into a single file.
- Interactive pop-ups for input.

## Prerequisites
1. **Python 3.7+** installed. You can download it from [python.org](https://www.python.org/).
2. **yt-dlp**: Install using pip (`pip install yt-dlp`).
3. **ffmpeg**: Required for merging video and audio. [Download ffmpeg](https://ffmpeg.org/) and ensure it is added to your system's PATH.
4. A **cookies.txt** file exported from your browser with authentication for YouTube.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Monster-ZeroX/YouTube-Live-Capture.git
   cd YouTube-Live-Capture
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
## Usage
1. Run the script:
```bash
python interactive_live_download.py
```
2. Follow the pop-ups to:
- Enter the YouTube live stream URL.
- Select the cookies.txt file exported from your browser.
- Choose the output folder to save the downloaded video.
## Requirements
- ```yt-dlp```: For downloading video and audio.
- ```ffmpeg```: For merging video and audio streams.
## Troubleshooting
- If the script fails to run, ensure yt-dlp and ffmpeg are properly installed and accessible in your PATH.
- Check the cookies.txt file to ensure it includes valid YouTube authentication details.
## License
This project is licensed under the MIT License. See the ```LICENSE``` file for details.

## Contributing
Feel free to open an issue or submit a pull request for improvements and fixes.
