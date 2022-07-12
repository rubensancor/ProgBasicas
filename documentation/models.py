from django.db import models


class ER(models.Model):
    NOMBRE_ERS = [
        ('Z', 'Zidor'),
        ('KOS', 'Koskorrak'),
        ('KAS', 'Kaskondoak'),
    ]
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    NOMBRE_GRUPOS = [
        ('Z2', 'Zidor 2'),
        ('Z3', 'Zidor 3'),
        ('KOS', 'Koskorrak'),
        ('KAS1', 'Kaskondoak 1'),
    ]

class Trimestre(models.Model):
    TRIMESTRES = [
        (1, 'Primero'),
        (2, 'Segundo'),
        (3, 'Tercero')
    ]
    numero = models.IntegerField(choices=TRIMESTRES,
                                 default=1)
    texto = models.TextField()

    # Constraints
    ER = models.ForeignKey(ER, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto


class Campamento(models.Model):
    NOMBRES_CAMPAMENTO = [
        ('NA', 'Navidad'),
        ('SS', 'Semana Santa'),
        ('VE', 'Verano'),

    ]
    nombre = models.CharField(
        choices=NOMBRES_CAMPAMENTO,
        default='NA'
    )

    # Constraints
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Contenido(models.Model):
    texto = models.TextField()

    # Constraints
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto


class Monte(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.URLField()
    foto = models.ImageField()

    # Constraints
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Taller(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.URLField()
    foto = models.ImageField()

    # Constraints
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Reunión(models.Model):
    nombre = models.CharField(max_length=100)
    texto = models.TextField()

    # Constraints
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Simbolo(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()

    # Constraints
    ER = models.ForeignKey(ER, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Paso(models.Model):
    texto = models.TextField()

    # Constraints
    ER = models.ForeignKey(ER, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto