from pytube import YouTube

class YouTubeDownloader:
    def download(self, url, quality):
        if not url:
            return "Please enter a valid YouTube URL!"
        try:
            yt = YouTube(url)
            if quality == "Audio Only (MP3)":
                stream = yt.streams.filter(only_audio=True).first()
                filename = stream.download()
                self.convert_to_mp3(filename)
                return "Download completed as MP3!"
            else:
                stream = yt.streams.filter(res=quality[:-1] + "p").first()
                if not stream:
                    return "Selected quality is not available."
                stream.download()
                return "Download completed successfully!"
        except Exception as e:
            return f"Error: {str(e)}"

    def convert_to_mp3(self, filename):
        if filename.endswith(".mp4"):
            import os
            base, _ = os.path.splitext(filename)
            os.rename(filename, base + ".mp3")
