# refresher.py

A simple Python script that opens a website in your default browser and refreshes it automatically as many times as you want.

## Download
[![Download EXE](https://img.shields.io/badge/Download-Windows%20Executable-green)](https://github.com/iceeyz1/refresher/releases/tag/executeable)

## Features

- Opens any website link in your default browser
- Refreshes the page automatically
- Lets you choose:
  - the number of refreshes
  - the delay between each refresh
- Very lightweight and easy to use

## How it works

The script:

1. Asks you for a website URL
2. Asks how many times the page should be refreshed
3. Asks how many seconds to wait between refreshes
4. Opens the website in your default browser
5. Presses `F5` repeatedly to refresh the page

## Requirements (If you want to run the .py)

You need Python installed, plus these modules:

- `webbrowser`  
- `time`  
- `pyautogui`

`webbrowser` and `time` are included with Python by default.  
You only need to install `pyautogui`.

## Installation

Install `pyautogui` with:

```bash
pip install pyautogui
