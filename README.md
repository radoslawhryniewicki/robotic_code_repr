# Robotic Code Representation

This simple web application was created as a recruitment task. It contains two open endpoints to store commands and get robotic code representation (RCR) from given command

1. POST Method `/commands/` - store commands in temporary memory
    Example Request Body:
    ```
    {
        "commands": ["UP", "DOWN", "DOWN"]
    }
    ```

2. GET Method `/rcrs/{SINGLE_COMMAND}` - retrieve RCR from specific SINGLE_COMMAND
    Example Response Body:
    ```
    {
        "rcr": "001"
    }
    ```

The web app was deployed on Azure at website: 
https://rcrwebapp.azurewebsites.net/

## Run app without docker
To run the application on your local machine, first copy the repo and create a virtual environment using poetry tool. All necessary informations are located on official poetry webpage: https://python-poetry.org/

Once you installed the poetry, run:

`poetry install`

and inside the project run an uvicorn command:

`uvicorn app.main:app`

An app should be available at `0.0.0.0:8000` 

## Run containerized app
To build an app execute the command below:

`docker build -t rcr_project .`

Once the build has been ended, run the image as a container:

`docker run --publish 80:80 rcr_project`

The docker container has been exposed at port 80.

## Tests running
To run the unit tests simply run:

`python -m pytest tests/`



