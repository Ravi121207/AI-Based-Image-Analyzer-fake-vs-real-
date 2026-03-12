import cv2
import numpy as np

def analyze_image(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return "Image not found"

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Sharpness
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Edge density
    edges = cv2.Canny(gray, 50, 150)
    edge_density = np.count_nonzero(edges) / edges.size

    # Noise
    noise = np.std(gray)

    print("Sharpness:", laplacian_var)
    print("Edge Density:", edge_density)
    print("Noise:", noise)

    score = 0

    # AI images usually smoother (low noise)
    if noise < 15:
        score += 1

    # AI images usually have lower edge density
    if edge_density < 0.02:
        score += 1

    # AI images often have very smooth surfaces
    if laplacian_var < 120:
        score += 1

    if score >= 2:
        return "Fake Image (AI Generated)"
    else:
        return "Real Image (Camera Photo)"
