import os
import random

def get_camera_frame(data_dir="data"):
    """
    Simulates capturing a frame from a camera.
    Returns:
        str: Path to a simulated image file.
    """
    if not os.path.exists(data_dir):
        print(f"Error: Data directory '{data_dir}' not found.")
        return None

    images = [f for f in os.listdir(data_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not images:
        print("Error: No images found in data directory.")
        return None
    
    selected_image = random.choice(images)
    return os.path.join(data_dir, selected_image)

if __name__ == "__main__":
    print(f"Captured frame: {get_camera_frame()}")
