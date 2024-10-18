## To run the application 
- Clone the repo
- Run the following commands <br>
`docker build -t my-fastapi-app .` <br>
`docker run -d --name my-fastapi-container -p 8000:8000 my-fastapi-app`
- The application should now be running in a Docker container at `http://127.0.0.1:8000`
- You can also access docs at `http://127.0.0.1:8000/docs`
- To stop the docker run `docker stop my-fastapi-container`
- To remove docker image run <br> 
`docker rm my-fastapi-container` <br>
`docker rmi my-fastapi-app` 
