import time
import sensor_simulation
import camera_simulation
import alert_system
from ai_inference import AIInference

def main():
    print("Initializing Intelligent Security System Simulation...")
    
    # Initialize AI
    try:
        ai = AIInference()
    except Exception as e:
        print(f"Failed to initialize AI: {e}")
        return

    print("System Armed. Monitoring...")
    
    try:
        while True:
            # 1. Check Sensor
            pir_status = sensor_simulation.generate_pir_signal()
            
            if pir_status == 1:
                print("\n[MOTION DETECTED] PIR Sensor triggered!")
                
                # 2. Activate Camera
                image_path = camera_simulation.get_camera_frame()
                if image_path:
                    print(f"Capturing image: {image_path}")
                    
                    # 3. AI Analysis
                    is_person, details = ai.detect_person(image_path)
                    print(f"AI Analysis Result: {details}")
                    
                    if is_person:
                        # 4. Trigger Alert
                        alert_system.trigger_alert(f"Person detected in {image_path}!")
                    else:
                        print("No person detected. False alarm.")
                else:
                    print("Camera failed to capture image.")
            else:
                print(".", end="", flush=True)
            
            time.sleep(2) # Wait before next check

    except KeyboardInterrupt:
        print("\nSystem Disarmed. Exiting.")

if __name__ == "__main__":
    main()
