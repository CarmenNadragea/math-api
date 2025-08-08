This repository contains a RESTful API developed using Flask, which provides several mathematical operations including exponentiation, factorial computation, and Fibonacci sequence evaluation. The application follows a modular architecture and integrates key cloud-native principles such as stateless authentication, asynchronous logging, and containerization.


The system offers the following core functionalities:

    JWT-based authentication for secure access control

    Kafka-based logging for capturing and publishing operational events

    Persistent storage of logs in a relational database

    Protected API endpoint for retrieving historical log data

Functional Capabilities

Mathematical Operations

    POST /api/power – Computes the result of raising a base number to a specified exponent

    POST /api/factorial – Calculates the factorial of a given non-negative integer

    POST /api/fibonacci – Returns the nth number in the Fibonacci sequence

Authentication Endpoint

    POST /login – Authenticates the user and returns a JWT token

        For demonstration purposes, the application uses a hardcoded credential pair:

            Username: admin

            Password: password

Kafka Logging Mechanism

Each mathematical request is asynchronously logged to Apache Kafka using a dedicated topic (api-logs). Each event is serialized as JSON and includes:

    The name of the operation performed

    The input parameters

    The resulting value

    A timestamp


Database Log Persistence

A Kafka consumer service is responsible for retrieving messages from the Kafka topic and storing them into a local SQL database, using SQLAlchemy as the ORM.
Secured Log Retrieval

    GET /logs – Returns all stored log entries in descending order by timestamp

        This endpoint is secured and requires a valid JWT token.

Containerization and Deployment

The application is designed to run in a Dockerized environment, using Docker Compose for orchestration. The system includes the following containers:

    math-api: the Flask-based API service

    kafka: Apache Kafka instance (Bitnami image)

    zookeeper: Zookeeper service required by Kafka
