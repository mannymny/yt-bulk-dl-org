# 📥 YouTube Bulk Downloader & Organizer

A **Python script** to download **multiple YouTube videos**, playlists, or entire channels, and automatically organize them into folders based on **keywords found in the video titles**.

Easily categorize your downloads by topic or name — for example, videos containing "Frank Cuesta" or "Raed" will be saved in separate folders.

---

## 🚀 Features

* ✅ Download **individual videos**, **playlists**, or **entire channels**
* 📂 Automatically **organizes videos into folders** based on keywords
* 🏷️ Configurable **keywords-to-folder mapping**
* 🎥 Downloads videos in **MP4** (highest available resolution)
* ❗ Handles invalid filenames by sanitizing them
* 🖥️ Interactive command-line interface
* ⚠️ Error handling for unavailable videos or connection issues

---

## 📁 Folder Structure Example

```
videos/
├── keyword_folder/
│   └── Video1.mp4
├── keyword_folder_2/
│   └── Video2.mp4
└── keyword_folder_3/
    └── Video3.mp4
```

---

## 🛠️ Requirements

* Python 3.7+
* [`pytube`](https://pytube.io/)

Install dependencies:

```bash
pip install pytube
```

---

## 💻 Usage

1. **Run the script:**

```bash
python downloader.py
```

2. **Enter the YouTube URLs**:

```
URL: https://www.youtube.com/@ExampleChannel
URL: https://www.youtube.com/watch?v=EXAMPLE123
URL: https://www.youtube.com/playlist?list=PLxxxxxxxxxxxx
URL: END
```

3. **Videos will be saved to**:

```
videos/<Keyword_Folder>/<VideoTitle>.mp4
```

---

## ⚙️ Configuration

Edit the `KEYWORDS` dictionary in `downloader.py` to match your organization preferences:

```python
KEYWORDS = {
    "Ibai": "Ibai",
    "Example Keyword": "example_keyword",
    "Nature": "Nature",
    # Add more as needed
}
```

Any video title **not matching any keyword** will be saved to the **"Others"** folder.

---

## ✅ To Do / Planned Features

* [ ] Clip option (choose the start and end of the video)
* [ ] Audio-only download option
* [ ] Graphical User Interface (GUI) version

---

## 📃 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by \[Manny]

Contributions, issues, and feature requests are welcome!

---
