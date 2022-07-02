# inventory-api

API for inventory app

## Setup for Development

Clone the repository onto your local machine

### Install dependencies

```bash
pip install -r requirements.txt
```

### Setup your credentials

Setup a firebase project and download your own firebase key. Create a .env file and add in the necessary lines.

```shell
PROJECT_ID=<your project id>
FIREBASE_KEY=<your firebase private key>
FIREBASE_KEY=<your service accounts email>
```

### Run the server

```bash
uvicorn main:app --reload
```