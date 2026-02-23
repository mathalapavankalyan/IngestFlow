<p align="center"> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=Serverless+Data+Ingestion+Service;Built+with+FastAPI+%2B+AWS+Lambda;Clean+Architecture+%7C+Cloud+Native;Scalable+%7C+Modular+%7C+Production+Ready" /> </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white"/> <img src="https://img.shields.io/badge/AWS-Lambda-FF9900?logo=amazonaws&logoColor=white"/> <img src="https://img.shields.io/badge/DynamoDB-NoSQL-4053D6?logo=amazondynamodb&logoColor=white"/> <img src="https://img.shields.io/badge/License-MIT-black"/> </p>
Overview

A cloud native, serverless data ingestion API built using FastAPI and AWS Lambda.

This project demonstrates:

Clean layered backend architecture

Serverless deployment model

Scalable NoSQL persistence

Modular and maintainable Python design

Architecture flow:
                                                                API → Service → Processor → Storage
Architecture Diagram : 
                                                                             
                                                                                 
                                                                                    ┌───────────────┐
                                                                                    │   Client/API  │
                                                                                    └───────┬───────┘
                                                                                            │
                                                                                            ▼
                                                                                    ┌───────────────┐
                                                                                    │   FastAPI     │
                                                                                    │   (Routes)    │
                                                                                    └───────┬───────┘
                                                                                            │
                                                                                            ▼
                                                                                    ┌───────────────┐
                                                                                    │  Service      │
                                                                                    │  Layer        │
                                                                                    └───────┬───────┘
                                                                                            │
                                                                                            ▼
                                                                                    ┌───────────────┐
                                                                                    │  Processor    │
                                                                                    └───────┬───────┘
                                                                                            │
                                                                                            ▼
                                                                                    ┌───────────────┐
                                                                                    │  DynamoDB     │
                                                                                    └───────────────┘

  Project Structure : 

                                                                                    data_ingestion/
                                                                                  ├── lambda_handler.py
                                                                                  ├── api/
                                                                                  │   └── routes.py
                                                                                  ├── core/
                                                                                  │   └── config.py
                                                                                  ├── models/
                                                                                  │   ├── request.py
                                                                                  │   └── response.py
                                                                                  ├── services/
                                                                                  │   ├── ingestion_service.py
                                                                                  │   └── query_service.py
                                                                                  ├── processors/
                                                                                  │   └── file_processor.py
                                                                                  ├── storage/
                                                                                  │   └── dynamodb.py
                                                                                  └── requirements.txt


Getting Started

Clone and Setup : 

 >> git clone [https://github.com/your-username/your-repo.git](https://github.com/mathalapavankalyan/IngestFlow.git)
 >> cd your-repo
 >> python -m venv venv
 >> source venv/bin/activate
 >> pip install -r requirements.txt

Run Locally :
uvicorn api.routes:app --reload

Open in your browser : 

http://127.0.0.1:8000/docs

Deployment

Designed for AWS Lambda.

Lambda handler :

lambda_handler.lambda_handler

Deploy using:

                  AWS SAM
                  
                  Serverless Framework
                  
                  Terraform
                  
                  Manual ZIP deployment
                  
                  Key Design Principles
                  
                  Separation of concerns
                  
                  Modular architecture
                  
                  Serverless first design
                  
                  Clean DynamoDB integration
                  
                  Easy extensibility

Roadmap

                Structured logging
                
                Observability and tracing
                
                Idempotency support
                
                Retry handling strategy
                
                CI/CD automation
                
                Performance benchmarking
                
                Contributing
                
                Contributions are welcome.

To contribute:

                Fork the repository
                
                Create a feature branch
                
                Commit your changes
                
                Open a pull request

License

MIT License

You are free to use, modify, and distribute this software.


  
