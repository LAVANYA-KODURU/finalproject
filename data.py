#importing necessary libraries
import pandas as pd 
import pymysql
import os

def create_table(db_host, db_user, db_password, db_name, table_name):
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = connection.cursor()
    
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        Restaurant_ID INT PRIMARY KEY,
        Restaurant_Name VARCHAR(255),
        Country_Code INT,
        City VARCHAR(255),
        Address VARCHAR(255),
        Locality VARCHAR(255),
        Locality_Verbose VARCHAR(255),
        Longitude FLOAT,
        Latitude FLOAT,
        Cuisines VARCHAR(255),
        Average_Cost_for_two INT,
        Currency VARCHAR(255),
        Has_Table_booking VARCHAR(10),
        Has_Online_delivery VARCHAR(10),
        Is_delivering_now VARCHAR(10),
        Switch_to_order_menu VARCHAR(10),
        Price_range INT,
        Aggregate_rating FLOAT,
        Rating_color VARCHAR(50),
        Rating_text VARCHAR(50),
        Votes INT
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    print(f"Table '{table_name}' checked/created.")
    
    cursor.close()
    connection.close()
    
#to load csv data into database 
def load_csv_to_db(csv_file, db_host, db_user, db_password, db_name, table_name):
    try:
        if not os.path.isfile(csv_file):
            print(f"Error: File '{csv_file}' does not exist.")
            return
        
        try:
            data_frame = pd.read_csv(csv_file, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                data_frame = pd.read_csv(csv_file, encoding='latin1')
            except UnicodeDecodeError:
                data_frame = pd.read_csv(csv_file, encoding='iso-8859-1')
        
        print(f"CSV file loaded. Number of rows: {len(data_frame)}")
        
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = connection.cursor()
#iterate over each row in data frame and insert that each row into  
        for i, row in data_frame.iterrows():
            insert_query = f"""
            
            INSERT INTO {table_name} (
                Restaurant_ID, Restaurant_Name, Country_Code, City, Address, Locality, Locality_Verbose,
                Longitude, Latitude, Cuisines, Average_Cost_for_two, Currency, Has_Table_booking,
                Has_Online_delivery, Is_delivering_now, Switch_to_order_menu, Price_range,
                Aggregate_rating, Rating_color, Rating_text, Votes
            ) VALUES (
                {row['Restaurant ID']}, 
                '{pymysql.converters.escape_string(str(row['Restaurant Name']))}', 
                {row['Country Code']}, 
                '{pymysql.converters.escape_string(str(row['City']))}', 
                '{pymysql.converters.escape_string(str(row['Address']))}', 
                '{pymysql.converters.escape_string(str(row['Locality']))}', 
                '{pymysql.converters.escape_string(str(row['Locality Verbose']))}', 
                {row['Longitude']}, 
                {row['Latitude']}, 
                '{pymysql.converters.escape_string(str(row['Cuisines']))}', 
                {row['Average Cost for two']}, 
                '{pymysql.converters.escape_string(str(row['Currency']))}', 
                '{pymysql.converters.escape_string(str(row['Has Table booking']))}', 
                '{pymysql.converters.escape_string(str(row['Has Online delivery']))}', 
                '{pymysql.converters.escape_string(str(row['Is delivering now']))}', 
                '{pymysql.converters.escape_string(str(row['Switch to order menu']))}', 
                {row['Price range']}, 
                {row['Aggregate rating']}, 
                '{pymysql.converters.escape_string(str(row['Rating color']))}', 
                '{pymysql.converters.escape_string(str(row['Rating text']))}', 
                {row['Votes']}
            );
            """
            cursor.execute(insert_query)
#commits the transaction after adding all the rows
        connection.commit()
        print(f"Data from {csv_file} loaded into {table_name} table in the database.")
        
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_file = 'zomato.csv'  
    db_host = 'localhost'
    db_user = 'root'
    db_password = ''
    db_name = 'zomatofinal'
    table_name = 'zomato_restaurants'
    
    create_table(db_host, db_user, db_password, db_name, table_name)
    load_csv_to_db(csv_file, db_host, db_user, db_password, db_name, table_name)
    