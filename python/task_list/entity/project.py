from task_list.entity.task import Task


class Project:

    def __init__(self, name: str, tasks: list[Task]) -> None:
        self.__name: str = name
        self.__tasks: list[Task] = tasks

    def get_tasks(self) -> list[Task]:
        return self.__tasks

    def get_name(self) -> str:
        return self.__name
