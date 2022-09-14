from django.db import models


class Er(models.Model):
    NOMBRE_ERS = [
        ('Z', 'Zidor'),
        ('KOS', 'Koskorrak'),
        ('KAS', 'Kaskondoak'),
        ('OIN', 'Oinarinak'),
        ('AZK', 'Azkarrak'),
        ('BID', 'Bidean'),
        ('AIN', 'Aingura'),
        ('CATE', 'Catecumenado'),
    ]

    nombre = models.CharField(
        choices=NOMBRE_ERS,
        max_length=100,
        primary_key=True)

    def natural_key(self):
        return self.nombre


    def __str__(self):
        return self.nombre


class Rama(models.Model):
    NOMBRE_RAMAS = [
        ('Z2', 'Zidor 2'),
        ('Z3', 'Zidor 3'),
        ('KOS', 'Koskorrak'),
        ('KAS1', 'Kaskondoak 1'),
        ('KAS2', 'Kaskondoak 2'),
        ('OIN1', 'Oinarinak 1'),
        ('OIN2', 'Oinarinak 2'),
        ('AZK1', 'Azkarrak 1'),
        ('AZK2', 'Azkarrak 2'),
        ('BID1', 'Bidean 1'),
        ('BID2', 'Bidean 2'),
        ('AIN', 'Aingura'),
        ('CATE', 'Catecumenado'),
    ]

    nombre = models.CharField(
        choices=NOMBRE_RAMAS,
        default='Z2',
        max_length=100,
        primary_key=True)

    descripcion = models.TextField(
        null=True,
        blank=True)

    icon = models.CharField(
        max_length=100,
        null=True,
        blank=True)



    # Constraints
    er = models.ForeignKey(
        Er,
        on_delete=models.CASCADE,
        default='KAS')

    def __str__(self):
        return self.nombre

class Salida(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.URLField()
    descripcion = models.TextField(null=True)
    foto = models.ImageField()

    # Constraints
    rama = models.ForeignKey(
        Rama, 
        on_delete=models.CASCADE,
        default='Kaskondoak 1')

    def __str__(self):
        return self.nombre


class Taller(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.URLField()
    descripcion = models.TextField(null=True)
    foto = models.ImageField()

    # Constraints
    rama = models.ForeignKey(
        Rama, 
        on_delete=models.CASCADE,
        default='Kaskondoak 1')

    def __str__(self):
        return self.nombre
