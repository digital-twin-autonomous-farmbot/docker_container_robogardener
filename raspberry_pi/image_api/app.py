from flask import Flask, request
import os
import datetime
from pymongo import MongoClient
import gridfs

app = Flask(__name__)

mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client["plant_images"]
fs = gridfs.GridFS(db)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    metadata = {
        "filename": file.filename,
        "content_type": file.content_type,
        "uploaded_at": datetime.datetime.utcnow()
    }

    file_id = fs.put(file, **metadata)
    return f"Saved with ID: {file_id}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
