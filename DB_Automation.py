import mysql.connector
# Establish the MySQL database connection
def connect_to_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connection established successfully.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to fetch data from a table
def fetch_data_from_table(connection, query):
    cursor = connection.cursor(dictionary=True)  # Using dictionary cursor for easier access to columns by name
    try:
        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all rows
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()

# Function to sort the data (by a specific column)
def sort_data(data, sort_by_column):
    # Sort the data based on the column name (e.g., 'age')
    return sorted(data, key=lambda x: x[sort_by_column])

# Main function to run the process
def main():
    # MySQL connection parameters
    host = 'localhost'  # Change this to your MySQL host
    user = 'root'  # Change this to your MySQL username
    password = 'yourpassword'  # Change this to your MySQL password
    database = 'yourdatabase'  # Change this to your MySQL database name

    # Connect to MySQL database
    connection = connect_to_mysql(host, user, password, database)

    if connection:
        # Example query to get data from a table (change 'your_table' to your actual table name)
        query = "SELECT * FROM your_table"

        # Fetch the data
        data = fetch_data_from_table(connection, query)

        if data:
            print("Original Data:")
            for row in data:
                print(row)

            # Sort the data by a specific column, e.g., 'age' or 'name'
            sorted_data = sort_data(data, 'your_column_to_sort_by')  # Replace with actual column name

            print("\nSorted Data:")
            for row in sorted_data:
                print(row)
        
        # Close the connection
        connection.close()

# Run the main function
if __name__ == "__main__":
    main()
