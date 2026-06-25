import pytest


@pytest.mark.parametrize(
    ("activity_name", "email"),
    [
        ("Chess Club", "newstudent@mergington.edu"),
        ("Programming Class", "student@mergington.edu"),
    ],
)
def test_signup_for_activity_returns_success_message(client, activity_name, email):
    # Arrange
    activity_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(activity_path, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}


def test_signup_for_existing_participant_returns_bad_request(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"
    activity_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(activity_path, params={"email": existing_email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student is already signed up for this activity"}


def test_unregister_for_unknown_participant_returns_not_found(client):
    # Arrange
    activity_name = "Chess Club"
    unknown_email = "ghost@mergington.edu"
    activity_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(activity_path, params={"email": unknown_email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}
