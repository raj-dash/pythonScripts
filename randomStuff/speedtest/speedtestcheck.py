import speedtest as st
import sys
from datetime import datetime

# getting current date
cur_date = str(datetime.now())

# setting up server variable
try:
    server = st.Speedtest()
except:
    print("Error, fix yo access")
    sys.exit()


# finding best server
server.get_best_server()

# Test ping

ping = server.results.ping
pingString = f"Ping: {round(ping)} ms"

print(pingString)

# Test download speed
download = server.download()
download /= 10 ** 6
downloadString = f"Download Speed: {round(download, 2)} MB/s"

print(downloadString)

# Test upload speed

upload = server.upload()
upload /= 10 ** 6
uploadString = f"Upload Speed: {round(upload, 2)} MB/s"

print(uploadString)

log_path = r"C:\Users\rajar\OneDrive\Coding\Python\Scripts\randomStuff\speedtest\speedlog.txt"

try:
    with open(log_path, "a") as f:
        f.write(cur_date + "\n\n")
        f.writelines([pingString + "\n", downloadString + "\n", uploadString + "\n"])
        line = "-" * 50
        f.write("\n" + line + "\n\n")
except IOError:
    print("Failed to open log file")


