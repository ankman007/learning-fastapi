## Prerequisites
Before you begin, ensure that you have the following installed on your system:
- [Git](https://git-scm.com/)
- [Docker](https://docs.docker.com/get-docker/)

## Steps to Run the Application
- **Clone the repository:**
   Open your terminal or command prompt and clone the repository by running:
   <br>`git clone https://github.com/ankman007/learning-fastapi`
   <br>`cd <repository-directory>`

- **Build the Docker image:** Use Docker to build the FastAPI application image by running the following command:
<br>`docker build -t my-fastapi-app .`
<br>This command will create a Docker image tagged as my-fastapi-app.

- **Run the Docker container:** Start the container in detached mode (running in the background) and map port 8000 to your local machine by running:
<br>`docker run -d --name my-fastapi-container -p 8000:8000 my-fastapi-app`
<br>The FastAPI application will now be running inside a Docker container, accessible at `http://127.0.0.1:8000`

- **Access the API documentation:** FastAPI provides interactive API docs using Swagger UI. You can access it at:
<br>`http://127.0.0.1:8000/docs`

- **Stop the Docker container:** To stop the running Docker container, use the following command:
<br>`docker stop my-fastapi-container`

- **Remove the Docker container and image (optional):** If you want to remove the container and image after stopping it, run the following commands:
<br>`docker rm my-fastapi-container  # Remove the container`
<br>`docker rmi my-fastapi-app       # Remove the Docker image`

## Additional Information
- **To restart the application, you can either run the docker run command again, or start the existing container with:**
<br>`docker start my-fastapi-container`
- **If you make changes to your application code and want those to reflect in the Docker container, you’ll need to rebuild the image:**
<br>`docker build -t my-fastapi-app .`




