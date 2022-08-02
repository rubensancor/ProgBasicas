from django.db import models


class Er(models.Model):
    NOMBRE_ERS = [
        ('Z', 'Zidor'),
        ('KOS', 'Koskorrak'),
        ('KAS', 'Kaskondoak'),
    ]
    nombre = models.CharField(
        choices=NOMBRE_ERS,
        max_length=100)

    def __str__(self):
        return self.nombre


class Rama(models.Model):
    NOMBRE_RAMAS = [
        ('Z2', 'Zidor 2'),
        ('Z3', 'Zidor 3'),
        ('KOS', 'Koskorrak'),
        ('KAS1', 'Kaskondoak 1'),
    ]

    nombre = models.CharField(
        choices=NOMBRE_RAMAS,
        default='Z2',
        max_length=100)

    descripcion = models.TextField(
        null=True,
        blank=True)


    # Constraints
    er = models.ForeignKey(
        Er, 
        on_delete=models.CASCADE,
        default='KAS')

    def __str__(self):
        return self.nombre


class Paso(models.Model):
    descripcion = models.TextField()

    # Constraints
    rama = models.OneToOneField(
        Rama,
        on_delete=models.CASCADE,
        default='Kaskondoak 1')

    def __str__(self):
        return self.descripcion


class Trimestre(models.Model):
    TRIMESTRES = [
        (1, 'Primer'),
        (2, 'Segundo'),
        (3, 'Tercer')
    ]
    numero = models.IntegerField(choices=TRIMESTRES,
                                 default=1)
    descripcion = models.TextField(
        default="",
        null=True,
        blank=True
    )

    # Constraints
    rama = models.ForeignKey(
        Rama, 
        on_delete=models.CASCADE,
        default='KAS1')

    def __str__(self):
        return '%s trimestre de %s' %  (self.get_numero_display(), self.rama)


class Campamento(models.Model):
    NOMBRES_CAMPAMENTO = [
        ('NA', 'Navidad'),
        ('SS', 'Semana Santa'),
        ('VE', 'Verano'),

    ]
    nombre = models.CharField(
        choices=NOMBRES_CAMPAMENTO,
        default='NA',
        max_length=2
    )

    # Constraints
    trimestre = models.ForeignKey(
        Trimestre, 
        on_delete=models.CASCADE,
        default=1)

    def __str__(self):
        return self.nombre


class Monte(models.Model):
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


class Reunion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)

    # Constraints
    trimestre = models.ForeignKey(
        Trimestre, 
        on_delete=models.CASCADE,
        default=1)

    def __str__(self):
        return self.nombre


class Simbolo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    foto = models.ImageField()

    # Constraints
    rama = models.ForeignKey(
        Rama,
        on_delete=models.CASCADE,
        default='KAS1')

    def __str__(self):
        return self.nombre


class Recurso(models.Model):
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

class Contenido(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.URLField(
        null=True,
        blank=True)
    descripcion = models.TextField(
        null=True,
        blank=True)
    foto = models.ImageField(
        null=True,
        blank=True
    )

    # Constraints
    trimestre = models.ForeignKey(
        Trimestre, 
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    rama = models.ForeignKey(
        Rama, 
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    paso = models.ForeignKey(
        Paso,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    campamento = models.ForeignKey(
        Campamento, 
        on_delete=models.CASCADE, 
        null=True,
        blank=True)

    def __str__(self):
        return self.nombre
