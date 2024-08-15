![Tests](https://github.com/DonMohamed/Practice/actions/workflows/actionspy.yml/badge.svg)

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
pip install -r requirements.txt
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
echo $PASSWORD | docker login -u mredaammer --password-stdin
docker push mredaammer/practice --all-tags
``` 
3. Pull And Run from DockerHub Repositories 
```bash
docker pull mredaammer/practice
docker run -p8080:8080 mredaammer/practice
```
## Using Github Actions 
 > writing flow using yml language 
 1. the yaml file should be in path of `.github/workflows/file.yml`

 2. check the flows which is written in this path `.github/workflows/actionspy.yml`

 ## Using Ansible
 > For configuring existing infrastructure local or remote which sync desiered state with actual sate
 1. `main.yml` file for  pull image from docker hub on EC2 instances and run container from image
 2. `stop_container_remove_Image.yml` file For stop and remove container and also remove image 

 3. this command for run ansible playbook
  - note `ansible-playbook` name of file you need to run
  - note `-vvv` provide more detailed output, helping you diagnose where the issue lies
  - note `-i hosts.ini` for inventory file which have EC2 instance IPs
  
 ```bash
  ansible-playbook -vvv main.yml
  ansible-playbook -i hosts.ini main.yml -vvv

  ```
  ## Using Terraform 
  > Is used For provision and manage infrastructure across various cloud providers and on-premises environments.
  1. this commands for run terraform file 
   
   ```bash
   cd ./.terraform
   terraform init
   terraform apply
   terraform Destroy 
   ```
   - note `terraform Destroy` for destroy provisined insatnces 

