from unittest.mock import patch, MagicMock
from src.services.user_service import UserService

def test_get_users_with_seed_user(client, seed_user):
    user, access_token = seed_user

    # Make the GET request to the /users endpoint with the JWT token
    response = client.get(
        '/users', 
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Assert that the response is successful
    assert response.status_code == 200

    # Assert that the seeded user is in the response
    assert {
        'id': user.id,
        'username': 'john_doe',
        'email': 'john@example.com'
    } in response.json



# Mock the POST /users route
@patch.object(UserService, 'create_new_user')
def test_create_user(mock_create_new_user, client, seed_user):
    user, access_token = seed_user

    # Mock the return value for the create_new_user method
    mock_create_new_user.return_value = MagicMock(id=2, username='jane_doe', email='jane@example.com')

    # Create the payload to send to the POST request
    new_user_data = {
        'username': 'jane_doe',
        'email': 'jane@example.com'
    }

    # Make the POST request to the /users endpoint
    response = client.post(
        '/users',
        json=new_user_data,
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Assert that the response is successful and returns a 201 status code
    assert response.status_code == 201

    # Assert that the response contains the new user's data
    assert response.json == {
        'id': 2,
        'username': 'jane_doe',
        'email': 'jane@example.com'
    }

    # Ensure the create_new_user method was called with the correct data
    mock_create_new_user.assert_called_once_with('jane_doe', 'jane@example.com')
