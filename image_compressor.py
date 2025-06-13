import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageCompressor:
    def __init__(self, n_colors=16):
        """Initialize with number of colors for compression"""
        self.n_colors = n_colors
        
    def compress_image(self, image_path, output_path=None):
        """Compress image using K-means clustering"""
        # Load and prepare image
        image = Image.open(image_path)
        pixels = np.array(image)
        w, h, d = pixels.shape
        
        # Reshape pixels for clustering
        pixel_array = pixels.reshape(-1, 3)
        
        # Perform K-means clustering
        centroids = self._kmeans(pixel_array)
        
        # Map each pixel to nearest centroid
        labels = self._find_closest_centroids(pixel_array, centroids)
        compressed_pixels = centroids[labels]
        
        # Reshape back to image dimensions
        compressed_image = compressed_pixels.reshape(w, h, d)
        compressed_image = compressed_image.astype(np.uint8)
        
        # Convert to PIL Image
        result = Image.fromarray(compressed_image)
        
        # Save if output path provided
        if output_path:
            result.save(output_path)
            
        return result
    
    def _kmeans(self, pixels, max_iters=10):
        """Perform K-means clustering on pixel data"""
        # Randomly initialize centroids
        idx = np.random.permutation(len(pixels))
        centroids = pixels[idx[:self.n_colors]]
        
        for _ in range(max_iters):
            # Assign pixels to nearest centroid
            labels = self._find_closest_centroids(pixels, centroids)
            
            # Update centroids
            for k in range(self.n_colors):
                if len(pixels[labels == k]) > 0:
                    centroids[k] = np.mean(pixels[labels == k], axis=0)
                    
        return centroids
    
    def _find_closest_centroids(self, pixels, centroids):
        """Find closest centroid for each pixel"""
        distances = np.sqrt(((pixels - centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)
    
    def show_comparison(self, original_path, compressed_path):
        """Display original and compressed images side by side"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        
        # Show original image
        original = Image.open(original_path)
        ax1.imshow(original)
        ax1.set_title('Original')
        ax1.axis('off')
        
        # Show compressed image
        compressed = Image.open(compressed_path)
        ax2.imshow(compressed)
        ax2.set_title(f'Compressed ({self.n_colors} colors)')
        ax2.axis('off')
        
        plt.show()
