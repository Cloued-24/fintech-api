# Fintech Microservice Deployment System

    Technologies: Python, Flask, Docker, GitHub Actions, AWS ECR
    Type: CI/CD + Containerization Project

Project Description

    Built a production-ready payment processing API with complete containerization and automated CI/CD pipeline.
    The system handles user account creation, transaction simulation, and logging, with automated builds and deployments to AWS container registry.    

Technical Architecture

<img width="3434" height="574" alt="deepseek_mermaid_20260407_7450ca" src="https://github.com/user-attachments/assets/395cbd42-9d3c-4218-bbfa-d46003753e7e" />

# Features Implemented:

   Backend API (Flask)

    ✅ User account creation endpoint (POST /user)

    ✅ Transaction processing endpoint (POST /transaction)

    ✅ Health check endpoint (GET /health)

    ✅ In-memory transaction logging

    ✅ Real-time logging with timestamps

  Containerization (Docker)

    ✅ Multi-stage Dockerfile optimization

    ✅ Environment variable configuration

    ✅ Port mapping and networking

    ✅ Container health monitoring

  CI/CD Pipeline (GitHub Actions)

    ✅ Automated builds on every push

    ✅ AWS ECR authentication

    ✅ Docker image tagging and pushing

    ✅ Secrets management

Cloud Infrastructure (AWS)

    ✅ ECR repository creation

    ✅ IAM user configuration

    ✅ CLI integration

Project Structure

    fintech-api/
    ├── app.py                 # Flask application
    ├── Dockerfile            # Container configuration
    ├── requirements.txt      # Python dependencies
    ├── .gitignore           # Git exclusions
    ├── .github/
    │   └── workflows/
    │       └── deploy.yml    # CI/CD pipeline
    └── venv/                 # Virtual environment (excluded)

# Key Code Snippets:

  # Phase 1: Development
 
  <img width="1843" height="1080" alt="1" src="https://github.com/user-attachments/assets/eab2f1ba-7f28-4166-9c08-a6ba91cb70da" />

 <img width="1399" height="385" alt="2" src="https://github.com/user-attachments/assets/e0755032-f321-4c31-b3cc-a5eb9da174a6" />

 <img width="1214" height="473" alt="3" src="https://github.com/user-attachments/assets/6ed6ad43-48d4-4219-9cb6-ef21f1c3fef9" />
 

Summary of Phase 1: Developed a REST API with three endpoints: user creation, transaction processing, and health checks.

# Phase 2: Docker Containerization

<img width="1354" height="589" alt="4" src="https://github.com/user-attachments/assets/33869eda-f261-4fdd-aee2-203072ca34c1" />

<img width="1494" height="703" alt="5" src="https://github.com/user-attachments/assets/e28cde00-0410-4676-94a9-b8e5431b6e08" />

<img width="1718" height="675" alt="6a" src="https://github.com/user-attachments/assets/2ec18a61-8ddf-4c5b-9a16-8f2d55456a6a" />


Summary of Phase 2: Containerized the application using Docker, reducing deployment complexity and ensuring environment consistency.

# Phase 3: GitHub & Version Control

<img width="1191" height="663" alt="7" src="https://github.com/user-attachments/assets/46f9b245-a49d-4809-b9e3-5239885bcb64" />

<img width="1126" height="425" alt="8" src="https://github.com/user-attachments/assets/7c5b2116-a119-4c50-95f0-5160dc5d0c1e" />


Summary of Phase 3: Implemented Git version control and connected to GitHub for remote repository management.

# Phase 4: AWS ECR Integration

<img width="1504" height="804" alt="9a" src="https://github.com/user-attachments/assets/74cb44d0-b32c-4365-b251-f33764e06ca0" />


Summary of Phase 4: Integrated AWS Elastic Container Registry (ECR) to store Docker images in the cloud.

# Phase 5: CI/CD Pipeline 

<img width="1485" height="1002" alt="10 part1" src="https://github.com/user-attachments/assets/034ed251-1b9c-4d05-9322-1a71c08f995f" />

<img width="1649" height="737" alt="10 part2" src="https://github.com/user-attachments/assets/a719794d-e009-4cdf-b26e-67bc4289704c" />

<img width="1799" height="947" alt="11b" src="https://github.com/user-attachments/assets/db95d63e-57b4-49d2-bb60-6cec4b635a0f" /> 


Summary of Phase 5: Automated the entire build and deployment process using GitHub Actions CI/CD pipeline.


# Results

    ✅ 100% automated build process

    ✅ Containerized application ready for deployment

    ✅ CI/CD pipeline triggers on every git push

    ✅ Docker images stored securely in AWS ECR


    





