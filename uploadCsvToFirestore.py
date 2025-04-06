import csv
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with a service account key file
cred = credentials.Certificate('./serviceAccountKey.json')  # Replace with the path to your service account key file
firebase_admin.initialize_app(cred)

db = firestore.client()

# Path to the CSV file
csv_file_path = './FAQdata.csv'

# Firestore collection name
collection_name = 'FAQs'

# Parse CSV and upload to Firestore
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            db.collection(collection_name).add(row)
            print(f'Uploaded: {row}')
        except Exception as e:
            print(f'Error uploading: {row}, Error: {e}')

# Add the specific question and answer to Firestore
mba_hod_data = {
    "Question": "MBA HOD",
    "Answer": "HOD: Dr. S. Manikanta Professor & HOD"
}
try:
    db.collection(collection_name).add(mba_hod_data)
    print(f'Uploaded: {mba_hod_data}')
except Exception as e:
    print(f'Error uploading: {mba_hod_data}, Error: {e}')

print('CSV file successfully processed and uploaded to Firestore.')
