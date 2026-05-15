# News Pipeline using AWS, Lambda, Docker & Streamlit

A cloud-based news data pipeline that fetches real-time news articles using NewsAPI, stores them in PostgreSQL (Amazon RDS), uploads raw JSON data to Amazon S3, and visualizes the processed data through a Streamlit dashboard deployed using Docker and Amazon ECS Fargate.

---

## Features

- Fetches real-time news articles using NewsAPI
- Stores raw news data in Amazon S3
- Inserts processed articles into PostgreSQL (Amazon RDS)
- Serverless ingestion using AWS Lambda
- Interactive dashboard built with Streamlit
- Containerized using Docker
- Deployed on Amazon ECS Fargate

---

## Tech Stack

### Backend & Processing
- Python
- AWS Lambda
- NewsAPI
- pg8000

### Cloud Services
- Amazon S3
- Amazon RDS (PostgreSQL)
- Amazon ECS Fargate
- Amazon ECR

### Dashboard
- Streamlit
- Pandas
- Matplotlib

### DevOps & Deployment
- Docker
- GitHub

---

## Architecture

![Architecture Diagram](docs/architecture-diagram.png)

---

## Dashboard Preview

![Dashboard](screenshots/dashboard-ui.png)

---

## Project Structure

```bash
NEWS-PIPELINE/
│
├── dashboard/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── lambda_function/
│   └── lambda_function.py
│
├── raw_news/
├── docs/
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Workflow

1. AWS Lambda fetches news articles from NewsAPI
2. Raw JSON data is uploaded to Amazon S3
3. Processed records are inserted into PostgreSQL (Amazon RDS)
4. Streamlit dashboard reads data from RDS
5. Dashboard is containerized using Docker
6. Docker image is deployed on Amazon ECS Fargate

---

## Running the Dashboard Locally

```bash
cd dashboard
docker build -t news-dashboard .
docker run -p 8501:8501 news-dashboard
```

Open:

```text
http://localhost:8501
```

---

## Future Improvements

- Add sentiment analysis
- Schedule Lambda using EventBridge
- Add CI/CD pipeline
- Deploy dashboard using custom domain
- Add analytics and filters

---

## Author

Sreelakshmi TK