from django.db import models


class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

    def __str__(self):
        return self.nombre


class Modalidad(models.Model):

    MODALIDAD_PRESENCIAL = "mp"
    MODALIDAD_ONLINE = "mo"

    MODALIDADES_CHOICES = (
        (MODALIDAD_PRESENCIAL, "Modalidad Presencial"),
        (MODALIDAD_ONLINE, "Modalidad Online"),
    )

    nombre = models.CharField(max_length=2, choices=MODALIDADES_CHOICES)

    class Meta:
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"

    def __str__(self):
        return self.get_nombre_display()


class Horario(models.Model):

    sede = models.ForeignKey(to=Sede, on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    dias_clase = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __str__(self):
        return f'Sede {self.sede.siglas} "{self.dias_clase} de {self.hora_inicio:%H:%M} - {self.hora_fin:%H:%M}"'


class Estudiante(models.Model):

    ANYO_ESTUDIO_QUINTO = "quinto"
    ANYO_ESTUDIO_BACHILLERATO = "bachillerato"

    ANYO_ESTUDIO_CHOICES = (
        (ANYO_ESTUDIO_QUINTO, "Quinto Año de Bachillerato"),
        (ANYO_ESTUDIO_BACHILLERATO, "Bachiller Graduado"),
    )

    primer_nombre = models.CharField(max_length=15)
    segundo_nombre = models.CharField(max_length=15, null=True, blank=True)
    primer_apellido = models.CharField(max_length=15)
    segundo_apellido = models.CharField(max_length=15, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=8)
    nombre_colegio = models.CharField(max_length=30)
    nombre_padre = models.CharField(max_length=60)
    telefono_padre = models.CharField(max_length=8)
    anyo_estudio = models.CharField(max_length=12, choices=ANYO_ESTUDIO_CHOICES)
    foto_carnet = models.FileField(upload_to="adjuntos/carnet")
    copia_identidad = models.FileField(upload_to="adjuntos/identidad")
    certificado = models.FileField(upload_to="adjuntos/certificado")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"


class Matricula(models.Model):

    estudiante = models.OneToOneField(to=Estudiante, on_delete=models.CASCADE)
    modalidad = models.ForeignKey(to=Modalidad, null=True, blank=True, on_delete=models.SET_NULL)
    horario = models.ForeignKey(to=Horario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

    def __str__(self):
        return self.id
