# Event Management CLI App

This is a command-line interface (CLI) application written in Python for managing events, participants, and tickets. It allows users to create and manage events, add and update participants, assign tickets to participants and perform various other operations.

## Features

- Create a new event
- Update an existing event
- Get event details by ID
- Get all events
- Count the number of events
- Delete an event
- Add a participant to an event
- Update a participant
- Get participant by ID.
- Get participant by event ID
- Get all participants
- Count all participants
- Delete a participoant
- Add a ticket
- Update a ticket
- Get ticket by ID
- Get ticket by participant ID
- Get ticket by event ID
- Get all tickets
- Count Tickets
- Delete tickets


## Prerequisites

- Python 3.x
- SQLite3 (included in Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/WendyKariuki/Phase-3-project.git
```
2. Navigate to the cloned directory:
```bash
cd Phase-3-project
```
3. (Optional) Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate # On Windows, use: source venv/Scripts/activate
```
4. Run the application:
```bash
python3 main.py
```

## Project Structure

- Phase-3-project     
    - lib/
        - config.py
        - event.py
        - participant.py
        - tickets.py
    - data.db
    - LICENSE
    - main.py
    - README.md
    - readonly.py

- `data.db`: SQLite database file
- `lib/config.py`: Database configuration and table creation/deletion
- `lib/event.py`: Functions for managing events
- `lib/participant.py`: Functions for managing participants
- `lib/tickets.py`: Functions for managing tickets
- `main.py`: Entry point of the application
- `LICENSE` : This project is licensed under the MIT License. By using this software, you agree to the terms outlined in the license.
- `README.md`: Project README

## Dependencies

- Python 3.x
- SQLite3 (included in Python standard library)

## Configuration

- Database: `data.db`
- Cursor: `CURSOR`

## Running the Application

To run the application, simply type `python3 main.py` in your terminal.

## Usage
The application is run from the command line using the `main.py` script. Upon running the script, the application will initialize the database, create the necessary tables, and perform some example operations.

You can modify the `main.py` script to include your desired operations or create additional scripts to interact with the application.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Author
- [Wendy](https://github.com/WendyKariuki/Phase-3-project.git)

## Version

- 1.0.0
