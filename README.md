Zemoga test
## Table of Contents:
- [Description](#description)
  - [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Using docker](#with-docker)
  - [Normal](#without-docker)
- [Usage](#run-it-locally)


## Description
This is a simple portfolio web.

### Features
Features included:
- Data modeling with pydantic.
- Data validation.
- CRUD of users.
- FastAPI Router

## Requirements:
- Python >= 3.6
- Docker (Optionally)

## Installation
1. Clone or download de repository:
    ```
    $ git clone https://github.com/EmilRueda/zemoga_test.git
    ```

2. Open the console inside the project directory and create a virtual environment (You can skip this step if you have docker installed).
    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

3. Install the app (You can skip this step if you have docker installed)
    ```bash
    (venv) $ pip install -r requirements.txt
    ```
4. Find credentials folder in the project,
    and put the correct credentials for database and twitter API

### With docker
1. Run it with Docker.
```bash
 $ docker build -t zemoga_test .
 $ docker run -d --name container -p 8000:8000 zemoga_test
```
It will run in the localhost


### Without docker



2. In the project folder run in the command line.
```bash
$ python3 main.py
```

## Testing

For running the test file type in the command line:
```bash
$ pytest -s --no-header -rA -vv --cov --cov-branch 
```

## Swagger UI documentation
For seeing the Swagger UI documentation when main.py is running in localhost
just go to (http://localhost:8000/docs).
