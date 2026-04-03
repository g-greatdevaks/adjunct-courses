# Lab Cheatsheet

Interactive Python tracking scripts and reference solutions for Laboratory 1 (Personal Assignment Tracker).

## Environment Setup

To run the tracking scripts locally, the required dependencies must be installed. The utilization of a virtual environment is recommended.

### 1. Initialize Virtual Environment

The following commands are executed from the repository root directory:

```bash
python3 -m venv venv
source venv/bin/activate
```

> [!NOTE]
> Detailed virtual environment setup instructions for various operating systems (Linux dependencies, Windows activation) are documented within the `dbms_foundations.ipynb` notebook.

### 2. Install Dependencies

The following command is executed to install dependencies via the requirements file located in this directory:

```bash
pip install -r dbms/glau/bcsc0034/lecture1/lab_cheatsheet/requirements.txt
```

### Running the Tracker

The tracker script can be executed programmatically:

```bash
python dbms/glau/bcsc0034/lecture1/lab_cheatsheet/assignments_tracker.py
```
