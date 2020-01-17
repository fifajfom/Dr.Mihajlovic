from django.contrib import admin
from . models import Pacijent, Zakazivanje,Pacijent_Memo,Pacijent_File,Dr
# Register your models here.
admin.site.register(Pacijent)
admin.site.register(Zakazivanje)
admin.site.register(Pacijent_Memo)
admin.site.register(Pacijent_File)
admin.site.register(Dr)