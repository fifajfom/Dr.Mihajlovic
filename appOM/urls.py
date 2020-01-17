#login urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.zakazivanjeV, name='home'),
    # Dodavanje pacijenata
    path('DodavanjePacijenta',views.addPacijentV, name='addpacijent'),
    path('DodavanjePacijenta/<int:pk>',views.editPacijentV, name='edit_pacijent'),
    path('DodavanjePacijenta/delete/<int:pk>',views.deletePacijentV, name='delete_pacijent'),
    # Zakazivanje
    path('zakazivanje',views.zakazivanjeTEST, name='zakazivanje'),
    path('zakazivanjek/<int:zak_pk>', views.completeZak, name='complete'),
    path('zakazivanjen/<int:zak_pk>', views.notcompleteZak, name='notcomplete'),
    path('zakazivanje/delete/<int:pk>',views.deleteZak, name='deleteZak'),
    path('zakazivanje/edit/<int:pk>',views.editZak, name='editZak'),
    # Pacijent
    path('pacijent/<int:pk>',views.PacijentAll, name='pacijent'),
    path('pacijent/file/', views.PacijentFile, name='upload'),
    path('pacijent/file/delete/<int:pk>',views.deletePacijentFile, name='deleteFile'),
    # Memo
    path('pacijent/memo/<int:pk>',views.editMemo, name='editMemo'),
    path('pacijent/addmemo/',views.addMemo, name='addMemo'),
    path('pacijent/memo/delete/<int:pk>',views.deleteMemo, name='deleteMemo'),
]

# VAZNO media mora da se dodaje u glavnom url fajlu