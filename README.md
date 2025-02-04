# EchoScript

## Project Overview

**EchoScript** is a Python script that processes media files (audio and video) within a given directory and transcribes them using the Whisper model. The project supports scanning directories recursively, extracting audio/video files, and generating text transcriptions that are saved in a structured format.

## Features

- Recursively scans directories for audio and video files.
- Utilizes the Whisper model for transcribing audio and video content.
- Saves transcriptions in a designated folder in text format.
- Supports both audio and video file transcription.
- Handles different audio/video file formats.

## Requirements

Before running the script, ensure you have the following dependencies installed:

- Python 3.10 or higher
- Whisper (OpenAI Whisper model for transcription)
- ffmpeg (for handling audio and video processing)
- os (for file and directory handling)

### Required Python Packages

```bash
pip install openai-whisper
pip install ffmpeg-python
```

### Setup
  - Clone or download the EchoScript repository to your local machine.
  - Install the required Python packages using the command above.
  - Ensure you have ffmpeg installed on your system for Whisper to process media files.
  - Place your media files (audio/video) in the directory you want to process.

### Usage
To use EchoScript, run the script as follows:
```bash
python script.py
```

### Script Workflow:
  - The script will scan the provided folder path recursively.
  - It will identify and list all audio and video files in the folder and subfolders.
  - Using the Whisper model, it will transcribe the contents of each file.
  - The transcriptions will be saved in a specified output folder (e.g., transcriptions/).

### Notes
  - Ensure ffmpeg is correctly installed and accessible in your system's PATH for proper audio/video processing.
  - The transcriptions will be saved in the specified output folder, and filenames will be preserved.
  - For large files or directories, processing time may vary depending on the size and number of files.

### License
This project is open-source and available under the MIT License.
