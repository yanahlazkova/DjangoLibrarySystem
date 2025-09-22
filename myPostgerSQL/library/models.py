from django.db import models

# from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True)
    #
    class Meta:
        ordering = ['-id']


    # Many-to-Many зв'язок з моделлю User
    # через проміжну модель Borrow
    # related_name='borrowed_books': Этот параметр позволяет легко получить
    # доступ ко всем книгам, взятым пользователем, через user.borrowed_books
    # borrowers = models.ManyToManyField(User, through='Borrow', related_name='borrowed_books')
    def __str__(self):
        return f"{self.title} ({self.author}, {self.year}, {self.genre.name})"



class Genre(models.Model):

    name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name


class UserBooks(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')
    date_received = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    date_returned = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return (f"{self.user.firstname} {self.user.lastname} borrowed {self.book.title}"
                f"data received: {self.date_received} "
                f"data returned: {self.date_returned}")
