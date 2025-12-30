# Student Performance Tracker

**Abstract**
Student Performance Tracker: A command-line Python program for tracking student scores, averages, grades, and rankings with persistent JSON storage.

**Persistent Storage**

Student data is stored as a dictionary mapping student identifiers to numeric score lists, as shown below:

```python
{
    "Student A": [78, 90],
    "Student B": [65, 72]
}
```

**Grading and Evaluation Logic**

Grades are assigned using explicit thresholds to ensure consistency and transparency.

| Average Score | Grade |
| ------------- | ----- |
| ≥ 90          | A     |
| 80–89         | B     |
| 70–79         | C     |
| 60–69         | D     |
| < 60          | F     |

A student passes if their average score is 60 or above and fails otherwise.

**Error Handling Strategy**

Invalid inputs are rejected, missing data is handled safely, and file errors fall back to default states to prevent crashes or data corruption.

**Automated Testing Strategy**

Core logic is tested with pytest to ensure correct averages, grading, and pass/fail behavior.

To run the test suite:

```sh
pytest test_project.py
```

**Technology Stack**

The project uses Python 3.10+, standard library modules (`json`, `os`), and pytest for testing.

**Execution Instructions**

Ensure Python 3.10 or newer is installed. Navigate to the project root directory and execute the program using the following command:

```sh
python project.py
```

Student data will be automatically created and persisted in a file named `students.json`.

**Design Rationale**

A class-based design with JSON storage and a command-line interface was chosen for simplicity, reliability, and maintainability.

**Scalability and Extension Considerations**

The system can be extended to support weighted grades, report exports, or database storage with minimal changes.

**Project Structure**

```text
project/
├── project.py
├── test_project.py
├── requirements.txt
├── students.json
└── README.md
```

**Author**

_Benjamin A. Ngafua_ <br>
CS50P Final Project

**Declaration**

This project was developed in accordance with CS50’s academic honesty and final project guidelines and represents original work by the author.
