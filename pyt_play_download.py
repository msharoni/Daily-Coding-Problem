import os
from pytubefix import Playlist
from pytubefix.cli import on_progress

def download_playlist_as_mp3(url):
    try:
        # Load the playlist
        pl = Playlist(url)
        print(f"Downloading playlist: {pl.title}")
        
        # Create a folder for the playlist if it doesn't exist
        folder_name = "".join([c for c in pl.title if c.isalnum() or c in (' ', '_')]).strip()
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for video in pl.videos:
            print(f"\nProcessing: {video.title}")
            
            # Filter for audio-only streams
            stream = video.streams.get_audio_only()
            
            # Download the file
            out_file = stream.download(output_path=folder_name)
            
            # Rename to .mp3 (YouTube sends them as .m4a or .webm)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            
            # If the file already exists, remove it first to avoid errors
            if os.path.exists(new_file):
                os.remove(new_file)
                
            os.rename(out_file, new_file)
            print(f"Successfully saved: {video.title}.mp3")

        print("\n--- All downloads complete! ---")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLcvEin2DQhrR45iMgO3t8_RBUkKeb_ETK"
    download_playlist_as_mp3(playlist_url)

