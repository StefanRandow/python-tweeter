import time
from datetime import datetime,timezone
import os



while True:
    now_utc = datetime.now(timezone.utc)
    if now_utc.minute == 00 or now_utc.minute == 30:
        
        if now_utc.hour == 12 and now_utc.minute == 30:
            os.system(r"forecast_tweet.py")
            time.sleep(1700)
            
        else:
            os.system(r"python tweeter.py")
            time.sleep(1700)
    else:
        time.sleep(59)
