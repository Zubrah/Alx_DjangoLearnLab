from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

def __str__(self):
    """
    Returns a string representation of the Book object.

    Parameters:
    self (Book): The instance of the Book class for which the string representation is to be generated.

    Returns:
    str: The title of the book.
    """
    return self.title



    
    
