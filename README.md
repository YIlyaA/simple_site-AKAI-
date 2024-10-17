# Jewelry Inventory Management System

## Overview
This web application is designed for managing a jewelry inventory, allowing users to add, edit, delete, and view records of various jewelry items. The application features a user-friendly interface with sorting and filtering capabilities for enhanced user experience.

## Features

1. **Homepage**
   - Displays a table listing all jewelry items with the following columns:
     - Id
     - Type (e.g., Diamond, Ruby, Gold)
     - Weight (e.g., in carats or grams)
     - Purity (e.g., SI, S, VVS)
     - Color (e.g., White, Pink, Yellow)
     - Origin (country of origin)
     - Owner (name of the owner)
   - Pagination controls to navigate through multiple pages of records.
   - Search functionality to find specific records.

2. **Add Record**
   - A form to input new jewelry items, including:
     - Type
     - Weight
     - Purity
     - Color
     - Origin
     - Owner
   - Submit button to save the new record and a Back button to return to the homepage.

3. **Edit Record**
   - An interface to modify existing records.
   - Fields pre-populated with the current data for the selected jewelry item.
   - Save button to apply changes and a Back button to return to the homepage.

4. **Delete Record**
   - Each row in the jewelry table includes a "Delete" button.
   - Confirmation prompt to prevent accidental deletions.

5. **Filtering and Sorting**
   - Dropdown menu to filter records based on different criteria (e.g., weight ascending/descending).
   - Users can choose how to sort the displayed records for better visibility.

## Technologies Used
- Frontend: HTML, CSS, JavaScript (for dynamic functionalities).
- Backend: Django.
- Database: SQLite.

## Installation
1. Clone the repository.
   ```bash
   git clone <repository-url>
   ```

2. ```
   -----------------------------------------
   pipinstall pipenv
   pipenv shell
   pipenv install

   or
   
   pip install -r requirements.txt
   -----------------------------------------

   
   python manage.py migrate
   python manage.py makemigrations
   python manage.py runserver
   
   ```
