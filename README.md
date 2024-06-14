# To-Do-List Application in Python using Flask

## Setting Up the Application

### Step 1: Clone the Repository

```sh
https://github.com/DonMohamed/Practice.git

```

### Step 2: Create a Virtual Environment

```bash
 python3 -m venv venv
 source venv/bin/activate
 ```

### Step 3: Install Requirements

```bash
pip install -r requirments.txt
```

### Step 4: Run App and Tests

```bash
python3 toDoList.py --> for running the App
pytest              --> for Testing
```

----------------------------------------
# Dockerization 
> Use Docker to Put my App in Container to Solve Problem that it was working for me .

## Docker 
> To Run Docker You Must install it from [Official site](https://docs.docker.com/engine/install/ubuntu/) Doucmentation to Be Able to use this Commands 

```bash
docker build -t practice .
docker run --rm -it -p8080:8080 practice
``` 
## Pushing Docker to Docker Hub Registry
1. Tage my build App 
> note that `mredaammer/practice`
1.  `mredaammer` is the user of DockerHub
2.  `practice`   is the repository on DockerHub
```bash
docker tag practice:latest mredaammer/practice
```
2. Push my Docker To DockerHub
```bash
docker login
docker push mredaammer/practice --all-tags
``` 
3. Pull And Run from DockerHub Repositories 
```bash
docker pull mredaammer/practice
docker run -p8080:8080 myusername/myapp
```
