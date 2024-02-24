# Images to PDF Converter

This Python script allows you to combine multiple images from a specified directory (including subdirectories) into a single PDF file. It's designed to handle images in a sequential order, making it ideal for converting book pages, scanned documents, or any series of images into a single PDF document.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Sorting Order and Conversion Process](#sorting-order-and-conversion-process)
  - [Example Directory Structure and Conversion](#example-directory-structure-and-conversion)
  - [Customizing the Order](#customizing-the-order)
- [License](#license)

---

## Features

- Recursively processes all images in the specified directory and its subdirectories.
- Supports `.png`, `.jpg`, and `.jpeg` image formats.
- Orders images naturally based on their file names and directory structure.
- Generates a high-quality PDF without altering the resolution of the original images.
- Provides a progress bar for real-time feedback during the conversion process.

---

## Prerequisites

Before running the script, ensure you have Python 3.6 or later installed on your system. You will also need to install the following Python packages:

- Pillow
- reportlab
- tqdm

You can install these packages using pip:

```sh
pip install Pillow reportlab tqdm
```

---

## Usage

1. Clone this repository or download the script to your local machine.
2. Modify the `images_directory_path` variable in the script to point to the directory containing your images.
3. Modify the `output_pdf_path` variable in the script to specify the desired output path and filename for the PDF.
4. Run the script using Python:

```sh
python3 convert.py
```

The script will process all images found in the specified directory and its subdirectories, combining them into a single PDF file at the specified output location. A progress bar will display in the terminal to indicate the script's progress.

---

## Sorting Order and Conversion Process

The "ImageMergePDF" tool processes images by traversing the specified root directory and its subdirectories recursively. The order in which images are combined into the PDF is determined by the sorting of directory and file names at each level. Here's a breakdown of the sorting logic:

### Example Directory Structure and Conversion

Consider the following directory structure as an example:

```
ProjectFolder/
├── 01_EventPhotos/
│   ├── 01_Event1/
│   │   ├── 01_photo.jpg
│   │   ├── 02_photo.jpg
│   │   └── 03_photo.jpg
│   └── 02_Event2/
│       ├── 01_photo.jpg
│       ├── 02_photo.jpg
│       └── 03_photo.jpg
└── 02_VacationPhotos/
    ├── 01_Beach/
    │   ├── 001_img.jpg
    │   ├── 002_img.jpg
    │   └── 003_img.jpg
    └── 02_City/
        ├── A_image.jpg
        ├── B_image.jpg
        └── C_image.jpg
```

### Customizing the Order

- If you need to customize the order in which images are combined, consider renaming your directories and files to fit the alphanumeric sorting logic. Prefixing names with numbers (e.g., `01_`, `02_`, etc.) is a straightforward way to control the order explicitly.

---

## License

This project is open source and available under the [MIT License](LICENSE).
