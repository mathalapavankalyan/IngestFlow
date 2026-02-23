Serverless Data Ingestion Service

<p align="center"> <b>Cloud Native • Serverless • Scalable • Clean Architecture</b> </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue" /> <img src="https://img.shields.io/badge/FastAPI-Framework-green" /> <img src="https://img.shields.io/badge/AWS-Lambda-orange" /> <img src="https://img.shields.io/badge/Database-DynamoDB-blue" /> <img src="https://img.shields.io/badge/License-MIT-lightgrey" /> </p>

Overview



A lightweight serverless data ingestion API built with FastAPI, AWS Lambda, and DynamoDB.



This project demonstrates clean backend architecture with a layered design:



API → Service → Processor → Storage



Designed for scalability, maintainability, and minimal operational overhead.



Project Structure

data\_ingestion/

│

├── lambda\_handler.py        # AWS Lambda entry point

│

├── api/

│   └── routes.py            # FastAPI route definitions

│

├── core/

│   └── config.py            # Configuration management

│

├── models/

│   ├── request.py           # Request schemas

│   └── response.py          # Response schemas

│

├── services/

│   ├── ingestion\_service.py # Business logic layer

│   └── query\_service.py     # Query logic

│

├── processors/

│   └── file\_processor.py    # Data transformation logic

│

├── storage/

│   └── dynamodb.py          # DynamoDB integration layer

│

└── requirements.txt

Getting Started

<details> <summary><b>Clone and Setup</b></summary>

git clone https://github.com/your-username/your-repo.git

cd your-repo

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

</details>

<details> <summary><b>Run Locally</b></summary>

uvicorn api.routes:app --reload



Open your browser:



http://127.0.0.1:8000/docs



</details>

Deployment



This service is built for AWS Lambda.



Lambda handler:



lambda\_handler.lambda\_handler



You can deploy using:



AWS SAM



Serverless Framework



Terraform



Manual ZIP deployment



Architecture Principles



Clean separation of concerns



Serverless first approach



Modular design



DynamoDB backed persistence



Easily extensible



Future Improvements



Structured logging



Idempotency support



Observability and tracing



Retry handling strategy



CI/CD pipeline



License



Licensed under the MIT License.

