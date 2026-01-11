# Student Course & Grade Management System

This is a simple student–course–grade management system built with Python and SQLite.  
The project was created to practice basic database design and Python–SQLite integration.

## Features

- Manage students
- Manage courses
- Assign grades to students
- Data validation with:
  - Foreign keys
  - Unique constraints
  - Grade range (0–100)

## Technologies

- Python 3
- SQLite3
- DB Browser for SQLite (optional)

## Database Structure

### students
| Column | Type | Description |
|------|------|------------|
| id | INTEGER | Primary key |
| name | TEXT | Student name |

### courses
| Column | Type | Description |
|------|------|------------|
| course_id | INTEGER | Primary key |
| course_name | TEXT | Course name |

### grades
| Column | Type | Description |
|------|------|------------|
| id | INTEGER | Primary key |
| student_id | INTEGER | Student reference |
| course_id | INTEGER | Course reference |
| grade | INTEGER | 0–100 |

## How It Works

- The database and tables are created automatically if they do not exist.
- Students and courses are stored in separate tables.
- Grades connect students and courses using foreign keys.
- Each student can have only one grade per course.

## How to Run

```bash
python main.py
