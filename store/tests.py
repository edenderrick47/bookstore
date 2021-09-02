from django.test import TestCase
from .models import Category, Writer, Book, Review, Slider
# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='thiller')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_create_at(self):
        self.category.create_at_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class WriterTestClass(TestCase):
    def setUp(self):
        self.writer = Writer(name='thiller')
        self.writer.save_writer()

    def test_instance(self):
        self.assertTrue(isinstance(self.writer, Writer))

    def test_create_at(self):
        self.writer.create_at_writer()
        writers = Writer.objects.all()
        self.assertTrue(len(writers) > 0)

    def test_delete_category(self):
        self.writer.delete_writer()
        writer =  Writer.objects.all()
        self.assertTrue(len(writer) == 0)

