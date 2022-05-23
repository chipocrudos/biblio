from django.core.exceptions import ValidationError
from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Library'
        verbose_name_plural = 'Librarys'


class Rack(models.Model):
    number = models.PositiveIntegerField()
    locationIdentifier = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        managed = True
        verbose_name = 'Rack'
        verbose_name_plural = 'Racks'


def isbn_validator(value):

    invalid_isbn = True
    isbn = value.replace('-', '')

    if len(isbn) == 10:
        addition = 0
        for i in range(9):
            # 0   <=    0   <=      9
            if 0 <= int(isbn[i]) <= 9:
                addition += int(isbn[i]) * (10 - i)
            else:
                invalid_isbn = True

        if isbn[9] == 'X':
            invalid_isbn = not (11 - addition % 11 > 9)
        else:
            invalid_isbn = not (11 - addition % 11 == int(isbn[9]))

    elif len(isbn) == 13:
        addition = 0
        for i in range(12):
            if (i+1) % 2:
                addition += int(isbn[i])
            else:
                addition += int(isbn[i]) * 3

        module = [10 - (addition % 10), 0][(addition % 10) == 10]
        invalid_isbn = not (int(isbn[-1:]) == module)

    if invalid_isbn:
        raise ValidationError(
            'Is not a valit ISBN',
            params={'value': value}
        )


class Book(models.Model):
    isbn = models.CharField(max_length=18,
                            unique=True,
                            validators=[isbn_validator])
    title = models.CharField(max_length=120)
    subject = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    page = models.PositiveSmallIntegerField()

    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class BookItem(models.Model):

    REFERENCEONLY = True
    LOAN = False

    REFERENCES = (
        (REFERENCEONLY, 'Reference only'),
        (LOAN, 'Loan')
    )

    HARDCOVER = "Hardcover"
    PAPERBACK = "Paperback"
    AUDIOBOOK = "Audiobook"
    EBOOK = "Ebook"
    NEWSPAPER = "Magazine"
    JOURNAL = "Journal"

    BOOKFORMAT = (
        (HARDCOVER, HARDCOVER),
        (PAPERBACK, PAPERBACK),
        (AUDIOBOOK, AUDIOBOOK),
        (EBOOK, EBOOK),
        (NEWSPAPER, NEWSPAPER),
        (JOURNAL, JOURNAL),
    )

    AVAILABLE = "Available"
    RESERVED = "Reserved"
    LOANED = "Loaned"
    LOST = "Lost"

    BOOKSTATUS = (
        (AVAILABLE, AVAILABLE),
        (RESERVED, RESERVED),
        (LOANED, LOANED),
        (LOST, LOST),
    )

    book = models.ForeignKey('library.Book', on_delete=models.CASCADE)

    barcode = models.CharField(max_length=50)
    isReferenceOnly = models.BooleanField(
        default=REFERENCEONLY,
        choices=REFERENCES)

    borrowed = models.DateField()
    dueDate = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    format = models.CharField(max_length=50, choices=BOOKFORMAT)
    status = models.CharField(
        max_length=50,
        default=AVAILABLE,
        choices=BOOKSTATUS)

    dateOfPurchease = models.DateField()
    publicationDate = models.DateField()

    rack = models.ForeignKey('library.Rack', on_delete=models.PROTECT)
    library = models.ForeignKey('library.Library', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.barcode, self.book.isbn)

    class Meta:
        managed = True
        verbose_name = 'BookItem'
        verbose_name_plural = 'BookItem'

    def save(self, *args, **kwargs):
        if not self.barcode:
            total = BookItem.objects.count() + 1
            self.barcode = '{0:03d}{1:04d}{2:06d}'.format(
                self.library.id,
                self.rack.number,
                total
            )

        super().save(*args, **kwargs)
