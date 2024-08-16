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
- for running the App
```bash
python3 toDoList.py 
          
```
- for Testing
```bash
pytest  

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
 > writing flow using yml language for createing CI/CD Pipline
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

  ## using Kubernetes 
  > Is used for  automating the deployment, scaling, and management of containerized applications.  
  1. Prerequisites
        - `Minikube`: Ensure Minikube is installed and running.
        - `kubectl`: Ensure kubectl is installed and configured to         interact with your Minikube cluster.
  2. note `fileManifest.ymal` it can be one of this files
        - `Namespace`: To organize your resources.
        - `Deployment`: To define the application's deployment.
        - `Service`: To expose your deployment internally.
        - `Ingress`: To expose your service externally.
        - `Roles and RoleBindings`: To manage permissions.

   
   ```bash
   minikube start
   kubectl apply -f fileManifest.yaml
   kubectl delete service/my-app-service
   kubectl delete deployment.apps/my-app-deployment

   ```
   - to make sure ngress addon is enabled into Minikube
   ```bash
   minikube addons enable ingress

   ```
   - to Check status
   ```bash
   kubectl get deployments -n my-app-namespace 

   ```
   - get runing url of app
   ``` bash
   minikube -n my-app-namespace service app-service --url
   
   ```
## Helm
> Is the package manager for K8s
```sh
 helm install my-chart app-deployment -n my-app --create-namespace
 helm -n my-app list
 helm uninstall my-chart -n my-app
```
## Monitoring
> use helm chart to monitor k8s
```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring

minikube addons enable metrics-server
```
- Access dashboards at http://localhost:3000/dashboards, default creds: admin:prom-operator , run next command before access grafana
```sh
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring

```

