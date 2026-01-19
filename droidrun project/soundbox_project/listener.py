import time
import requests
import re
import sys

MOCK_MODE = False 

try:
    if not MOCK_MODE:
        from droidrun.agent.droid import DroidAgent
        agent = DroidAgent(goal="Monitor notifications for payment alerts")
        print("Connected to Android Device")
except ImportError:
    print("DroidRun library not found. Switching to MOCK MODE.")
    MOCK_MODE = True
except Exception as e:
    print(f"Connection failed ({e}). Switching to MOCK MODE.")
    MOCK_MODE = True

def run_listener():
    print("Soundbox Listener Started...")
    
    PATTERN = r"(?:Received|Paid)\s+(?:Rs\.?|₹)\s*([\d\.]+)\s+(?:from|by)\s+([A-Za-z ]+)"

    while True:
        try:
            if MOCK_MODE:
                print("\nSimulating a payment (waiting 10s)...")
                time.sleep(10)

                ui_text = "Notification: Received ₹50.00 from Test Customer via PhonePe"
            else:
               
                agent.adb.shell("cmd statusbar expand-notifications")
                time.sleep(2) 
               
                ui_text = agent.get_screen_text()
          
                agent.adb.shell("cmd statusbar collapse")

            matches = re.findall(PATTERN, ui_text, re.IGNORECASE)

            if matches:
                for amount, sender in matches:
                    print(f"Detected: ₹{amount} from {sender}")
                    
                    payload = {
                        "sender": sender.strip(),
                        "amount": amount,
                        "time_key": time.time() 
                    }
                    
                    try:
                        resp = requests.post("http://127.0.0.1:8000/api/log/", json=payload)
                        if resp.status_code == 200:
                            print("Sent to Soundbox")
                        else:
                            print("Duplicate or Error")
                    except Exception as e:
                        print(f"Server Error: {e}")

            if not MOCK_MODE:
                time.sleep(3)

        except KeyboardInterrupt:
            print("Stopped.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_listener()