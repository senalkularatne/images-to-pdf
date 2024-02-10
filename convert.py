import os
from PIL import Image
from reportlab.pdfgen import canvas
from tqdm import tqdm
from pathlib import Path

images_directory_path = "./input/"
output_pdf_path = "output/my_file.pdf"

def collect_images(directory_path):
    image_paths = []
    for root, dirs, files in os.walk(directory_path):
        dirs.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
        for file in sorted(files, key=lambda x: int(''.join(filter(str.isdigit, x)) or -1)):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_paths.append(Path(root) / file)
    return image_paths

def images_to_pdf(image_paths, pdf_path):
    if not image_paths:
        print("\nNo images to convert.")
        return

    pdf_canvas = canvas.Canvas(str(pdf_path))
    print()
    for image_path in tqdm(image_paths, desc="Processing Images", unit="image"):
        try:
            with Image.open(image_path) as img:
                img_width, img_height = img.size
                pdf_canvas.setPageSize((img_width, img_height))
                pdf_canvas.drawImage(str(image_path), 0, 0, width=img_width, height=img_height)
                pdf_canvas.showPage()
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
    pdf_canvas.save()
    print(f"\nPDF created successfully: {pdf_path}")

image_paths = collect_images(images_directory_path)
images_to_pdf(image_paths, Path(output_pdf_path))
