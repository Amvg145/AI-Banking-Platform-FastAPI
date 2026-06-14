# 🏦 AI Banking Platform

A Banking Backend System built using FastAPI, PostgreSQL, SQLAlchemy ORM, and JWT Authentication.

This project simulates real-world banking operations such as user registration, login, account creation, deposits, withdrawals, fund transfers, and transaction history management.

---

## 🚀 Tech Stack

### Backend
- FastAPI
- Python 3.12

### Database
- PostgreSQL

### ORM
- SQLAlchemy

### Authentication
- JWT (JSON Web Token)
- Passlib (Password Hashing)

### API Documentation
- Swagger UI
- OpenAPI

---

## 📂 Project Structure

backend/
│
├── app/
│ ├── api/
│ ├── services/
│ ├── models/
│ ├── schemas/
│ ├── database/
│ ├── core/
│ └── main.py
│
├── requirements.txt
├── .env
└── README.md

---

## ✨ Features Implemented

### User Management

- User Registration
- User Login
- Password Hashing
- JWT Token Generation

### Account Management

- Create Savings Account
- Auto Account Number Generation
- Account Status Tracking

### Transactions

- Deposit Money
- Withdraw Money
- Fund Transfer
- Transaction History

---

## Database Tables

### Users

| Column | Type |
|----------|----------|
| id | Integer |
| full_name | String |
| email | String |
| password_hash | String |
| created_at | DateTime |

### Accounts

| Column | Type |
|----------|----------|
| id | Integer |
| user_id | Integer |
| account_number | String |
| account_type | String |
| balance | Float |
| status | String |
| created_at | DateTime |

### Transactions

| Column | Type |
|----------|----------|
| id | Integer |
| account_id | Integer |
| transaction_type | String |
| amount | Float |
| balance_after_transaction | Float |
| description | String |
| created_at | DateTime |

---

## API Endpoints

### Authentication

| Method | Endpoint |
|----------|----------|
| GET | /api/auth/health |
| POST | /api/auth/register |
| POST | /api/auth/login |

### Accounts

| Method | Endpoint |
|----------|----------|
| POST | /api/accounts/create |

### Transactions

| Method | Endpoint |
|----------|----------|
| POST | /api/transactions/deposit |
| POST | /api/transactions/withdraw |
| POST | /api/transactions/transfer |
| GET | /api/transactions/transactions/{account_number} |

---

## Running the Project

### Clone Repository

git clone <repository-url>

cd ai-banking-platform/backend

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file:

DATABASE_URL=postgresql://postgres:password@localhost:5432/banking_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

### Create Tables

python -m app.database.create_tables

### Start Server

uvicorn app.main:app --reload

---

## Swagger Documentation

Open:

http://127.0.0.1:8000/docs

---

## Future Enhancements

- JWT Protected Routes
- User-specific Accounts
- Current Accounts
- Loan Management
- Fixed Deposits
- AI Fraud Detection
- Email Notifications
- Docker Deployment
- CI/CD Pipeline
- Unit Testing
- Integration Testing

---

## Author

Veerana Gouda

Software Development Engineer in Test (SDET)

Python | FastAPI | PostgreSQL | Automation Testing