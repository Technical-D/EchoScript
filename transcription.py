import whisper
import os
import ffmpeg

def convert_video_to_audio(video_path, output_audio_path):
    # Converting video file into audio for transcription
    try:
        ffmpeg.input(video_path).output(output_audio_path, format='mp3', acodec='mp3').run(quiet=True, overwrite_output=True)
        return output_audio_path
    except Exception as e:
        print(f"Error converting {video_path} to audio: {e}")
        return None 

def transcribe_audio(file_path, model):
    # Transcribing the audio file
    print(f"Transcribing: {file_path} ...")
    result = model.transcribe(file_path)
    return result["text"]

def save_transcription(file_name, text, output_folder):
    # Saving transcription in output folder
    output_file = os.path.join(output_folder, f"{file_name}.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved transcription: {output_file}")

def process_files(audio_files, video_files, output_folder="transcriptions"):
    # Creating a output directory
    os.makedirs(output_folder, exist_ok=True)
    model = whisper.load_model("tiny")

    # looping through audio file
    for file_name, file_path in audio_files.items():
        text = transcribe_audio(file_path, model)
        save_transcription(file_name, text, output_folder)

    # looping through video file
    for file_name, file_path in video_files.items():
        audio_path = os.path.join(output_folder, f"{file_name}.mp3")
        converted_audio = convert_video_to_audio(file_path, audio_path)
        
        if converted_audio:
            text = transcribe_audio(converted_audio, model)
            save_transcription(file_name, text, output_folder)
            os.remove(converted_audio) # Removing the converted audio file

    print("Transcription process completed!")