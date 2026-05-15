"""Service helpers for department CRUD workflows used by API views."""
from .models import Department
from django.db.models import QuerySet
from typing import Optional


def get_all_departments() -> QuerySet:
    """Return departments in a stable order for UI dropdowns and lists."""
    return Department.objects.all().order_by('name')


def get_department_by_id(department_id: int) -> Optional[Department]:
    """Return a department by ID, or None when it does not exist."""
    try:
        return Department.objects.get(id=department_id)
    except Department.DoesNotExist:
        return None


def create_department(**kwargs) -> Department:
    """Create a department after trimming user-entered names."""
    if 'name' in kwargs and isinstance(kwargs['name'], str):
        kwargs['name'] = kwargs['name'].strip()

    department = Department.objects.create(**kwargs)
    return department


def update_department(department_id: int, **kwargs) -> Optional[Department]:
    """Update department fields and return None if the department is missing."""
    department = get_department_by_id(department_id)
    if department:
        for key, value in kwargs.items():
            # Normalize editable text fields before persisting.
            if isinstance(value, str):
                value = value.strip()
            setattr(department, key, value)
        department.save()
        return department
    return None


def delete_department(department_id: int) -> bool:
    """Delete a department by ID. Returns True when a row was removed."""
    department = get_department_by_id(department_id)
    if department:
        department.delete()
        return True
    return False
