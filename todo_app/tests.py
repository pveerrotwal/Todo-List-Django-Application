# from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import ToDoList, ToDoItem


class ToDoListTests(TestCase):
    def setUp(self):
        self.todo_list = ToDoList.objects.create(title="Groceries")

    def test_todo_list_creation(self):
        """Test if ToDoList is created successfully."""
        self.assertEqual(self.todo_list.title, "Groceries")

    def test_todo_list_str_method(self):
        """Test the __str__ method of ToDoList."""
        self.assertEqual(str(self.todo_list), "Groceries")

    def test_todo_list_absolute_url(self):
        """Test the get_absolute_url method of ToDoList."""
        expected_url = reverse("list", args=[self.todo_list.id])
        self.assertEqual(self.todo_list.get_absolute_url(), expected_url)


class ToDoItemTests(TestCase):
    def setUp(self):
        self.todo_list = ToDoList.objects.create(title="Work")
        self.todo_item = ToDoItem.objects.create(
            title="Finish project",
            description="Complete the task on time",
            due_date=timezone.now() + timezone.timedelta(days=3),
            todo_list=self.todo_list,
        )

    def test_todo_item_creation(self):
        """Test if ToDoItem is created successfully."""
        self.assertEqual(self.todo_item.title, "Finish project")
        self.assertEqual(self.todo_item.description, "Complete the task on time")

    def test_todo_item_str_method(self):
        """Test the __str__ method of ToDoItem."""
        expected_str = f"Finish project: due {self.todo_item.due_date}"
        self.assertEqual(str(self.todo_item), expected_str)

    def test_todo_item_absolute_url(self):
        """Test the get_absolute_url method of ToDoItem."""
        expected_url = reverse(
            "item-update", args=[str(self.todo_list.id), str(self.todo_item.id)]
        )
        self.assertEqual(self.todo_item.get_absolute_url(), expected_url)
