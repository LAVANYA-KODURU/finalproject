# Data Loading

This directory contains the script to load Zomato restaurant data into a database.

## Purpose

The purpose of this script is to load restaurant data from a given CSV file into a database. This is part of the "Zomato Restaurant Listing & Searching" project.

## Dependencies

- Python 3.x
- pandas
- pymysql

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>/data_loading
    ```

2. **Install required Python packages:**
    ```bash
    pip install pandas pymysql
    ```

## Usage

1. **Configure the script:**

    Modify the following variables in the script as needed:
    ```python
    csv_file = 'zomato.csv'  # Path to your CSV file
    db_host = 'localhost'  # Database host
    db_user = 'root'  # Database user
    db_password = ''  # Database password
    db_name = 'zomatofinal'  # Database name
    table_name = 'zomato_restaurants'  # Table name
    ```

2. **Run the script:**
    ```bash
    python data_loading_script.py
    ```

## Script Details

### `create_table`

This function creates a table in the specified database if it does not already exist. The table schema matches the structure of the CSV data.

### `load_csv_to_db`

This function loads data from the specified CSV file into the database table. It handles different CSV encodings and ensures data is correctly inserted into the table.

### Example Commands

1. **Create the table:**
    ```python
    create_table(db_host, db_user, db_password, db_name, table_name)
    ```

2. **Load CSV data into the database:**
    ```python
    load_csv_to_db(csv_file, db_host, db_user, db_password, db_name, table_name)
    ```
