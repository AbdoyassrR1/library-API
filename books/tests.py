from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django",
            subtitle="APIs with python and django",
            author="abdoyasser",
            isbn= "none"
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Django")
        self.assertEqual(self.book.subtitle, "APIs with python and django")
        self.assertEqual(self.book.author, "abdoyasser")
        self.assertEqual(self.book.isbn, "none")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "python and django")
        self.assertTemplateUsed(response, "books/book_list.html")
