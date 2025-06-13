import os
import sys
from pathlib import Path

# Get the absolute path of the project root
current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
project_root = os.path.dirname(current_dir)

# Add the project root to Python path
if project_root not in sys.path:
    sys.path.append(project_root)
    print(f"Added {project_root} to Python path")

try:
    from image_compressor import ImageCompressor
    print("Successfully imported ImageCompressor")
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Current sys.path: {sys.path}")
    sys.exit(1)

def main():
    try:
        # Set up paths
        input_path = os.path.join(project_root, 'images', 'input', 'example.png')
        output_path = os.path.join(project_root, 'images', 'output', 'compressed.png')
        
        print(f"Project root: {project_root}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Input path: {input_path}")
        print(f"File exists: {os.path.exists(input_path)}")
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Initialize compressor and process image
        compressor = ImageCompressor(n_colors=16)
        compressor.compress_image(input_path, output_path)
        compressor.show_comparison(input_path, output_path)
        
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()
