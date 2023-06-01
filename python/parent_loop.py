import time
from datetime import datetime,timezone
import os



while True:
    now_utc = datetime.now(timezone.utc)
    if now_utc.minute == 00 or now_utc.minute == 30:
        os.system(r"python tweeter.py")
        time.sleep(1700)
    else:
        time.sleep(59)
        