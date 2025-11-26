import datetime

def trigger_alert(details):
    """
    Triggers an alert.
    Args:
        details (str): Description of the alert.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_message = f"[{timestamp}] ALERT: {details}"
    
    print("\033[91m" + alert_message + "\033[0m")  # Print in red
    
    with open("alerts.log", "a") as f:
        f.write(alert_message + "\n")

if __name__ == "__main__":
    trigger_alert("Test Alert")
