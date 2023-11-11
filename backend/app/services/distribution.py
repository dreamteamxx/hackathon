import datetime
import math
from typing import List

from app.schemas import PointRead, EmployeeReferenceRead


async def grade_tasks(
        points: List[PointRead]
) -> dict[int, dict[str, int | PointRead]]:
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
            points_map[point.id] = {"priority": 1, "task_id": 1, "point": point}
        elif (
                point.issued_cards_count > 0
                and point.approved_requests_count / point.issued_cards_count < 0.5
        ):
            points_map[point.id] = {"priority": 2, "task_id": 2, "point": point}
        elif (
                point.connected_date == datetime.date.today() - datetime.timedelta(days=1)
                or point.cards_delivered is None
        ):
            points_map[point.id] = {"priority": 3, "task_id": 3, "point": point}
    return points_map


def calculate_distance_between_points(point_1: str, point_2: str) -> float:
    """
    Calculates distance between two coordinates with the Haversine formula
    :param point_1: Coordinates of point 1
    :param point_2: Coordinates of point 2
    :return: Distance between points
    """
    lat1, lon1 = point_1.split(",")
    lat2, lon2 = point_2.split(",")
    lat1, lon1, lat2, lon2 = map(float, [lat1, lon1, lat2, lon2])
    radius = 6371  # km

    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) * math.sin(d_lat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)
    ) * math.sin(d_lon / 2) * math.sin(d_lon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance


async def assign_tasks(
        employees: List[EmployeeReferenceRead], points: dict[int, dict[str, int]]
) -> dict:
    """
    Assigns tasks to employees based on their level and the tasks' priority
    :param employees: List of employees to assign tasks to
    :param points: List of points to assign tasks to
    :return: List of tasks assigned to employees
    """
    offices = [employee.office for employee in employees]
    offices_set = set(offices)
    office_task_map = {}

    for point in points.values():
        point_obj: PointRead = point["point"]
        coordinates = point_obj.coordinates
        if coordinates is None:
            continue
        distance_map = {}
        for office in offices_set:
            distance_map[office.id] = calculate_distance_between_points(
                coordinates, office.coordinates
            )
        closest_office = min(distance_map, key=distance_map.get)
        if closest_office not in office_task_map:
            office_task_map[closest_office] = []
        office_task_map[closest_office].append(point)

    return office_task_map
