from unittest.mock import patch, MagicMock
from src.services.enrollment_service import EnrollmentService

# Mock the GET /enrollments/<user_id> route
@patch.object(EnrollmentService, 'get_enrollments_for_user')
def test_get_user_enrollments(mock_get_enrollments_for_user, client, seed_user):
    user, access_token = seed_user

    # Create mock enrollment objects
    mock_enrollment_1 = MagicMock(id=1, user_id=user.id, course_id=1)
    mock_enrollment_2 = MagicMock(id=2, user_id=user.id, course_id=2)

    # Mock the return value for get_enrollments_for_user
    mock_get_enrollments_for_user.return_value = [mock_enrollment_1, mock_enrollment_2]

    # Make the GET request to the /enrollments/<user_id> endpoint
    response = client.get(
        f'/enrollments/{user.id}',
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Assert that the response is successful and returns a 200 status code
    assert response.status_code == 200

    # Assert that the response contains the user's enrollments data
    assert response.json == [
        {'id': 1, 'user_id': user.id, 'course_id': 1},
        {'id': 2, 'user_id': user.id, 'course_id': 2}
    ]

    # Ensure the get_enrollments_for_user method was called with the correct user ID
    mock_get_enrollments_for_user.assert_called_once_with(user.id)

# Mock the POST /enroll route
@patch.object(EnrollmentService, 'enroll_user_in_course')
def test_enroll_user(mock_enroll_user_in_course, client, seed_user):
    user, access_token = seed_user

    # Create a mock enrollment object
    mock_enrollment = MagicMock()
    mock_enrollment.id = 1
    mock_enrollment.user_id = 1
    mock_enrollment.course_id = 1

    # Mock the return value for enroll_user_in_course
    mock_enroll_user_in_course.return_value = mock_enrollment

    # Create the payload to send to the POST request
    enrollment_data = {
        'user_id': 1,
        'course_id': 1
    }

    # Make the POST request to the /enroll endpoint
    response = client.post(
        '/enroll',
        json=enrollment_data,
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Assert that the response is successful and returns a 201 status code
    assert response.status_code == 201

    # Assert that the response contains the enrollment's data
    assert response.json == {
        'id': 1,
        'user_id': 1,
        'course_id': 1
    }

    # Ensure the enroll_user_in_course method was called with the correct data
    mock_enroll_user_in_course.assert_called_once_with(1, 1)


from unittest.mock import patch

# Mock the DELETE /enrollments/<enrollment_id> route
@patch.object(EnrollmentService, 'remove_enrollment')
def test_remove_enrollment(mock_remove_enrollment, client, seed_user):
    user, access_token = seed_user
    enrollment_id = 1

    # Make the DELETE request to the /enrollments/<enrollment_id> endpoint
    response = client.delete(
        f'/enrollments/{enrollment_id}',
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Assert that the response is successful and returns a 200 status code
    assert response.status_code == 200

    # Assert that the response contains the correct message
    assert response.json == {'message': 'Enrollment removed'}

    # Ensure the remove_enrollment method was called with the correct enrollment ID
    mock_remove_enrollment.assert_called_once_with(enrollment_id)
