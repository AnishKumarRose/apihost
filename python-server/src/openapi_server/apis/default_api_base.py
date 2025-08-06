# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictInt, StrictStr
from typing import Any, List
from openapi_server.models.task import Task
from openapi_server.models.task_create import TaskCreate
from openapi_server.models.token import Token
from openapi_server.models.user_create import UserCreate
from openapi_server.models.user_out import UserOut
from openapi_server.security_api import get_token_BearerAuth

class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def login_post(
        self,
        username: StrictStr,
        password: StrictStr,
    ) -> Token:
        ...


    async def register_post(
        self,
        user_create: UserCreate,
    ) -> UserOut:
        ...


    async def tasks_get(
        self,
    ) -> List[Task]:
        ...


    async def tasks_post(
        self,
        task_create: TaskCreate,
    ) -> Task:
        ...


    async def tasks_task_id_delete(
        self,
        task_id: StrictInt,
    ) -> None:
        ...


    async def tasks_task_id_put(
        self,
        task_id: StrictInt,
        task_create: TaskCreate,
    ) -> Task:
        ...
