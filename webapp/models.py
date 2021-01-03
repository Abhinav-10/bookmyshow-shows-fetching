from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

#Create your models here.

class City(models.Model) :
    city_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self) :
        return self.city_name


class theatre(models.Model) :
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    city = models.ManyToManyField(City,related_name="theatre")

    def __str__(self) :
        return self.name


class screen(models.Model) :
    name = models.CharField(max_length=20)
    no_of_rows = models.IntegerField(validators=[MaxValueValidator(75)])
    no_of_columns = models.IntegerField(validators=[MaxValueValidator(50)])
    theatre = models.ForeignKey(theatre,related_name="screen",on_delete=models.CASCADE)

    def __str__(self) :
        return "{x} {y}".format(x=self.name,y=self.theatre.name)



class movie(models.Model) :
    name = models.CharField(max_length=50)
    hero = models.CharField(max_length=30)
    heroine = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    genre = models.CharField(max_length=150,help_text='Seperate genre with spaces',null=True)
    language = models.CharField(max_length=150,help_text='Seperate language with spaces',null=True)
    description = models.TextField(default='Description Text')
    release_date = models.DateField(help_text='mm/dd/yyyy')
    runtime_in_minutes = models.IntegerField(validators=[MaxValueValidator(200)])
    trailer = models.CharField(max_length=1000)
    thumbnail_image = models.ImageField(upload_to='movie_thumbs')
    slideshow_image = models.ImageField(upload_to='movie_thumbs',default='true')

    def __str__(self) :
        return self.name


class show(models.Model) :
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()
    screen = models.ForeignKey(screen,related_name="show_screen",on_delete=models.CASCADE)
    theatre = models.ForeignKey(theatre,related_name="show_theatre",on_delete=models.CASCADE)
    movie = models.ForeignKey(movie,related_name="show_movie",on_delete=models.CASCADE)
    city = models.ManyToManyField(City,related_name="show_city")



    def __str__(self) :
        return "Date : {}".format(self.date)


TICKET_STATUS_CHOICES = (
    (1, 'AVAILABLE'),
    (2, 'BLOCKED'),
    (3, 'BOOKED')
)

class booking(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    row_num = models.PositiveSmallIntegerField(null=False, blank=False)
    col_num = models.PositiveSmallIntegerField(null=False, blank=False)
    show = models.ForeignKey(show,related_name="booking_show",null=False,on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="booking_user",null=False,default=None, on_delete=models.CASCADE)
    status = models.IntegerField(choices=TICKET_STATUS_CHOICES, default=1)
    session = models.CharField(blank=False, null=False, max_length=200)

    class Meta:
        unique_together = ('show', 'row_num', 'col_num')