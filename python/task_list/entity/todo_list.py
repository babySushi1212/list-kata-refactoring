from task_list.entity.project import Project
from task_list.entity.task import Task


class TodoList:

    def __init__(self) -> None:
        self.__projects: list[Project] = []

    def add_project(self, name: str, tasks: list[Task]):
        self.__projects.append(Project(name=name, tasks=tasks))

    def get_all_project(self) -> list[Project]:
        return self.__projects

    # weird to have get_task here
    def get_task(self, name: str) -> list[Task] | None:
        for p in self.__projects:
            if p.get_name() == name:
                return p.get_tasks()
        return None
