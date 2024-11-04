from models.user import User
from extensions import db

# see the db table user with the following values: 
# {
#     "username": "john_doe",
#     "email": "john@example.com"
# }

def seed_db():
    try:
        new_user = User(username="john_doe", email="john@example.com")
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()