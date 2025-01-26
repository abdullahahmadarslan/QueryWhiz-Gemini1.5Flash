import sqlite3
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Loaing the environment variable
load_dotenv()

# Initialize the Google Gemini API (ensure you have the API key set as an environment variable)
API_KEY = os.environ.get("api_key")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to interact with the SQLite database
def execute_query(query):
    try:
        conn = sqlite3.connect("studentdb.db")
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return str(e)

# Streamlit App UI
st.title("Natural Language to SQL Query App")
st.write("Enter a natural language query, and I will fetch results from the database.")

# User Input
user_prompt = st.text_input("Your Query", placeholder="e.g., Show all students majoring in Computer Science")

# Button to execute the query
if st.button("Get Results"):
    if user_prompt:
        # Few-shot inference prompt for Gemini
        prompt_template = (
            """
            I have an SQLite database with a table named 'student'. The table has the following columns:
            - id (integer)
            - name (text)
            - age (integer)
            - major (text)
            - gpa (real)
            - graduation_year (integer)

            Here are some example queries:
            1. Natural language: "Show all students majoring in Computer Science"
               SQL: SELECT * FROM student WHERE major = 'Computer Science';
            2. Natural language: "List the names and GPAs of students with a GPA greater than 3.5"
               SQL: SELECT name, gpa FROM student WHERE gpa > 3.5;
            3. Natural language: "Find the number of students graduating in 2025"
               SQL: SELECT COUNT(*) FROM student WHERE graduation_year = 2025;

            Please provide only a valid SQL SELECT query without any code block markers or comments. For example:
            Natural language: "List all students"
            SQL: SELECT * FROM student;

            Convert the following natural language query into a valid SQL SELECT statement:
            """
        )

        # Prepare the complete prompt
        full_prompt = prompt_template + f"\n{user_prompt}\n"

        # Get the response from the Gemini API
        try:
            response = model.generate_content(full_prompt)
            generated_sql = response.text.strip()  # Get the text and remove extra whitespace

            st.write("### Generated SQL Query:")
            st.code(generated_sql)

            # Execute the SQL query on the database
            results = execute_query(generated_sql)

            # Display results
            if results:
                st.write("### Query Results:")
                st.dataframe(results)
            else:
                st.write("No results found or invalid query.")
        except Exception as e:
            st.error(f"Error generating query: {e}")
    else:
        st.warning("Please enter a query.")