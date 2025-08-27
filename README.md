# ObservaSec 🚀  
**Secure CI/CD & Centralized Observability Platform with GitLab, GitHub, ELK, and Kubernetes**

---

## 📌 Overview
**LogShield** is a DevSecOps reference project that integrates:

- **Source Control**: GitHub for code hosting.  
- **CI/CD**: GitLab pipelines with security scans and automated deployments.  
- **Deployment**: Kubernetes (kind/minikube) for container orchestration.  
- **Observability**: ELK Stack (Elasticsearch, Logstash/Filebeat, Kibana) for centralized logging.  
- **Security**: Bandit (SAST), Trivy (container scan), Gitleaks (secret detection).  

This project demonstrates a **production-style DevSecOps pipeline** — from code commit to deployment, with built-in security and observability.

---

## 🏗️ Architecture

```mermaid
flowchart LR
    Dev[Developer] -->|Push Code| GH[GitHub Repo]
    GH -->|Webhook/Mirror| GL[GitLab CI/CD]
    
    subgraph CI/CD Pipeline
      GL --> SAST[Bandit SAST Scan]
      GL --> Secrets[Gitleaks Secret Scan]
      GL --> Trivy[Trivy Image Scan]
      GL --> Build[Docker Build & Push]
      GL --> Deploy[K8s Deployment via kubectl]
    end
    
    Deploy --> K8s[(Kubernetes Cluster)]
    K8s --> AppPod[Flask App Pods]
    
    subgraph ELK
      Filebeat[Filebeat DaemonSet] --> ES[Elasticsearch]
      ES --> Kibana[Kibana Dashboard]
    end
    
    AppPod -->|Logs| Filebeat
