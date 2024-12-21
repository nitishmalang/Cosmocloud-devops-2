# DevOps Task 2 - FastAPI Backend with Redis

This repository contains the solution for **DevOps Task 2**, where the objective was to debug and deploy a FastAPI backend application with Redis using Helm charts on Kubernetes.

---

## Project Structure

devops-task-2-main/
├── backend-app/                  
│   ├── main.py                   
│   ├── Dockerfile                
│   ├── requirements.txt          
├── sample-helm-chart/            
│   ├── Chart.yaml                
│   ├── values.yaml              
│   └── templates/              
│       ├── backend-deployment.yaml  
│       ├── backend-service.yaml    
│       ├── redis-deployment.yaml   
│       └── redis-service.yaml       
---

## Steps to Run

###  Build and Push Docker Image**
Navigate to the `backend-app` folder:
```
docker build -t nitishmalang/backend-app:latest .
docker push nitishmalang/backend-app:latest
```

### Deploy with Helm
`helm lint .`

`helm install devops-task-2-main . --namespace default --create-namespace`

`kubectl port-forward svc/devops-task-2-main-backend 8080:8000 -n default`

### Test the API:

`curl http://localhost:8080`


### Features
FastAPI backend application
Redis integration to store and increment a hit counter
Kubernetes deployment using Helm






