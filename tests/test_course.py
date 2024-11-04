from unittest.mock import patch, MagicMock
from src.services.course_service import CourseService

# Mock the GET /courses route
@patch.object(CourseService, 'get_all_courses')
def test_get_courses(mock_get_all_courses, client, seed_user):
    user, access_token = seed_user

    # Create mock course objects with real data
    mock_course_1 = MagicMock(id=1, name='Course 1', description='Description 1')
    mock_course_2 = MagicMock(id=2, name='Course 2', description='Description 2')

    # Ensure the MagicMock returns real values for these attributes
    mock_course_1.id = 1
    mock_course_1.name = 'Course 1'
    mock_course_1.description = 'Description 1'

    mock_course_2.id = 2
    mock_course_2.name = 'Course 2'
    mock_course_2.description = 'Description 2'

    # Mock the return value for get_all_courses to return a list of mock courses
    mock_get_all_courses.return_value = [mock_course_1, mock_course_2]

    # Make the GET request to the /courses endpoint
    response = client.get(
        '/courses',
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Assert that the response is successful and returns a 200 status code
    assert response.status_code == 200

    # Assert that the response contains the mock courses data
    assert response.json == [
        {'id': 1, 'name': 'Course 1', 'description': 'Description 1'},
        {'id': 2, 'name': 'Course 2', 'description': 'Description 2'}
    ]

from unittest.mock import patch, MagicMock

# Mock the POST /courses route
@patch.object(CourseService, 'create_new_course')
def test_create_course(mock_create_new_course, client, seed_user):
    user, access_token = seed_user

    # Create a mock course object with real data
    mock_course = MagicMock()
    mock_course.id = 1
    mock_course.name = 'New Course'
    mock_course.description = 'New Description'

    # Mock the return value for create_new_course
    mock_create_new_course.return_value = mock_course

    # Create the payload to send to the POST request
    new_course_data = {
        'name': 'New Course',
        'description': 'New Description'
    }

    # Make the POST request to the /courses endpoint
    response = client.post(
        '/courses',
        json=new_course_data,
        headers={"Authorization": f"Bearer {access_token}"}
    )

    # Assert that the response is successful and returns a 201 status code
    assert response.status_code == 201

    # Assert that the response contains the new course's data
    assert response.json == {
        'id': 1,
        'name': 'New Course',
        'description': 'New Description'
    }

    # Ensure the create_new_course method was called with the correct data
    mock_create_new_course.assert_called_once_with('New Course', 'New Description')
