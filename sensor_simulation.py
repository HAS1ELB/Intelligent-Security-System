import random
import time

def generate_pir_signal():
    """
    Simulates a PIR sensor.
    Returns:
        int: 1 if motion detected, 0 otherwise.
    """
    # Simulate random motion with 30% probability
    if random.random() < 0.3:
        return 1
    return 0

if __name__ == "__main__":
    while True:
        print(f"PIR Signal: {generate_pir_signal()}")
        time.sleep(1)
