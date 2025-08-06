# coding: utf-8

from typing import Dict, List, Optional  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.impl.Login import LoginImpl
from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import StrictInt, StrictStr
from typing import Any, List
from openapi_server.models.task import Task
from openapi_server.models.task_create import TaskCreate
from openapi_server.models.token import Token
from openapi_server.models.user_create import UserCreate
from openapi_server.models.user_out import UserOut
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()
service = LoginImpl()
ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/login",
    responses={
        200: {"model": Token, "description": "Access token"},
    },
    tags=["default"],
    summary="Login and get access token",
    response_model_by_alias=True,
)
async def login_post(
    username: StrictStr = Form(None, description=""),
    password: StrictStr = Form(None, description=""),
) -> Token:
    try:
        login = await service.LoginDetails(username, password)
        return login
    except HTTPException as err:
        raise HTTPException(status_code=err.status_code, detail=err.detail)


@router.post(
    "/register",
    responses={
        200: {"model": UserOut, "description": "User created"},
    },
    tags=["default"],
    summary="Register a new user",
    response_model_by_alias=True,
)
async def register_post(
    user_create: UserCreate = Body(None, description=""),
) -> Any:
        try:
            create = await service.signup(user_create)
            return create
        except HTTPException as err:
            raise HTTPException(status_code=err.status_code, detail=err.detail)


@router.get(
    "/tasks",
    responses={
        200: {"model": List[Task], "description": "List of tasks"},
    },
    tags=["default"],
    summary="Get list of tasks",
    response_model_by_alias=True,
)
async def tasks_get(
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> List[Task]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().tasks_get()


@router.post(
    "/tasks",
    responses={
        200: {"model": Task, "description": "Task created"},
    },
    tags=["default"],
    summary="Create a task",
    response_model_by_alias=True,
)
async def tasks_post(
    task_create: TaskCreate = Body(None, description=""),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Task:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().tasks_post(task_create)


@router.delete(
    "/tasks/{task_id}",
    responses={
        200: {"description": "Task deleted"},
    },
    tags=["default"],
    summary="Delete a task",
    response_model_by_alias=True,
)
async def tasks_task_id_delete(
    task_id: StrictInt = Path(..., description=""),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().tasks_task_id_delete(task_id)


@router.put(
    "/tasks/{task_id}",
    responses={
        200: {"model": Task, "description": "Task updated"},
    },
    tags=["default"],
    summary="Update a task",
    response_model_by_alias=True,
)
async def tasks_task_id_put(
    task_id: StrictInt = Path(..., description=""),
    task_create: TaskCreate = Body(None, description=""),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Task:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().tasks_task_id_put(task_id, task_create)
