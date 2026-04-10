# BCSC0034: Database Management Systems

This directory contains module materials for the Database Management Systems (DBMS) course at GLA University, Noida, India.

## Course Structure

The course is divided into lectures, each containing its own notebooks, lab resources, and specific setup instructions.

- **[`lecture1/`](lecture1/)**: Python Connectivity & Database Design Principles.
- **[`lecture2/`](lecture2/)**: Advanced Data Retrieval: Subqueries and Query Optimization.

---

## General Usage Instructions

### 💻 Option 1: Local Run (Recommended)

Laboratory exercises typically utilize a local MySQL database. A local machine run is recommended.

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/g-greatdevaks/adjunct-courses.git
    cd adjunct-courses
    ```
2.  **Navigate and Setup**:
    Navigate to the specific lecture directory (e.g., `dbms/glau/bcsc0034/lecture1/` or `lecture2/`) and consult the `README.md` file within that directory for detailed environment setup instructions.

### ☁️ Option 2: [Google Colab](https://colab.research.google.com/) Run

1.  The `.ipynb` file is uploaded to Google Colab.
2.  The `%pip install` cell at the top of the notebook is executed to install dependencies within the Colab instance.
3.  _Note on Database Access_: Colab runs on remote servers and cannot access a `localhost` MySQL instance directly. A tunnel (such as `ngrok`) or a cloud-hosted database must be utilized to connect to MySQL from Colab.
    dbms/glau/bcsc0034/README.md
