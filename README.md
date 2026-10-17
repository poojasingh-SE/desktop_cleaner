#  Desktop Cleaner

A Python script that automatically organizes your Desktop files into
folders based on their extensions (Images, Documents, Zips).

Built as my first Python automation project — learning while shipping.

## Features

- 📁 Extension-based sorting (Images / Documents / Zips)
- 🔒 Collision-safe (never overwrites — skips if file exists)
- ⚠️ Per-file error handling (one locked file doesn't break the batch)
- 🪟 Native Windows popup on completion
- 🧩 Pure standard library — no `pip install` needed

## How It Works

1. Scans your Desktop
2. Reads each file's extension
3. Moves it into the right folder (`Images/`, `Documents/`, `Zips/`)
4. Shows a summary popup

## Usage

```bash
python cleaner.py