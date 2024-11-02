# **MentiBot** - Mental Health Web Application

**MentiBot** is a Flask-based mental health application designed to help users track their mood, manage stress, and receive mental health support through an AI-powered chatbot. With a user-friendly interface and essential mental health tools, MentiBot empowers users to improve their well-being.

---

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Setup and Installation](#setup-and-installation)
4. [Requirements](#requirements)
5. [Running the Application](#running-the-application)
6. [Minimum System Specifications](#minimum-system-specifications)
7. [Troubleshooting](#troubleshooting)
8. [License](#license)

---

## Features

- **Mood Tracker**: Enables users to log and monitor their moods over time.
- **Stress Management Tools**: Includes mindfulness exercises, guided meditation, and breathing exercises to reduce stress.
- **AI-powered Chatbot**: Provides personalized mental health tips and resources.
- **Dark Mode Toggle**: Allows users to switch between light and dark modes for a customized experience.
- **Responsive UI**: Built with Tailwind CSS, offering a visually appealing and mobile-friendly design.

---

## Project Structure

```plaintext
mentibot/
├── .venv/                      # Virtual environment files (optional)
├── instance/                   # Configuration and instance files
├── media/                      # Folder for media files (e.g., user uploads)
├── static/                     # Static files (CSS, JavaScript, images)
├── templates/                  # HTML templates for Flask
├── app.py                      # Main Flask application file
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## Setup and Installation

### 1. Clone the Repository
Clone the project repository to your local machine:

```bash
git clone https://github.com/u2508/mentibot.git
cd mentibot
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
To keep dependencies isolated, create a virtual environment:

#### For Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### For macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Step 1: Initialize the Database (If Required)
If this is the first time running the application, initialize the database:

```bash
flask db init
flask db migrate
flask db upgrade
```

### Step 2: Run the Application
Start the Flask application by running the `app.py` file:

```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

---

## Minimum System Specifications

- **Operating System**: Windows, macOS, or Linux
- **Processor**: 1 GHz or faster
- **RAM**: 512 MB minimum (1 GB recommended)
- **Python Version**: 3.7 or higher
- **Storage**: At least 200 MB of free space

Ensure you have Python 3.7+ installed. Lower-end systems may experience reduced performance under high loads.

---

## Troubleshooting

- **Cannot Start Flask Server**: Make sure the virtual environment is activated and dependencies are installed.
- **Database Errors**: Check that the migrations have been correctly initialized and applied.
- **Dependency Issues**: Update dependencies with `pip install --upgrade -r requirements.txt`.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This documentation provides a comprehensive guide to setting up and running MentiBot with minimal configuration required.