
# To Do List

This project is a small Django based Rest API that will allow you to create lists and tasks, and will allow you to mark a task as completed.

## Run Locally

Clone the project

```bash
  git clone https://github.com/codeplatoon-devops/to-do-list-django.git
```

Go to the project directory

```bash
  cd to-do-list-django
```

Create and activate Virtual Environment

```bash
  python -m venv `name_of_env`
  source `name_of_env`/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create your database

```bash
  createdb to_do
```

Migrate migrations

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

## API Reference

### Get all Lists

```http
  GET /api/v1/lists/
```

### Get a Lists

```http
  GET /api/v1/lists/<int:id>/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. ID/PK of desired list |

### Get a task from a list

```http
  GET /api/v1/list/<int:id>/todos/<int:item_id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` | `int` | **Required**. ID/PK of desired list |
| `item_id` | `int` | **Required**. ID/PK of desired task |

### Create a list

```http
  POST /api/v1/lists/
```

#### Data (application/json)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `str` | **Required**. Title of the list to be created |

### Create a task

```http
  POST /api/v1/lists/<int:id>/todos/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` | `int` | **Required**. ID/PK of desired list |

#### Data (application/json)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `str` | **Required**. Title of the task to be created |

### Mark a task as complete

```http
  PUT /api/v1/list/<int:id>/todos/<int:item_id>/complete/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id` | `int` | **Required**. ID/PK of desired list |
| `item_id` | `int` | **Required**. ID/PK of desired task |
