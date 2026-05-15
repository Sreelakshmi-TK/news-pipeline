# News Pipeline on AWS

An end-to-end cloud-based news data pipeline built using AWS services, Python, Docker, and Streamlit.

This project fetches real-time news articles from NewsAPI, processes the data using AWS Lambda, stores raw JSON data in Amazon S3, saves structured records in PostgreSQL (Amazon RDS), and visualizes the news through a Streamlit dashboard deployed on Amazon ECS Fargate.

The project demonstrates practical implementation of serverless computing, containerization, cloud storage, database integration, and dashboard deployment in AWS.

---

# Architecture Diagram

![Architecture](docs/architecture.png)

---

# Project Overview

The pipeline performs the following workflow:

1. AWS Lambda fetches real-time news data from NewsAPI
2. Raw JSON responses are stored in Amazon S3
3. Processed news articles are inserted into PostgreSQL hosted on Amazon RDS
4. A Streamlit dashboard reads the stored data
5. The dashboard is containerized using Docker
6. Docker image is deployed to Amazon ECS Fargate using Amazon ECR

---

# Tech Stack

## Programming Language
- Python

## Cloud Services
- AWS Lambda
- Amazon S3
- Amazon RDS PostgreSQL
- Amazon ECS Fargate
- Amazon ECR
- CloudWatch

## Libraries and Frameworks
- Streamlit
- Pandas
- Requests
- pg8000
- Boto3

## DevOps Tools
- Docker
- Git
- GitHub

---

# Features

- Automated real-time news ingestion
- Serverless data processing with AWS Lambda
- Cloud storage using Amazon S3
- PostgreSQL database integration
- Containerized dashboard deployment
- ECS Fargate deployment
- Interactive Streamlit dashboard
- End-to-end AWS integration

---

# AWS Architecture Components

| AWS Service | Purpose |
|---|---|
| AWS Lambda | Fetch and process news data |
| Amazon S3 | Store raw JSON news files |
| Amazon RDS PostgreSQL | Store structured news records |
| Amazon ECS Fargate | Run Streamlit dashboard containers |
| Amazon ECR | Store Docker images |
| CloudWatch | Logging and monitoring |

---

# Project Structure

```bash
news-pipeline/
│
├── dashboard/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── lambda_function/
│   └── lambda_function.py
│
├── docs/
│   └── architecture.png
│
├── screenshots/
│   ├── lambda-success.png
│   ├── ecs-cluster.png
│   ├── ecs-task.png
│   ├── dashboard-home.png
│   ├── s3-bucket.png
│   └── rds-instance.png
│
├── requirements.txt
├── README.md
└── .gitignore