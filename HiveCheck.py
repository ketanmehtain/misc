import subprocess
import smtplib
from cryptography.fernet import Fernet

# Decrypt the username and password
with open(".credentials", "rb") as file:
    encrypted_username = file.readline().strip()
    encrypted_password = file.readline().strip()
    key = file.read()

# Create a new Fernet object with the key
fernet = Fernet(key)

decrypted_username = fernet.decrypt(encrypted_username).decode()
decrypted_password = fernet.decrypt(encrypted_password).decode()
#print(decrypted_username)

# Beeline command to check HiveServer2 status
beeline_cmd = f"beeline -u jdbc:hive2://"

# Execute beeline command to check status and get number of concurrent connections
try:
    process = subprocess.run(["beeline", "-u", "jdbc:hive2://", "-e", "show databases;"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output = process.stdout
    error = process.stderr
    with open("out.txt", "w") as f:
        f.write(output)
    status = "OK"
    print("OK")
except subprocess.CalledProcessError:
    status = "DOWN"
    print("Down")
