# refresher.py

![GitHub repo size](https://img.shields.io/github/repo-size/iceeyz1/refresher)
![GitHub stars](https://img.shields.io/github/stars/iceeyz1/refresher?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/iceeyz1/refresher)

A simple Python script that opens a website in your default browser and refreshes it automatically as many times as you want.

---

## Download

[![Download EXE](https://img.shields.io/badge/Download-Windows%20Executable-green)](https://github.com/iceeyz1/refresher/releases/tag/executeable)

Download the compiled `.exe` if you don't want to install Python.

---

## Features

- Opens any website link in your default browser
- Automatically refreshes the page
- Lets you choose:
  - number of refreshes
  - delay between refreshes
- Very lightweight
- No browser extensions required

---

## How it Works

The script:

1. Asks you for a website URL
2. Asks how many times the page should be refreshed
3. Asks how many seconds to wait between refreshes
4. Opens the website in your default browser
5. Presses `F5` repeatedly to refresh the page

---

## Requirements (for running the `.py` file)

You need Python installed.

Required modules:

- `webbrowser`
- `time`
- `pyautogui`

`webbrowser` and `time` are included with Python by default.

You only need to install **pyautogui**.

---

## Installation

Install the required module:

```bash
pip install pyautogui
```

Then run the script:

```bash
python refresher.py
```

---

## License

MIT License
