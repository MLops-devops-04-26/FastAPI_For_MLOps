# 4. Dockerization



To make our application portable and easy to deploy, we'll containerize it using Docker. Docker allows us to package our application with all of its dependencies into a standardized unit for software development.

## The `Dockerfile`

The `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image. Here's what our `Dockerfile` does:

1.  **`FROM python:3.9`**: We start with an official Python 3.9 base image.
2.  **`WORKDIR /app`**: We set the working directory inside the container to `/app`.
3.  **`COPY requirements.txt .`**: We copy the `requirements.txt` file into the container.
4.  **`RUN pip install ...`**: We install the Python dependencies.
5.  **`COPY . .`**: We copy the rest of our application code into the container.
6.  **`CMD ["uvicorn", ...]`**: We specify the command to run when the container starts.

## The `.dockerignore` File

This file is similar to `.gitignore`. It lists files and directories that we want to exclude from the Docker image. This helps to keep our image small and to avoid accidentally leaking sensitive information.

## Building and Running the Container

You can build the Docker image with:
```bash
docker build -t house-price-predictor .
```

And run it with:
```bash
docker run -p 80:80 house-price-predictor
```

