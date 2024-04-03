https://www.youtube.com/watch?v=6OxqiEeCvMI

docker network ls
docker network inspect host
docker rm fastapi-container 
docker run --name fastapi-container -p 80:80 --network=host fastapi-image
docker run --name fastapi-container -p 80:80 --network=host -d fastapi-image
docker logs fastapi-container

docker run --name fastapi-container -p 80:80 --network=host -d -v $(pwd):/code fastapi-image

# FastAPI Application Deployment using Docker  [Docker YouTube Tutorial](https://www.youtube.com/watch?v=6OxqiEeCvMI)

## Introduction

This project demonstrates how to containerize and run a FastAPI application using Docker. By leveraging Docker, we ensure that the application runs consistently across different environments.

## Prerequisites

Before you begin, ensure you have Docker installed and running on your machine. If you haven't installed Docker, please refer to the [official Docker documentation](https://docs.docker.com/get-docker/) for installation instructions.

## Running the Application

To run the FastAPI application using Docker, follow these steps:

1. **List Docker Networks**: This step is optional but recommended to understand which networks are available in your Docker environment.
   ```bash
   docker network ls
   ```

2. **Inspect the Host Network**: Optionally, inspect the 'host' network to understand its configuration. This is useful for debugging network-related issues.
   ```bash
   docker network inspect host
   ```

3. **Remove Previous Container**: If you have previously run the FastAPI container, remove it to avoid naming conflicts.
   ```bash
   docker rm fastapi-container
   ```

4. **Run the Application**: Run your FastAPI application by creating a new container. You can do this in two modes:

   - **Foreground Mode**: Runs the container in the foreground. Use this mode for debugging purposes.
     ```bash
     docker run --name fastapi-container -p 80:80 --network=host fastapi-image
     ```

   - **Detached Mode**: Runs the container in the background. This mode is preferred for long-running applications.
     ```bash
     docker run --name fastapi-container -p 80:80 --network=host -d fastapi-image
     ```

   - **Detached Mode with Volume Mapping**: If you want to map your current directory to the `/code` directory inside the container (useful for development), use this command:
     ```bash
     docker run --name fastapi-container -p 80:80 --network=host -d -v $(pwd):/code fastapi-image
     ```

## Viewing Logs

To view the logs of the running FastAPI container, use the following command:

```bash
docker logs fastapi-container
```

## Conclusion

This README provides the necessary steps to containerize and run a FastAPI application using Docker. By following these instructions, you can ensure your application is running in a consistent and isolated environment.

