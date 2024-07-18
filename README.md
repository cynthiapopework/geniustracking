# Company Project

This project provides a Flask-based internal API for tracking shipments and finding DHL service points. The API exposes endpoints to get tracking information and locate service points based on various parameters.

## Introduction

This project is designed to provide a simplified interface for interacting with DHL's tracking and service point APIs. It serves as an internal API for DigitalGenius to fetch tracking details and locate DHL service points based on various criteria.

## Features

- Fetch tracking information for shipments.
- Locate DHL service points based on country code, address locality, and radius.

## Setup

### Prerequisites

- Python 3.8 or higher
- `pyenv` for managing Python versions
- `pip` for managing Python packages

### Using pyenv

1. **Install pyenv**:

   Follow the installation instructions from the [pyenv GitHub repository](https://github.com/pyenv/pyenv#installation).

2. **Install Python Version**:

   Use `pyenv` to install the required Python version:

   ```sh
   pyenv install 3.11.4
   ```

3. **Set the Local Python Version**:

   Set the local Python version for the project:

   ```
   pyenv local 3.11.4
   ```

### Installing Dependencies

1. **Create a Virtual Environment**:
   ```
   python -m venv venv
   ```
2. **Activate the Virtual Environment**:
   ```
   source venv/bin/activate
   ```
3. **Install Required Packages**:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. **Running the Flask API**

   ```
   python main.py
   ```

   This will start the Flask server on http://localhost:5000.

2. **Directly Calling Repository Functions**
   ```
   python direct_call.py
   ```
3. **Calling the API Programmatically**
   ```
   python call_api.py
   ```

### Testing
1. **To run tests**
    ```
    python -m unittest discover tests
    ```
