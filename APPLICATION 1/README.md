
# Rule Engine with AST

## Overview
This application is a 3-tier rule engine that uses **Abstract Syntax Trees (AST)** to evaluate dynamic rules based on user attributes like `age`, `department`, `salary`, `experience`, etc. The system allows for the creation, modification, combination, and evaluation of these rules. It uses **SQLite3** for data storage and is built using **Flask** for the API and backend.

## Features
- **AST-based Rule Representation**: Rules are parsed into ASTs, allowing dynamic rule creation and modification.
- **SQLite3 Integration**: Rules are stored and retrieved from a SQLite database.
- **API Design**: APIs are provided for rule creation, evaluation, update, and deletion.
- **Sample UI**: A simple HTML interface to submit rules and user data.

---

## Project Structure

```plaintext
rule_engine_app/
│
├── app.py                # Flask application for routing and APIs
├── ast_engine.py         # AST creation and evaluation logic
├── database/
│   ├── db.py             # SQLite3 database initialization and CRUD operations
│   └── rules.db          # SQLite3 database file
├── templates/
│   └── index.html        # Simple UI for rule submission and data evaluation
└── static/
    └── style.css         # Optional styling for the UI
```

---

## Requirements

- **Python 3.7+**
- **Flask**
- **SQLite3**

You can install Flask using `pip`:
```bash
pip install Flask
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rule-engine-app.git
cd rule-engine-app
```

### 2. Set up the environment
Ensure you have the necessary Python packages:
```bash
pip install Flask
```

### 3. Initialize the SQLite Database
The `db.py` file will handle database initialization automatically, but make sure the `rules.db` file is created in the `database` folder.

### 4. Run the Application
Start the Flask server:
```bash
python app.py
```
The application will run on `http://127.0.0.1:5000/`.

### 5. Access the UI
Open a browser and go to `http://127.0.0.1:5000/` to interact with the rule engine UI.

---

## API Endpoints

### 1. `/api/evaluate_rule` (POST)
- **Description**: Evaluates a given rule string against provided user data.
- **Request**:
    - `rule`: The rule to evaluate.
    - `age`, `department`, `salary`, `experience`: The user data attributes.
- **Response**: Returns the result of the evaluation (True/False) or an error message.

### 2. `/api/rules` (GET)
- **Description**: Retrieves all the stored rules.

### 3. `/api/update_rule/<rule_id>` (PUT)
- **Description**: Updates an existing rule in the database.

### 4. `/api/delete_rule/<rule_id>` (DELETE)
- **Description**: Deletes an existing rule from the database.

---

## Example Rule Strings

- **Rule 1**: `((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)`
- **Rule 2**: `((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)`

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.
