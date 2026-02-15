## 🖼️ Image Processing Tool (OpenCV + Python)

## 📌 Overview

A Python program to perform multiple image processing operations using OpenCV. Users can interactively:

- Add text on images  
- Draw shapes (rectangle, circle, ellipse)  
- Stack images horizontally or vertically  
- Blend two images  
- Detect edges  
- Add borders  
- Apply blurring  
- Convert images to grayscale  

All operations can be applied on any image with custom parameters like color, size, and position.

## 🚀 Key Features

- **Add custom text** with font, size, color, and thickness  
- **Stack up to 3 images** horizontally or vertically  
- **Draw rectangles, circles, and ellipses**  
- **Blend two images** with adjustable transparency  
- **Edge detection** using Canny  
- **Add borders** of specified size  
- **Gaussian, Median, and Bilateral blurring**  
- **Convert images to grayscale**

## 🛠 Technologies Used

- Python  
- OpenCV  
- NumPy  

## 🔎 Project Workflow

### 1️⃣ Load and Resize Image
```python
image = cv2.imread(path)
image = cv2.resize(image, size)  # specify width and height

### 2️⃣ Add Text
cv2.putText(image, text, position, font, font_scale, color, thickness)

### 3️⃣ Image Stacking
stacked_img = np.vstack((image, sec_img))  # vertical
stacked_img = np.hstack((image, sec_img))  # horizontal

### 4️⃣ Draw Shapes
cv2.rectangle(image, top_left, bottom_right, color, thickness)
cv2.circle(image, center, radius, color, thickness)
cv2.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness)

### 5️⃣ Blend Two Images
blended = cv2.addWeighted(image, 0.5, sec_img, 0.5, 1)

### 6️⃣ Edge Detection
edges = cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient=True)

### 7️⃣ Add Border
bordered = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_ISOLATED)

### 8️⃣ Blurring
cv2.GaussianBlur(image, (7,7), 0)
cv2.medianBlur(image, 5)
cv2.bilateralFilter(image, 10, 100, 100)

### 9️⃣ Grayscale Conversion
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

### 📦 Installation
pip install opencv-python numpy

### ▶️ How to Run
python your_file_name.py

### 🎯 Use Cases
Image annotation and labeling
Basic computer vision experiments
Educational project for OpenCV beginners
Real-time image editing practice


