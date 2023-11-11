import datetime
from typing import List

from app.schemas import PointRead, EmployeeReferenceRead


async def grade_tasks(
        points: List[PointRead]
) -> dict[int, dict[str, int]]:
    """
    Distributes tasks to employees based on their level and the tasks' priority
    :param points: List of points to distribute and assign to employees
    :return:
    """
    # Task 1 if days_after_last_delivery > 7 and approved_requests_count >0  or days_after_last_delivery > 14
    # Task 2 if issued_cards_count > 0 and approved_requests_count/issued_cards_count < 0.5
    # Task 3 if connected_date is yesterday(timedelta) or cards_delivered is none

    points_map = {}  # {point_id: {priority: priority, task_id: task_id}}

    for point in points:
        if (
                point.days_after_last_delivery > 7
                and point.approved_requests_count > 0
                or point.days_after_last_delivery > 14
        ):
            points_map[point.id] = {"priority": 1, "task_id": 1}
        elif (
                point.issued_cards_count > 0
                and point.approved_requests_count / point.issued_cards_count < 0.5
        ):
            points_map[point.id] = {"priority": 2, "task_id": 2}
        elif (
                point.connected_date == datetime.date.today() - datetime.timedelta(days=1)
                or point.cards_delivered is None
        ):
            points_map[point.id] = {"priority": 3, "task_id": 3}
    return points_map


async def assign_tasks(
        employees: List[EmployeeReferenceRead], points: dict[int, dict[str, int]]
) -> dict:
    """
    Assigns tasks to employees based on their level and the tasks' priority
    :param employees: List of employees to assign tasks to
    :param points: List of points to assign tasks to
    :return: List of tasks assigned to employees
    """
    return {}
