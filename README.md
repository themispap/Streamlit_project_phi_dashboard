# Φ Maths & Statistics Lab Dashboard - Streamlit App

This project is a Streamlit application that provides an interactive dashboard for the Φ Maths & Statistics Lab. The app connects to a PostgreSQL database using SQLAlchemy, enabling real-time data visualization and management of the lab's operations, including data analysis projects, university courses, and secondary school lessons.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Setup Instructions](#setup-instructions)
5. [Usage](#usage)
6. [Screenshots](#screenshots)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

The 'Φ' Maths & Statistics Lab offers three main services:
1. Data analysis projects
2. Courses for university students
3. Lessons for secondary school students

This Streamlit app provides a user-friendly interface to interact with the database, visualize key metrics, and generate reports.

## Features

- **Interactive Dashboard**: Real-time visualization of data.
- **Data Management**: Add, update, and delete records for projects, students, customers, courses, lesson plans, payments, and income.
- **Reports**: Generate detailed reports on income, expenses, student enrollments, and project details.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: PostgreSQL
- **ORM**: SQLAlchemy
- **Language**: Python

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/phi-maths-stats-lab-streamlit.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd phi-maths-stats-lab-streamlit
   ```
3. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up the PostgreSQL database**:
   - Follow the setup instructions from the [Φ Maths & Statistics Lab Database](https://github.com/your-username/phi-maths-stats-lab-database) repository to create and populate the database.
6. **Configure the database connection**:
   - Create a `.env` file in the project root directory and add your database connection string:
     ```
     DATABASE_URL=postgresql://username:password@localhost/phi_maths_stats_lab
     ```
7. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Usage

- Open your web browser and navigate to `http://localhost:8501` to access the Streamlit app.
- Use the sidebar to navigate through different sections of the dashboard.
- Add, update, or delete records as needed.
- Generate reports by selecting the desired options from the reports section.

## Screenshots

_Screenshot examples of the dashboard can be added here to give users a visual overview of the app._

## Contributing

Contributions are welcome! If you have any suggestions or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.