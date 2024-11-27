# User Registration Streamlit App

This is a simple Streamlit application that allows you to register users, update their data, and delete users from a SQLite database. The app provides a user-friendly interface to interact with a database of user information, specifically names and ages.

## Features

- Add a new user with their name and age.
- Update the name and/or age of an existing user.
- Delete a user from the database.
- View the list of registered users in a clean, structured layout.

## Prerequisites

Before you run the app, ensure that you have Python 3.6+ installed.

You will also need to create a virtual environment and install the necessary dependencies.

### Setting up the environment

1. **Create a Virtual Environment**:
   To avoid conflicts with other Python projects, it is recommended to create a virtual environment.

   Open your terminal and run:

   ```bash
   python3 -m venv env

This will create a directory named env which contains a clean Python environment.

Install Dependencies: After activating the virtual environment, install the required libraries using pip.

pip install -r requirements.txt

Alternatively, you can manually install the required dependencies with:

    pip install streamlit sqlite3

Running the Application

Once you have set up the virtual environment and installed the dependencies, you can run the Streamlit app using the following command:

streamlit run app.py

This will start the Streamlit app in your browser, where you can interact with it to register users, update or delete existing records, and view the list of users.
App Explanation

The app allows you to perform the following actions:

    Add Users: You can enter a name and age, and the app will save the information in an SQLite database.
    Update Users: You can update the name and age of an existing user by clicking the "Save changes" button next to the user’s information.
    Delete Users: You can delete a user by clicking the "Delete" button next to their information.

The app also displays a list of all registered users and updates the list dynamically when changes are made.
SQLite Database

The app uses an SQLite database (user_data.db) to store user information. The database automatically creates a table for users if it doesn't exist already.

The table schema is as follows:

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)

The app interacts with the database to add, update, or delete user records.
