# QueryWhiz

This project demonstrates a Streamlit application that takes natural language input, converts it into an SQL query using the Google Gemini API, executes the query on an SQLite database, and displays the results in a user-friendly interface. The project aims to bridge the gap between human-friendly queries and database operations seamlessly.

---

## Features

- **Natural Language Processing**: Accepts natural language input to create SQL queries.
- **Prompt Templating**: Created Few Shot Inference Prompts to get optimized inferences from the LLM.
- **Google Gemini API Integration**: Leverages the power of the Gemini 1.5 Flash model for generating SQL queries.
- **SQLite Database**: Queries are executed on a pre-defined SQLite database (`studentdb.db`) containing a `student` table.
- **User-Friendly Interface**: A Streamlit-based UI that simplifies user interaction.

---

## Prerequisites

Before you start, make sure you have the following installed:

- Python 3.10+
- Required Python libraries:
  - `streamlit`
  - `sqlite3` (part of Python standard library)
  - `google.generativeai`


