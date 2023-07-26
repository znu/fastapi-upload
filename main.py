from fastapi import FastAPI, UploadFile, File
from datetime import datetime
import os
import uuid
from typing import Dict, List

app = FastAPI()

def get_file_info(path: str, filename: str) -> Dict[str, str]:
    """
    Get information about a file
    """
    file_path = os.path.join(path, filename)
    file_info = os.stat(file_path)

    # Get file extension
    file_ext = os.path.splitext(filename)[1]
    if file_ext == '':
        file_ext = 'unknown'

    return {
        "filename": filename,
        "last_modified": datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        "extension": file_ext
    }


@app.get("/files/")
async def get_files_tree() -> Dict[str, List[Dict[str, str]]]:
    base_path = './uploads'
    files_tree = {}
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            files_tree[folder] = [get_file_info(folder_path, f) for f in os.listdir(folder_path)]
    return files_tree

@app.post("/files/")
async def create_upload_file(file: UploadFile):
    try:
        # Create a directory named with today's date
        date_today = datetime.now().strftime('%Y-%m-%d')
        directory = f'./uploads/{date_today}'

        if not os.path.exists(directory):
            os.makedirs(directory)

        # Save the file with the date and time included in the filename
        date_time_now = datetime.now().strftime('%H%M%S%f')
        filename = f"{date_time_now}_{file.filename}"
        file_location = f"{directory}/{filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
            
        return {"info": f"file '{filename}' saved at {directory}"}
        
    except Exception as e:
        return {"error": str(e)}
