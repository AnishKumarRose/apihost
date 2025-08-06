# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictInt, StrictStr  # noqa: F401
from typing import Any, List  # noqa: F401
from openapi_server.models.task import Task  # noqa: F401
from openapi_server.models.task_create import TaskCreate  # noqa: F401
from openapi_server.models.token import Token  # noqa: F401
from openapi_server.models.user_create import UserCreate  # noqa: F401
from openapi_server.models.user_out import UserOut  # noqa: F401


def test_login_post(client: TestClient):
    """Test case for login_post

    Login and get access token
    """

    headers = {
    }
    data = {
        "username": 'username_example',
        "password": 'password_example'
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/login",
    #    headers=headers,
    #    data=data,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_register_post(client: TestClient):
    """Test case for register_post

    Register a new user
    """
    user_create = {"password":"password","username":"username"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/register",
    #    headers=headers,
    #    json=user_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tasks_get(client: TestClient):
    """Test case for tasks_get

    Get list of tasks
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tasks",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tasks_post(client: TestClient):
    """Test case for tasks_post

    Create a task
    """
    task_create = {"title":"title"}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/tasks",
    #    headers=headers,
    #    json=task_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tasks_task_id_delete(client: TestClient):
    """Test case for tasks_task_id_delete

    Delete a task
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/tasks/{task_id}".format(task_id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_tasks_task_id_put(client: TestClient):
    """Test case for tasks_task_id_put

    Update a task
    """
    task_create = {"title":"title"}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/tasks/{task_id}".format(task_id=56),
    #    headers=headers,
    #    json=task_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

