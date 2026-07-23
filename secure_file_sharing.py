import os
import shutil
import hashlib

UPLOAD_FOLDER = "SecureStorage"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

USERNAME = "admin"
PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

print("=" * 40)
print(" Secure File Sharing System ")
print("=" * 40)

username = input("Username: ")
password = input("Password: ")

entered_hash = hashlib.sha256(password.encode()).hexdigest()

if username == USERNAME and entered_hash == PASSWORD_HASH:

    print("\nLogin Successful!")

    print("\n1. Upload File")
    print("2. View Uploaded Files")

    choice = input("Choose Option: ")

    if choice == "1":

        path = input("Enter File Path: ")

        if os.path.exists(path):

            filename = os.path.basename(path)

            destination = os.path.join(UPLOAD_FOLDER, filename)

            shutil.copy(path, destination)

            print("\nFile Uploaded Successfully!")

        else:
            print("\nFile Not Found!")

    elif choice == "2":

        files = os.listdir(UPLOAD_FOLDER)

        if len(files) == 0:
            print("\nNo files uploaded.")

        else:

            print("\nUploaded Files:")

            for file in files:
                print("-", file)

else:
    print("\nInvalid Login")