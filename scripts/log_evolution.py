import datetime
import json
import os
import sys

LOG_FILE = os.path.join("proof", "evolution_log.jsonl")

def log_evolution(event, insight, action):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "event": event,
        "insight": insight,
        "action": action
    }
    
    # Ensure dir exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    
    print(f"✅ [Kaizen Memory] Logged event: {event}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python log_evolution.py <event> <insight> <action>")
        sys.exit(1)
        
    log_evolution(sys.argv[1], sys.argv[2], sys.argv[3])
