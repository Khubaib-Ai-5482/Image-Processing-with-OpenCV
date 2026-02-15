🖼️ Image Processing Tool (OpenCV + Python)
📌 Overview

A Python program to perform multiple image processing operations using OpenCV. Users can interactively:

Add text on images

Draw shapes (rectangle, circle, ellipse)

Stack images horizontally or vertically

Blend two images

Detect edges

Add borders

Apply blurring

Convert images to grayscale

All operations can be applied on any image with custom parameters like color, size, and position.

🚀 Key Features

✔ Add custom text with font, size, color, and thickness
✔ Stack up to 3 images horizontally or vertically
✔ Draw rectangles, circles, and ellipses
✔ Blend two images with adjustable transparency
✔ Edge detection using Canny
✔ Add borders of specified size
✔ Gaussian, Median, and Bilateral blurring
✔ Convert images to grayscale

🛠 Technologies Used

Python

OpenCV

NumPy

🔎 Project Workflow
1️⃣ Load and Resize Image

User provides the image path

Input desired width (x_size) and height (y_size)

Image is resized accordingly

image = cv2.imread(path)
image = cv2.resize(image, size)

2️⃣ Add Text

Input text, position, font scale, color (BGR), and thickness

Text appears on the image

cv2.putText(image, text, position, font, font_scale, color, thickness)

3️⃣ Image Stacking

Stack images vertically or horizontally

Up to 3 images supported

Images are resized to match the first image

stacked_img = np.vstack((image, sec_img))
# or
stacked_img = np.hstack((image, sec_img))

4️⃣ Draw Shapes

Rectangle, Circle, or Ellipse

Specify position, size, color, and thickness

cv2.rectangle(image, top_left, bottom_right, color, thickness)
cv2.circle(image, center, radius, color, thickness)
cv2.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness)

5️⃣ Blend Two Images

Combine two images with weights (0.0–1.0)

blended = cv2.addWeighted(image, 0.5, sec_img, 0.5, 1)

6️⃣ Edge Detection

Canny edge detection with customizable thresholds

edges = cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient=True)

7️⃣ Add Border

Add border around image with custom top, bottom, left, and right values

bordered = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_ISOLATED)

8️⃣ Blurring

Apply Gaussian Blur, Median Blur, or Bilateral Filter

cv2.GaussianBlur(image, (7,7), 0)
cv2.medianBlur(image, 5)
cv2.bilateralFilter(image, 10, 100, 100)

9️⃣ Grayscale Conversion

Convert color image to grayscale

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

📦 Installation

Install required packages:

pip install opencv-python numpy

▶️ How to Run
python image_tool.py


Follow the menu-driven prompts to apply different operations

🎯 Use Cases

Image annotation and labeling

Basic computer vision experiments

Educational project for OpenCV beginners

Real-time image editing practice

👨‍💻 Author

Interactive Python project for learning image processing using OpenCV and NumPy.

If you find this project helpful, give it a ⭐ on GitHub!
