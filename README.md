# 🏫 Teacher Management System (DBMS Project)

**A Python-MySQL based project for managing teacher records**  
Designed for the AISSCE Informatics Practices (065) coursework  
By: **Karthik V** | Under the guidance of **Mrs. Archana Pataskar**

---

## **📌 Project Overview**

**Teacher Management System** is a menu-driven command-line application built with **Python**, connected to a **MySQL database**, to manage and visualize teacher data efficiently. This system is tailored to automate the tasks of storing, viewing, updating, and analyzing teacher records.

---

## **🚀 Features**

- **Display All Records**  
- **Search by Teacher ID**
- **Insert New Teacher Record**
- **Update Existing Data (Salary)**
- **Delete Teacher Record**
- **Graphical Representations (Bar, Histogram, Stem)**
- **Exit Program Gracefully**

---

## **🛠️ Technologies Used**

- **Frontend / Scripting**: Python 3.x  
  - Libraries: `pandas`, `mysql.connector`, `prettytable`, `matplotlib`, `fontstyle`
- **Backend**: MySQL (Database name: `project`)
- **IDE**: VS Code / Python IDLE
- **Operating System**: Windows 11

---

## **🗃️ Database Schema**

**Table Name**: `project`  
| Column Name      | Data Type    | Description                          |
|------------------|--------------|--------------------------------------|
| id               | INT          | Teacher ID (Primary Key)             |
| name             | VARCHAR      | Teacher Name                         |
| dob              | DATE         | Date of Birth                        |
| father_name      | VARCHAR      | Father's Name                        |
| experience       | INT          | Teaching Experience (in years)       |
| post             | VARCHAR      | Post/Position                        |
| salary           | INT          | Monthly Salary                       |
| date_of_joining  | DATE         | Date of Joining                      |

---

## **📊 Graphical Output**

- **Bar Graph**: Name vs Salary  
- **Histogram**: Salary distribution  
- **Stem Plot**: Name vs Salary (Alternative view)

---

## **📷 Sample Output Screens**

> Screenshots of terminal output and graphs can be added here.

---

## **📄 Setup Instructions**

1. **Install required libraries**:
    ```bash
    pip install pandas matplotlib mysql-connector-python prettytable fontstyle
    ```

2. **Set up MySQL Database**:
    ```sql
    CREATE DATABASE project;
    USE project;

    CREATE TABLE project (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        dob DATE,
        father_name VARCHAR(50),
        experience INT,
        post VARCHAR(30),
        salary INT,
        date_of_joining DATE
    );
    ```

3. **Update MySQL credentials** in `final_project.py`:
    ```python
    con = sqltor.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="project")
    ```

4. **Run the project**:
    ```bash
    python final_project.py
    ```

---

## **📚 References**

- Informatics Practices by Preeti Arora  
- NCERT IP Textbook  
- Stack Overflow  
- Google & Online Resources

---

## **📌 License**

This project was created for educational purposes as part of the CBSE AISSCE curriculum. Open for academic use and learning.

---
