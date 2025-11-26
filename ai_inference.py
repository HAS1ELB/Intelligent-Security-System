from ultralytics import YOLO
import cv2

class AIInference:
    def __init__(self, model_path="yolov8n.pt"):
        print("Loading AI Model...")
        self.model = YOLO(model_path)
        print("Model loaded.")

    def detect_person(self, image_path):
        """
        Detects if a person is present in the image.
        Args:
            image_path (str): Path to the image.
        Returns:
            bool: True if person detected, False otherwise.
            list: List of detections (for logging).
        """
        results = self.model(image_path, verbose=False)
        
        person_detected = False
        detections = []

        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = self.model.names[cls]
                
                if label == "person" and conf > 0.5:
                    person_detected = True
                
                detections.append(f"{label} ({conf:.2f})")
        
        return person_detected, detections

if __name__ == "__main__":
    ai = AIInference()
    # Test with dummy data
    print(f"Testing empty: {ai.detect_person('data/empty_room.jpg')}")
    print(f"Testing person: {ai.detect_person('data/person_room.jpg')}")
