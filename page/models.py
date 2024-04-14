from django.db import models

# Create your models here.


# TARAW BOYISHA MODELS
class Category(models.Model):
    """Taraw boyisha categoriyalar"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


"""
Xorezm
Tashkent
Nókis
"""
class Location(models.Model):
    """Manzili"""
    where = models.CharField(max_length=250)

    def __str__(self):
        return self.where


class Language(models.Model):
    """
    Qaysi tillerdi biliwi
    Misali:
            Orıs tili
            Anglichan tili
            Ózbek tili
            Qaraqalpaq tili
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Specialist(models.Model):
    """
        Bul Specialist boyisha
        Misali: 
            Reumatologiya
            Sport medicinası
            Gastroenterologiya
            Onkologiya
            Immunologiya
            Kardiologiya
            Fizikalıq terapiya
            Urologiya
            Pediatriya
            Anesteziologiya
            Nevrologiya
            Immigratsiya huqıqı
            Qarızdarlıq boyınsha
            Jınayat jumısları boyınsha
            Salıq boyisha
            Shańaraqqa tiyisli huqıq
            Miynet nızamshiliǵi
    """
    SPECIALIZATION_CHOICES = [
        ('YURIST', 'Yurist'),
        ('SHIPAKER', 'Shipaker'),
    ]
    specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Professional(models.Model):
    """
        Qa'niyge iyesi boyisha mag'liwmat...
    """
    specialization = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="specializations")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="professional/")
    about = models.TextField()
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="locations")
    languages = models.ManyToManyField(Language, related_name="languages")
    specialists = models.ManyToManyField(Specialist, related_name="specialists")
    

    def __str__(self):
        return self.first_name



class Education(models.Model):
    """
        Qaysi Oqiwda oqig'anlig'i haqida mag'liwmatlar
    """
    who = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="educations")
    name = models.CharField(max_length=200)
    where = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField()
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    """
        Qay jerde islegeni haqida
    """
    who = models.ForeignKey(Professional, on_delete=models.CASCADE,related_name="experiences")
    name = models.CharField(max_length=200)
    where = models.CharField(max_length=200)
    when = models.DateField()

    def __str__(self) -> str:
        return self.name

# END TARAW BOYISHA MODELS

# USER MODEL
class UserBase(models.Model):
    """
        User table
    """
    user_name = models.CharField(max_length=240)
    image = models.ImageField(upload_to="users/")
    star = models.IntegerField()
    feedback = models.TextField()
    
    def __str__(self):
        return self.user_name
# END USER MODEL


# APTEKAR USHIN MODEL
class Product(models.Model):
    title = models.CharField(max_length=200, default="Analgin")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="aptekars", default="aptekars/dari.webp")

    def __str__(self):
        return self.title

# END APTEKAR USHIN MODEL
