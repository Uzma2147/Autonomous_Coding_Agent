#  Autonomous Coding Agent

An AI-inspired autonomous coding agent that automates software bug analysis by searching a code repository, diagnosing issues, generating code patches, executing tests in a sandbox, and producing detailed reports through a state-driven workflow.

# Overview

The Autonomous Coding Agent is a backend application developed in Python and FastAPI. It demonstrates how an intelligent software agent can process bug reports, locate relevant source files, analyze possible causes, suggest code fixes, execute automated tests, and generate a professional report.

This project was developed as part of my AI Engineering Internship at **Khizex**.

# Features

- Bug Intake System
- Repository Search
- Rule-Based Bug Diagnosis
- Automatic Patch Generation
- Git-Style Diff Generation
- Source Code Reader
- Sandbox Test Execution
- State Machine Workflow
- FastAPI REST API
- Professional Report Generation

##  Tech Stack

- Python 3
- FastAPI
- Pydantic
- Pytest
- pathlib
- difflib
- Uvicorn

##  Installation

Clone the repository:

bash
git clone  https://github.com/Uzma2147/Autonomous_Coding_Agent.git


Move into the project directory:

->bash
cd Autonomous-Coding-Agent


Create a virtual environment:

->bash
python -m venv venv


Activate the virtual environment:

Windows

->bash
venv\Scripts\activate

Install dependencies:

->bash
pip install -r requirements.txt

# Run the Project

Start the FastAPI server:

->bash
uvicorn main:app --reload


Open Swagger UI:
http://127.0.0.1:8000/docs


Run the interactive agent:

->bash
python -m tests.test_agent

##Author

**Uzma Kainat**
Software Engineering Student | AI & Data Science Enthusiast
Developed during the **Khizex AI Engineering Internship**.

## License
This project is developed for educational and internship purposes.