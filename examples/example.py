import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from image_compressor import ImageCompressor

def main():
    # Initialize compressor
    compressor = ImageCompressor(n_colors=16)
    
    # Compress image
    input_path = '../images/input/example.png'
    output_path = '../images/output/compressed.jpg'
    
    # Perform compression
    compressor.compress_image(input_path, output_path)
    
    # Show comparison
    compressor.show_comparison(input_path, output_path)

if __name__ == "__main__":
    main()
