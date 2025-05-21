from app import greet

def test_greet():
    assert greet("SonarQube") == "Hello, SonarQube!"
    assert greet("drone stting") == "Hello, drone stting!"
