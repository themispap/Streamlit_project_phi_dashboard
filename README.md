# Φ Maths & Statistics Lab Dashboard

## Table of Contents
- [Overview](#overview)
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Overview
This repository contains a Streamlit dashboard for managing the Φ Maths & Statistics Lab, an educational platform that offers data analysis projects, university courses, and lessons for secondary school students.

## Introduction
The Φ (Phi) Maths & Statistics Lab is dedicated to providing high-quality education in mathematics and programming for high school students. We also undertake data analysis projects, equipping students with practical skills to excel in their academic and professional pursuits.

## Features
- **Dashboard**: An overview of key metrics, including total students, recent signups, and financial summaries.
- **Student Info**: Manage student records, view details, and track progress.
- **Customer Info**: Maintain customer information and track services used.
- **Add Records**: Add new students, customers, lessons, and more through intuitive forms.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: PostgreSQL
- **ORM**: SQLAlchemy
- **Language**: Python

## Folder Structure
```graphql
phi-maths-dashboard/
├── app/                  # Streamlit app scripts
│   ├── __init__.py
│   ├── main.py           # Main Streamlit app script
│   ├── pages/            # Additional Streamlit pages
│   ├── queries.py        # Optional: Store SQL queries as constants
├── sql/                  # SQL query files
│   ├── get_student_info.sql
│   ├── get_daily_lessons.sql
│   ├── get_balance_summary.sql
│   ├── ...               # Other SQL files
├── data/                 # Placeholder for local datasets
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables
├── README.md             # Project documentation
└── setup.sh              # Setup script
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phi_dashboard.git
   cd phi_dashboard
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your PostgreSQL database and configure the `.env` file with your database connection string.

## Usage
Run the Streamlit app:
```bash
streamlit run app/main.py
```

## Screenshots
![Screenshot 1](path/to/screenshot1.png)
![Screenshot 2](path/to/screenshot2.png)
![Screenshot 3](path/to/screenshot3.png)

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

### Instructions:
- Replace `path/to/screenshotX.png` with the actual paths to your screenshots.
- Feel free to customize any other sections as needed!

Let me know if you need further adjustments or anything else!
