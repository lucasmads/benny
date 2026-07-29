# Permission System

A lightweight Role-Based Access Control (RBAC) application built with Python.

The project demonstrates how users, roles, and permissions can be managed in a modular architecture using local JSON storage. It is intended as a learning project and a solid starting point for building administrative tools or backend authorization systems.

---

## Features

- User management
- Role management
- Permission assignment
- Access validation
- Local JSON database
- Import and export functionality
- Audit log support
- Statistics overview
- Modular architecture
- Command-line interface

---

## Project Structure

```
permission-system/
├── config/
├── data/
├── docs/
├── src/
├── tests/
├── .github/
├── README.md
├── LICENSE
├── requirements.txt
└── pyproject.toml
```

---

## Requirements

- Python 3.11+
- pip

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/permission-system.git
```

Move into the project directory:

```bash
cd permission-system
```

Create a virtual environment (recommended):

```bash
python -m venv .venv
```

Activate the environment.

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python src/main.py
```

---

## Example Menu

```
1. Manage Users
2. Manage Roles
3. Manage Permissions
4. Check Access
5. Statistics
6. Export Data
7. Exit
```

---

## Data Storage

The application stores all information locally inside the `data/` directory.

Example files:

- users.json
- roles.json
- permissions.json
- audit_log.json

No external database is required.

---

## Testing

Run all tests:

```bash
pytest
```

---

## Continuous Integration

GitHub Actions automatically:

- install dependencies
- execute unit tests
- perform linting (optional)

---

## Project Architecture

```
CLI
    │
    ▼
Services
    │
    ▼
Managers
    │
    ▼
Repository
    │
    ▼
JSON Storage
```

---

## Future Improvements

- SQLite support
- PostgreSQL backend
- User authentication
- Password hashing
- REST API
- FastAPI integration
- JWT authentication
- YAML configuration
- Web dashboard
- Docker support
- Permission inheritance
- Audit report generation

---

## Technologies

- Python
- JSON
- Dataclasses
- Pytest
- GitHub Actions

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to open an issue or submit a pull request.

---

## Author

Developed as a portfolio project for learning Python architecture, RBAC concepts, and software design.
