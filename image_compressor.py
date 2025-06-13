import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

class ImageCompressor:
    def __init__(self, n_colors=16):
        self.n_colors = n_colors
        
    def compress_image(self, image_path, output_path=None):
        """Compress image using K-means clustering"""
        # Get absolute paths
        image_path = os.path.abspath(image_path)
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Input image not found: {image_path}")
            
        # Load and process image
        original_img = plt.imread(image_path)
        rgb_img = original_img
        
        # Reshape image for clustering
        X_img = np.reshape(rgb_img, (rgb_img.shape[0] * rgb_img.shape[1], 3))
        
        # Initialize centroids and run K-means
        initial_centroids = self._kmeans_init_centroids(X_img, self.n_colors)
        centroids, idx = self._run_kmeans(X_img, initial_centroids)
        
        # Compress image
        compressed = centroids[idx]
        compressed = np.reshape(compressed, original_img.shape)
        
        # Save compressed image if output path provided
        if output_path:
            plt.imsave(output_path, compressed)
        
        return compressed

    def _kmeans_init_centroids(self, X, K):
        """Initialize K centroids"""
        randidx = np.random.permutation(X.shape[0])
        centroids = X[randidx[:K]]
        return centroids
    
    def _find_closest_centroids(self, X, centroids):
        """Find closest centroids for all points"""
        K = centroids.shape[0]
        idx = np.zeros(X.shape[0], dtype=int)
        
        for i in range(X.shape[0]):
            distances = [np.linalg.norm(X[i] - centroids[j])**2 for j in range(K)]
            idx[i] = np.argmin(distances)
            
        return idx
    
    def _compute_centroids(self, X, idx, K):
        """Compute new centroids based on data points"""
        centroids = np.zeros((K, X.shape[1]))
        
        for k in range(K):
            points = X[idx == k]
            if len(points) > 0:
                centroids[k] = np.mean(points, axis=0)
                
        return centroids
    
    def _run_kmeans(self, X, initial_centroids, max_iters=10):
        """Run K-means clustering algorithm"""
        centroids = initial_centroids
        
        for i in range(max_iters):
            print(f"K-Means iteration {i}/{max_iters-1}")
            idx = self._find_closest_centroids(X, centroids)
            centroids = self._compute_centroids(X, idx, self.n_colors)
            
        return centroids, idx
    
    def show_comparison(self, original_path, compressed_path, comparison_path):
        """Display original and compressed images side by side"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 16))
        
        # Show original
        original = plt.imread(original_path)
        ax1.imshow(original)
        ax1.set_title('Original')
        ax1.axis('off')
        
        # Show compressed
        compressed = plt.imread(compressed_path)
        ax2.imshow(compressed)
        ax2.set_title(f'Compressed ({self.n_colors} colors)')
        ax2.axis('off')

        plt.savefig(comparison_path, bbox_inches='tight', dpi=300)
        plt.show()
        
    def show_color_palette(self, X_img):
        """Display the color palette used for compression"""
        initial_centroids = self._kmeans_init_centroids(X_img, self.n_colors)
        centroids, _ = self._run_kmeans(X_img, initial_centroids)
        
        palette = np.expand_dims(centroids, axis=0)
        num = np.arange(0, len(centroids))
        
        plt.figure(figsize=(16, 2))
        plt.xticks(num)
        plt.yticks([])
        plt.imshow(palette)
        plt.title('Color Palette')
        plt.show()
