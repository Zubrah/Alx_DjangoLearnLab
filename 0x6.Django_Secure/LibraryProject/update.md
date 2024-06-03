
### update.md

```markdown
# Update the title of the Book instance

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
print(book.title, book.author, book.publication_year)
