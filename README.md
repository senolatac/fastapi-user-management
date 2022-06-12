# fastapi-user service
User service with python-fastapi

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/0bd67820567942cfa10336c3c0e65a88)](https://www.codacy.com/gh/senolatac/fastapi-user-management/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=senolatac/fastapi-user-management&amp;utm_campaign=Badge_Grade)

### Install dependencies and run server
Dependencies are managed by  [poetry](https://python-poetry.org/)

[Install poetry](https://python-poetry.org/docs/#installation) before moving forward.

Use Poetry to install required dependencies:
```
poetry install --no-root
```

If you need to use new dependencies (e.g. requests), use poetry:
```
poetry add requests 
```

To start the server call the following command:
```
poetry run uvicorn --port 5000 --host 127.0.0.1 app.main:app --reload
```

It will automatically load any code updates, no need to restart.

then reach it -> `http://localhost:5000/docs`

You can call CTRL-C to stop the server.

### Run tests
```
poetry run pytest  
```
