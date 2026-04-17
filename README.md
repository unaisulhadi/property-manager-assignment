# Property Manager API

This project is a Django REST API for managing properties, members, contracts, and authentication.

## Prerequisites

Before starting, make sure you have:

- Python 3.10+ installed
- PostgreSQL installed and running
- A PostgreSQL database created for this project

This application uses PostgreSQL as its primary database backend.

## Setup From Scratch

### 1) Clone and enter the project

```bash
git clone <your-repo-url>
cd property-manager-hmlet
```

### 2) Create and activate a virtual environment

On Windows (PowerShell):

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Create `.env` file

Copy `.env.sample` into `.env` and fill in real values:

```bash
cp .env.sample .env
```

If `cp` is not available on Windows, create `.env` manually and add:

```env
# Database
DB_HOST=localhost
DB_NAME=property_manager
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432

# Django
SECRET_KEY=your_secret_key
ENV=local
```

### 5) Run migrations

```bash
python manage.py migrate
```

### 6) Start the development server

```bash
python manage.py runserver
```

The API will run at: `http://127.0.0.1:8000/`

## Why this project uses 4 apps

We split the code into 4 domain-focused apps to keep things simple, maintainable, and easier to reason about:

- `account`: Handles authentication and user-related logic
- `property`: Handles property-specific data and operations
- `member`: Handles member/tenant-related logic
- `contract`: Handles contract and agreement workflows

This domain-oriented structure gives better separation of concerns. Each app has a clear responsibility, which makes development faster, testing easier, and future changes safer.

## API Documentation (Swagger)

After running the server, open Swagger UI at:

- `http://127.0.0.1:8000/swagger/`

Other docs endpoints:

- ReDoc: `http://127.0.0.1:8000/redoc/`
- OpenAPI JSON: `http://127.0.0.1:8000/swagger.json`
