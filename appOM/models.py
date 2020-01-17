from django.db import models
from datetime import *

# Model za kreiranje doktora

class Dr(models.Model):
    dr = models.CharField(max_length=50)

    def __str__(self):
        return self.dr
    
# Model za kreiranje pacijenta

class Pacijent(models.Model):
    ime = models.CharField(default='', max_length=50)
    prezime = models.CharField(default='', max_length=50)
    email = models.CharField(default='example@example.com', max_length=50)
    telefon = models.CharField(default='', max_length=50)
    def __str__(self):
        return '%s %s' %(self.ime,self.prezime)

# Model za zakazivanje

class Zakazivanje(models.Model):
    ime_prezime = models.ForeignKey("Pacijent", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    time_start = models.TimeField(default='')
    time_end = models.TimeField(default='')
    text = models.TextField(default='text',max_length=900)
    dr = models.ForeignKey("Dr", on_delete=models.CASCADE, blank=True, null=True )
    zavrseno = models.BooleanField(default=False)

    def __str__(self):
        return "%s" %(self.ime_prezime)


# Model za dodavanje Beleski

class Pacijent_Memo(models.Model):
    idpacijenta = models.ForeignKey("Pacijent", on_delete=models.CASCADE,blank=True, null=True )
    memo_pacijent = models.TextField(default="",max_length=900 )
    datee = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return "%s" %(self.idpacijenta)

# Model za dodavanje dokumenata

class Pacijent_File(models.Model):
    imepacijenta = models.ForeignKey("Pacijent", on_delete=models.CASCADE)
    opis = models.CharField(default="", max_length=50)
    fajl = models.FileField(upload_to='File/pdf')
    datum = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.opis
    

# Model za dodavanje slika