import os
import subprocess
from tkinter import Tk, filedialog, simpledialog, messagebox

def download_and_merge_youtube_live_stream(youtube_live_url, cookies_file_path, output_folder, output_filename="live_stream_1080p60.mp4"):
    """
    Downloads a YouTube live stream in the best available 1080p60 quality using yt-dlp 
    and merges video/audio streams using ffmpeg.
    
    :param youtube_live_url: The URL of the YouTube live stream.
    :param cookies_file_path: Path to the cookies.txt file for authentication.
    :param output_folder: Folder path to save the downloaded stream.
    :param output_filename: Name of the final output file (merged).
    """
    try:
        # Ensure the output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Construct the full output path
        final_output_path = os.path.join(output_folder, output_filename)
        
        # Temp files for video and audio
        video_output = os.path.join(output_folder, "video.mp4")
        audio_output = os.path.join(output_folder, "audio.mp4")
        
        # yt-dlp command to download best available 1080p60 video and audio separately
        download_command = [
            "yt-dlp",
            "--hls-use-mpegts",  # Ensures no corruption in case of interruptions
            "--live-from-start",  # Downloads the stream from the beginning of DVR buffer
            "--cookies", cookies_file_path,  # Use cookies for authentication
            "-f", "bestvideo[height=1080][fps=60]+bestaudio",  # Dynamically select the best 1080p60 video and audio
            "--retries", "10",  # Retry limit for overall download
            "--fragment-retries", "10",  # Retry limit for individual fragments
            "--output", video_output,  # Temporary video output path
            youtube_live_url
        ]

        # Run yt-dlp command
        subprocess.run(download_command, check=True)
        print(f"Download completed. Merging video and audio streams...")

        # ffmpeg command to merge video and audio into a single file
        merge_command = [
            "ffmpeg",
            "-i", video_output,  # Input video
            "-i", audio_output,  # Input audio
            "-c:v", "copy",  # Copy video codec
            "-c:a", "copy",  # Copy audio codec
            final_output_path  # Final merged output
        ]

        # Run ffmpeg command
        subprocess.run(merge_command, check=True)
        print(f"Merge completed. Final file saved at: {final_output_path}")

        # Cleanup temp files
        os.remove(video_output)
        os.remove(audio_output)
        print("Temporary files cleaned up.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure 'yt-dlp' and 'ffmpeg' are installed and available in PATH.")

def get_user_inputs():
    """
    Opens popups to get inputs from the user for the YouTube URL, cookies file, and output folder.
    """
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Get YouTube live URL
    youtube_live_url = simpledialog.askstring("Input", "Enter the YouTube live URL:")
    if not youtube_live_url:
        print("No URL provided. Exiting.")
        return None, None, None

    # Get cookies file path
    cookies_file_path = filedialog.askopenfilename(title="Select Cookies File")
    if not cookies_file_path:
        print("No cookies file selected. Exiting.")
        return None, None, None

    # Get output folder
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        print("No output folder selected. Exiting.")
        return None, None, None

    # Confirmation popup
    confirm_message = (
        f"Please confirm your inputs:\n\n"
        f"YouTube Live URL: {youtube_live_url}\n"
        f"Cookies File Path: {cookies_file_path}\n"
        f"Output Folder: {output_folder}\n\n"
        f"Do you want to proceed?"
    )
    confirm = messagebox.askyesno("Confirm Inputs", confirm_message)
    if not confirm:
        print("User cancelled the operation.")
        return None, None, None

    return youtube_live_url, cookies_file_path, output_folder

if __name__ == "__main__":
    # Get inputs from the user
    youtube_live_url, cookies_file_path, output_folder_path = get_user_inputs()
    
    if youtube_live_url and cookies_file_path and output_folder_path:
        download_and_merge_youtube_live_stream(youtube_live_url, cookies_file_path, output_folder_path)
