<div align="center">

# 🎨 Image Compression Using K-means

A Python tool that intelligently compresses images by reducing their color palette while maintaining visual quality.


![Compression Example](images/output/comparison.png) (Credits: Coursera)

</div>

---

## 📋 Table of Contents
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/lakshmi2688/Image-Compression.git
cd Image-Compression

# 2. Install dependencies
pip install numpy Pillow matplotlib

# 3. Run example
python examples/example.py
```

## 📦 Installation

1. **Prerequisites**
   - Python 3.7+
   - pip package manager

2. **Required Packages**
   ```bash
   pip install numpy Pillow matplotlib
   ```

## 💻 Basic Usage

```python
from image_compressor import ImageCompressor

# Initialize compressor
compressor = ImageCompressor(n_colors=16)

# Compress image
compressor.compress_image(
    'images/input/photo.jpg',
    'images/output/compressed.jpg'
)

# Show comparison
compressor.show_comparison(
    'images/input/photo.jpg',
    'images/output/compressed.jpg',
    'images/output/comparison.jpg'
)
```

## 📁 Project Structure
```
image-compression/
├── image_compressor.py    # Main compression algorithm
├── examples/
│   └── example.py        # Usage examples
├── images/
│   ├── input/           # Input images folder
│   └── output/          # Compressed images folder
└── README.md
```

## 🎯 Examples

### 1. Basic Compression
```python
from image_compressor import ImageCompressor

compressor = ImageCompressor()
compressor.compress_image('input.jpg', 'output.jpg')
```

### 2. Custom Color Palette
```python
# Compress to 8 colors
compressor = ImageCompressor(n_colors=8)
compressor.compress_image('input.jpg', 'output.jpg')
```

### 3. Visual Comparison
```python
# Show before/after comparison
compressor.show_comparison('input.jpg', 'output.jpg')
```

## 📚 Documentation

### ImageCompressor Class

#### Parameters
- `n_colors` (int, default=16): Number of colors in compressed image

#### Methods
1. `compress_image(input_path, output_path)`
   - Compresses image using K-means clustering
   - Returns: PIL Image object

2. `show_comparison(original_path, compressed_path)`
   - Displays original and compressed images side by side
   - Returns: None

## ❗ Troubleshooting

### Common Issues

1. **ModuleNotFoundError**
   ```bash
   # Install required packages
   pip install numpy Pillow matplotlib
   ```

2. **Image Not Found Error**
   ```bash
   # Check image path
   mv your_image.jpg images/input/
   ```

3. **Permission Error**
   ```bash
   # Fix permissions
   chmod 755 images/output
   ```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📊 Results

### Performance Metrics
| Metric | Original | Compressed |
|--------|----------|------------|
| File Size | 2.4 MB | 0.4 MB |
| Colors | Millions | 16 |
| Quality | 100% | ~95% |

### Visual Examples
![Compression Results](images/results.png)

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.




</div>
