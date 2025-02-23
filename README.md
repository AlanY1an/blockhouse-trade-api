# Trade API

## Overview

The **Trade API** is a backend service built with **FastAPI** to manage trade orders. It supports **creating orders**, **retrieving orders**, and **storing data** in a **PostgreSQL** database. The application is containerized using **Docker** and deployed on an **AWS EC2** instance.

## Features

- **POST /orders**: Accepts trade order details (symbol, price, quantity, order type) and creates a new order.
- **GET /orders**: Retrieves a list of all submitted orders.
- **Database**: The API stores order data in a **PostgreSQL** database.
- **Deployment**: The application is containerized using **Docker** and deployed on **AWS EC2**.

## Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **PostgreSQL**: A powerful, open-source relational database system.
- **Docker**: A platform used for developing, shipping, and running applications in containers.
- **AWS EC2**: A scalable cloud computing service from Amazon Web Services to host the application.
- **GitHub Actions**: A CI/CD platform to automate testing and deployment processes.

## Requirements

Before running the application, make sure you have the following installed:

- Python 3.9+
- Docker
- PostgreSQL (or use AWS RDS for production)
- AWS EC2 (for deployment)

## API Documentation
You can access the auto-generated API documentation:

Swagger UI: http://3.137.178.53/docs
ReDoc: http://3.137.178.53/redoc


## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AlanY1an/blockhouse-trade-api.git
cd blockhouse-trade-api
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
# or
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Make sure you have a PostgreSQL database running. Update the database connection URL in the application with your database credentials.

### 5. Run the Application Locally

To start the application locally:

```bash
uvicorn app.main:app --reload
```

You can now access the API at `http://127.0.0.1:8000`.

### 6. Docker Setup

To containerize the application using Docker, you can build and run it with:

```bash
docker build -t trade-api .
docker run -d -p 8000:8000 trade-api
```

### 7. Deploy to AWS EC2

1. **Launch an EC2 instance** (Ubuntu recommended) on AWS.
2. **Install Docker** and **PostgreSQL** on the EC2 instance.
3. **Transfer the code** to the EC2 instance and run the Docker container.

```bash
scp -i /path/to/your/key.pem -r . ubuntu@<ec2-public-ip>:~/blockhouse-trade-api
ssh -i /path/to/your/key.pem ubuntu@<ec2-public-ip>
cd blockhouse-trade-api
docker build -t trade-api .
docker run -d -p 80:8000 trade-api
```

### 8. Configure GitHub Actions for CI/CD

Set up a GitHub Actions workflow to automate testing and deployment on push to the `main` branch. This can be done by adding a `.github/workflows/deploy.yml` file in the repository.

