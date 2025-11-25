import os
from pytube import Playlist, YouTube
from moviepy.editor import AudioFileClip # For converting to MP3

def download_playlist_as_mp3(playlist_url, output_path="downloads"):
    """
    Downloads a YouTube playlist's audio as MP3 files.

    Args:
        playlist_url (str): The URL of the YouTube playlist.
        output_path (str): The directory to save the MP3 files.
    """
    try:
        playlist = Playlist(playlist_url)
        print(f"Downloading playlist: {playlist.title}")
        os.makedirs(output_path, exist_ok=True)

        for video_url in playlist.video_urls:
            try:
                yt = YouTube(video_url)
                print(f"Downloading audio for: {yt.title}")

                # Get the highest quality audio stream
                audio_stream = yt.streams.filter(only_audio=True).first()

                if audio_stream:
                    # Download the audio stream
                    downloaded_file = audio_stream.download(output_path=output_path)
                    
                    # Convert to MP3 using moviepy (which utilizes FFmpeg)
                    base, ext = os.path.splitext(downloaded_file)
                    mp3_filename = f"{base}.mp3"

                    audio_clip = AudioFileClip(downloaded_file)
                    audio_clip.write_audiofile(mp3_filename)
                    audio_clip.close()

                    # Remove the original downloaded audio file (e.g., .webm)
                    os.remove(downloaded_file)
                    print(f"Successfully downloaded and converted {yt.title} to MP3.")
                else:
                    print(f"No audio stream found for {yt.title}. Skipping.")

            except Exception as e:
                print(f"Error downloading or converting video {video_url}: {e}")

    except Exception as e:
        print(f"Error processing playlist {playlist_url}: {e}")

if __name__ == "__main__":
    playlist_link = input("Enter the YouTube playlist URL: ")
    download_playlist_as_mp3(playlist_link)