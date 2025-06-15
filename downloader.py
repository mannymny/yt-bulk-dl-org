import os
import re
from pytube import YouTube, Channel, Playlist

KEYWORDS = {
    "Ibai": "Ibai",
    "Example Keyword": "example_keyword",
    "Nature": "Nature",
}

DOWNLOADS_FOLDER = "videos"


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


def get_folder_for_video(title):
    for keyword, folder in KEYWORDS.items():
        if keyword.lower() in title.lower():
            return folder
    return "Otros"


def download_video(url):
    yt = YouTube(url)
    title = sanitize_filename(yt.title)
    folder = get_folder_for_video(title)
    save_path = os.path.join(DOWNLOADS_FOLDER, folder)
    os.makedirs(save_path, exist_ok=True)

    print(f"➡️  Downloading: {title} -> {folder}")

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(output_path=save_path, filename=f"{title}.mp4")


def download_channel(channel_url):
    ch = Channel(channel_url)
    print(f"\n📺 Downloading chanel: {ch.channel_name} ({len(ch.video_urls)} videos)\n")
    for video_url in ch.video_urls:
        try:
            download_video(video_url)
        except Exception as e:
            print(f"⚠️  Error with {video_url}: {e}")


def download_playlist(playlist_url):
    pl = Playlist(playlist_url)
    print(f"\n🎵 Downloading playlist: {pl.title} ({len(pl.video_urls)} videos)\n")
    for video_url in pl.video_urls:
        try:
            download_video(video_url)
        except Exception as e:
            print(f"⚠️  Error with {video_url}: {e}")


def main():
    print("🎬 Enter YouTube video, channel, or playlist URLs (one per line).")
    print("🔸 Type 'END' when you are done.\n")
  
    urls = []
    while True:
        url = input("URL: ").strip()
        if url.lower() == "end":
            break
        if url:
            urls.append(url)

    for url in urls:
        try:
            if "playlist?list=" in url:
                download_playlist(url)
            elif "/@":
                if "youtube.com/@":
                    download_channel(url)
                else:
                    download_video(url)
            else:
                download_video(url)
        except Exception as e:
            print(f"⚠️  Error with {url}: {e}")

    print("\n✅ Download finished.")


if __name__ == "__main__":
    main()
