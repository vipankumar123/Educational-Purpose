# signals.py
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.signals import request_started, request_finished, got_request_exception
from .models import Book

@receiver(pre_save, sender=Book)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:  # Check if the slug is not already set
        slug_value = instance.title + "_"
        instance.slug = slug_value

@receiver(post_save, sender=Book)
def post_save_book(sender, instance, created, **kwargs):
    if created:
        print(f'A new book titled "{instance.title}" has been saved.')
    else:
        print(f'The book titled "{instance.title}" has been updated.')


@receiver(pre_delete, sender=Book)
def pre_delete_book(sender, instance, **kwargs):
    print(f'About to delete book titled "{instance.title}".')

@receiver(post_delete, sender=Book)
def post_delete_book(sender, instance, **kwargs):
    print(f'Book titled "{instance.title}" has been deleted.')

@receiver(request_started)
def request_started_callback(sender, **kwargs):
    print("Request started processing...")

@receiver(request_finished)
def request_finished_callback(sender, **kwargs):
    print("Request finished processing.")

@receiver(got_request_exception)
def request_exception_callback(sender, **kwargs):
    print("Exception occurred during request processing.")
