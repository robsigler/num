import time
import datetime
import csv
from concurrent.futures import ThreadPoolExecutor
import socket

def internet_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect(("8.8.8.8", 53))
        return True
    except socket.error:
        return False
    finally:
        sock.close()

def ping():
    timestamp = datetime.datetime.now().isoformat()
    print("Calling 8.8.8.8....")
    status = internet_connection()
    print("Call completed!")
    row = {'timestamp': timestamp, 'status': status}
    print(row)
    writer.writerow(row)

with open('uptime_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    with ThreadPoolExecutor(max_workers=4) as executor:
        while True:
            executor.submit(ping)
            time.sleep(15)