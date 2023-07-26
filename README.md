# FastAPI File Upload Project

This project provides a FastAPI application for uploading files to a server. The server organizes the files by date and provides an API endpoint to get a tree view of the stored files.

## Features

- Upload files to the server
- Stores uploaded files in a directory specified by the current date
- Retrieve a tree structure of the uploaded files including file names, last modified times and file extensions
- Each file saved with a timestamp down to the millisecond, ensuring uniqueness

## Setting Up

Before starting, make sure you have Python 3.6 or later and Pip installed. If not, you can download them from [here](https://www.python.org/downloads/).

Follow these steps to set up the project:

1. **Clone the repository**

    ```bash
    git clone https://github.com/znu/fastapi-upload.git
    cd fastapi-upload
    ```

2. **Create a virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```bash
    pip install fastapi uvicorn
    ```

4. **Run the application**

    ```bash
    uvicorn main:app --reload
    ```

Once the server is running, you can access the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

## Usage

- To upload a file, make a POST request to `/files/` with the file included in the request body.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/files/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@vue.min.js'
```

- To get a tree structure of the stored files, make a GET request to `/files/`.

## Contribution

We welcome contributions from everyone. Please see the CONTRIBUTING file for help getting started.
