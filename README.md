# Notes

## Executing Locally

### Create Virtual Env

    cd ~/Documents/code/microservices
    python3 -m venv env

### From Shell

    cd ~/Documents/code/microservices
    source env/bin/activate
    export FLASK_APP=api/project/__init__.py
    export FLASK_ENV=development
    export APP_SETTINGS=project.config.DevelopmentConfig
    python api/manage.py run

### Using vscode

Hit F5 and choose 'Python: Flask [DEV]'

#### launcher settings

    {
        "name": "Python: Flask [DEV]",
        "type": "python",
        "request": "launch",
        "module": "flask",
        "env": {
            "FLASK_APP": "api/project/__init__.py",
            "FLASK_ENV": "development",
            "APP_SETTINGS": "project.config.DevelopmentConfig"
        },
        "program": "${workspaceFolder}/api/manage.py",
        "args": [
            "run",
            "--no-debugger",
            "--no-reload"
        ]
    }

#### Docker 

Start it:

    docker-compose -f docker-compose-dev.yml up -d

Rebuild it:

    docker-compose -f docker-compose-dev.yml up -d --build

View logs in real-time:

    docker-compose -f docker-compose-dev.yml logs

Run unit tests:

    docker-compose -f docker-compose-dev.yml run api python manage.py test

# Resources

## Microservices Tutorial
https://testdriven.io/part-one-getting-started

## Flask Tutorial on vscode
https://code.visualstudio.com/docs/python/tutorial-flask

## Docker on Ubuntu
https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1
https://docs.docker.com/install/linux/linux-postinstall/