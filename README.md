# Car Rental System

## Project Overview
This project simulates a car rental system that allows users to book cars for specific dates and durations, implemented in Python using object-oriented principles. The system manages three types of vehicles: sedans, SUVs, and vans, each with a limited number of cars available. It verifies vehicle availability, handles date conflicts, and only confirms reservations if a car of the requested type is available.

## Features
- **Vehicle Inventory Management**: Tracks and manages the inventory of available cars by type.
- **Reservation System**: Allows users to book cars for specific dates and durations.
- **Date Conflict Handling**: Prevents overlapping reservations by checking if a car is available for the requested period.
- **Limited Fleet**: Controls the number of cars available for each vehicle type (sedan, SUV, van).

## Installation
1. Ensure you have Python installed
2. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

## Usage
You can run the main application as follows:
   ```python
   python main.py
   ```

## Code Structure
- main.py: Contains the primary code for managing car inventory and reservations.
- main_test.py: Includes unit tests to verify that the system behaves as expected, covering scenarios like booking available cars, handling date conflicts, and limiting car availability per type.

## Running Tests

To ensure the system works correctly, you can run unit tests with the following command:

```python
python main_test.py
```