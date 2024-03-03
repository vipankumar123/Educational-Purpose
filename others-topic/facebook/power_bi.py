# from sqlalchemy import create_engine, MetaData, Table, Column, DateTime, Float
# from sqlalchemy.sql import select
# from sqlalchemy.exc import OperationalError
# import psutil
# import time

# # Database connection parameters
# DATABASE_URL = 'mssql+pyodbc://root:root@localhost/SystemPerformanceDB?driver=ODBC+Driver+17+for+SQL+Server'

# # Create SQLAlchemy engine
# engine = create_engine(DATABASE_URL)

# # Create metadata
# metadata = MetaData()

# # Define the table structure
# system_performance = Table(
#     'SystemPerformanceData',
#     metadata,
#     Column('Timestamp', DateTime),
#     Column('CPU_Usage', Float),
#     Column('Memory_Usage', Float),
#     Column('Disk_IO', Float),
#     Column('Network_Traffic', Float)
# )

# try:
#     # Create the table if not exists
#     metadata.create_all(engine)

#     # Main loop for data collection and storage
#     while True:
#         timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
#         cpu_usage = psutil.cpu_percent(interval=1)
#         memory_usage = psutil.virtual_memory().percent
#         disk_io = psutil.disk_io_counters().read_count + psutil.disk_io_counters().write_count
#         network_traffic = psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent

#         # Insert data into SQL Server using SQLAlchemy
#         with engine.connect() as connection:
#             insert_query = system_performance.insert().values(
#                 Timestamp=timestamp,
#                 CPU_Usage=cpu_usage,
#                 Memory_Usage=memory_usage,
#                 Disk_IO=disk_io,
#                 Network_Traffic=network_traffic
#             )
#             connection.execute(insert_query)

#         # Sleep for 5 seconds before collecting the next set of data
#         time.sleep(5)

# except OperationalError as e:
#     print("An error occurred:", e)



import mysql.connector

# Establish connection to the MySQL server
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="test123"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Define the SQL query to create the example_table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS example_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
    """

    # Execute the create table query
    cursor.execute(create_table_query)
    print("Table 'example_table' created successfully.")

    # Define data to be inserted into the table
    data = [
        ('John', 25),
        ('Alice', 30),
        ('Bob', 28),
        ('Carol', 35),
        ('David', 40),
        ('Eva', 22),
        ('Frank', 33),
        ('Grace', 27),
        ('Henry', 38),
        ('Ivy', 29)
    ]

    # Define the SQL query to insert data into the example_table
    insert_query = "INSERT INTO example_table (name, age) VALUES (%s, %s)"

    # Execute the insert query for each data tuple
    cursor.executemany(insert_query, data)
    conn.commit()

    print("Data inserted successfully.")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close the cursor and database connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()


