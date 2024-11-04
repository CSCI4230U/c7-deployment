Packages:

    flask
    flask_sqlalchemy
    flask_migrate
    flask_jwt_extended
    pytest

`pip install -r requirements.txt`

From the root:

Delete `instance` and `migrations` folders before

    flask --app src db init
    flask --app src db migrate
    flask --app src db upgrade

Insert user on the database for authentication (jwt)

run: `flask --app src run --debug`

test: `pytest tests/`