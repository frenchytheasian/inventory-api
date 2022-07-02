import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from dotenv import load_dotenv

load_dotenv()

# Use the application default credentials
cred = credentials.Certificate({
    "type": "service_account",
    'project_id': os.getenv('PROJECT_ID'),
    "private_key": os.getenv('FIRESTORE_KEY').replace('\\n', '\n'),
    "client_email": os.getenv('FIRESTORE_EMAIL'),
    "token_uri": "https://oauth2.googleapis.com/token",
})
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('users').document('alovelace')
doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1815
})
