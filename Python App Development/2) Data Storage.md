# $\fbox{Chapter: DATA STORAGE}$





## **Topic - 1: SQLite**

```python
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Create a table 'users' if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Insert some data into the table
cursor.execute('''
	INSERT INTO users (name, age)
	VALUES (?, ?)
	''',
	('John Doe', 30)
)

cursor.execute('''
	INSERT INTO users (name, age)
	VALUES (?, ?)
	''',
	('Jane Smith', 25)
)

# Commit the transaction
connection.commit()

# Query and display all users
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

print("All Users:")
for user in users:
    print(user)

# Update a user's age
cursor.execute('''
UPDATE users
SET age = ?
WHERE name = ?
''', (32, 'John Doe'))

# Commit the transaction
connection.commit()

# Query again after update
cursor.execute('SELECT * FROM users')
updated_users = cursor.fetchall()
print("\nUpdated Users:")
for user in updated_users:
    print(user)

# Delete a user
cursor.execute('''
DELETE FROM users
WHERE name = ?
''', ('Jane Smith',))

# Commit the transaction
connection.commit()

# Query after deletion
cursor.execute('SELECT * FROM users')
final_users = cursor.fetchall()

print("\nFinal Users After Deletion:")
for user in final_users:
    print(user)

# Close the connection
connection.close()
```
