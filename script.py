import os
from transcription import process_files

def scan_media_files(folder_path):
    # File extensions
    audio_extensions = {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"}
    video_extensions = {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"}

    # Dict to store the file location
    audio_files = {}
    video_files = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_name = os.path.splitext(file)[0].lower()
            file_ext = os.path.splitext(file)[1].lower()
            file_path = os.path.join(root, file)
            
            if file_ext in audio_extensions:
                audio_files[file_name] = file_path
            elif file_ext in video_extensions:
                video_files[file_name] = file_path
    return audio_files, video_files

audio_files, video_files = scan_media_files('media')
print("File extracted sucessfully!")
process_files(audio_files=audio_files, video_files=video_files, output_folder="transcriptions")