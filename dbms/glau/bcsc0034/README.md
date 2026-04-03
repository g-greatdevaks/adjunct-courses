# BCSC0034: Database Management Systems

This directory contains module materials for the Database Management Systems (DBMS) course at GLA University, Noida, India.

## Course Structure

The course is divided into lectures, each containing its own notebooks and lab resources.

- **[`lecture1/`](lecture1/)**: Python Connectivity & Database Design Principles.

---

## Usage Instructions (Running Notebooks)

### 💻 Option 1: Local Run (Recommended for MySQL)

The laboratory exercises utilize a local MySQL database. A local machine run is recommended.

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/g-greatdevaks/adjunct-courses.git
    cd adjunct-courses
    ```
2.  **Set Up Virtual Environment**:
    Standard procedures for initializing a virtual environment are executed from the repository root:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    > [!NOTE]
    > Comprehensive virtual environment setup instructions for various operating systems (Linux dependencies, Windows activation) are documented within the `dbms_foundations.ipynb` notebook.

3.  **Install Lab Dependencies**: The specific requirements file for the lab (located in `lecture1/lab_cheatsheet/`) can be utilized. Alternatively, `%pip install` can be run directly inside the notebook cells.
    ```bash
    pip install -r dbms/glau/bcsc0034/lecture1/lab_cheatsheet/requirements.txt
    ```
4.  **Launch Jupyter Lab/Notebook**:
    ```bash
    jupyter notebook
    ```
5.  **Credentials Adjustment**: The `dbms_foundations.ipynb` notebook is opened. The `%env MYSQL_DB_PASSWORD` cells are modified if the local MySQL password differs from the default (`root`).

### ☁️ Option 2: [Google Colab](https://colab.research.google.com/) Run

1.  The `.ipynb` file is uploaded to Google Colab.
2.  The `%pip install` cell at the top of the notebook is executed to install dependencies within the Colab instance.
3.  _Prudence_: Colab runs on remote servers. It cannot access a `localhost` MySQL directly. A tunnel (such as `ngrok`) or a cloud-hosted DB table must be utilized to run MySQL queries from Colab.
