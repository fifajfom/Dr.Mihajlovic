from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import addPacijentForm, ZakazivanjeqForm, Pacijent_MemoForm,Pacijent_FileForm
from .models import Pacijent,Zakazivanje,Pacijent_Memo,Pacijent_File
from django.http import HttpResponseRedirect

@login_required
def addPacijentV(request):
    query_results = Pacijent.objects.all()

    if request.method == 'POST':
        filled_form = addPacijentForm(request.POST)  # za prihvatanje fajlova
        if filled_form.is_valid():
            #cuva u bazu
            #filled_form.save()
            created_pacijent = filled_form.save()
            created_pacijent_pk = created_pacijent.id
            note = "Uspesno ste dodali novog pacijenta %s %s sa email adresom %s " %(filled_form.cleaned_data['ime'],
            filled_form.cleaned_data['prezime'],
            filled_form.cleaned_data['email'],)
            filled_form = addPacijentForm()
        else:   #ukoliko nije validan input  u html-u se postavlja novalidate
            created_pacijent_pk = None
            note = 'Niste uspeli da dodate novog pacijenta'
        return render(request,'appOM/addpatient.html', {'pacijent_pk':created_pacijent_pk,'pacijentform':filled_form, 'note':note,'query_results':query_results})
    else:
        form = addPacijentForm()
        return render(request,'appOM/addpatient.html', {'pacijentform':form,'query_results':query_results})
        
@login_required
def editPacijentV(request,pk):
    pacijent = Pacijent.objects.get(pk=pk)
    form = addPacijentForm(instance=pacijent)
    if request.method == 'POST':
        filled_form = addPacijentForm(request.POST, instance=pacijent)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            #note = 'Pacijent je uređen'
            return redirect('addpacijent')
    return render(request,'appOM/editpatient.html',{'form':form,'pacijent':pacijent})

@login_required
def deletePacijentV(request,pk):
    Pacijent.objects.filter(pk=pk).delete()
    return redirect('addpacijent')


@login_required
def zakazivanjeV(request):
    query_results = Zakazivanje.objects.all().order_by('date','time_start')

    if request.method == 'POST':
        filled_form = ZakazivanjeqForm(request.POST)  # za prihvatanje fajlova
        if filled_form.is_valid():
            #cuva u bazu
            #filled_form.save()
            created_zakazivanje = filled_form.save()
            created_zakazivanje_pk = created_zakazivanje.id
            note = " Uspesno ste dodali novog pacijenta %s %s sa email adresom %s " %(filled_form.cleaned_data['ime_prezime'],
            filled_form.cleaned_data['date'],
            filled_form.cleaned_data['time_start'],
            filled_form.cleaned_data['time_end'],
            filled_form.cleaned_data['text'],
            )
            filled_form = ZakazivanjeqForm()
        else:   #ukoliko nije validan input  u html-u se postavlja novalidate
            created_zakazivanje_pk = None
            note = 'Niste uspeli da dodate novog pacijenta'
        return render(request,'appOM/home.html', {'zakazivanje_pk':created_zakazivanje_pk,'zakazivanjeform':filled_form, 'note':note,'query_results':query_results})
    else:
        form = ZakazivanjeqForm()
        return render(request,'appOM/home.html', {'zakazivanjeform':form,'query_results':query_results})

@login_required
def zakazivanjeTEST(request):
    query_results = Zakazivanje.objects.all().order_by('date')

    if request.method == 'POST':
        filled_form = ZakazivanjeqForm(request.POST)  # za prihvatanje fajlova
        if filled_form.is_valid():
            created_zakazivanje = filled_form.save()
            created_zakazivanje_pk = created_zakazivanje.id
            note = " Uspesno ste zakazali termin"  
            filled_form = ZakazivanjeqForm()
        else:   #ukoliko nije validan input  u html-u se postavlja novalidate
            created_zakazivanje_pk = None
            note = 'Niste uspeli da zakažete'
        return render(request,'appOM/zakazivanje.html', {'zakazivanje_pk':created_zakazivanje_pk,'zakazivanjeform':filled_form, 'note':note,'query_results':query_results})
    else:
        form = ZakazivanjeqForm()
        return render(request,'appOM/zakazivanje.html', {'zakazivanjeform':form,'query_results':query_results})

@login_required
def completeZak(request,zak_pk):
    pacijent =Zakazivanje.objects.get(pk=zak_pk)
    pacijent.zavrseno = True
    pacijent.save()
    return redirect('home')

@login_required
def notcompleteZak(request,zak_pk):
    pacijent =Zakazivanje.objects.get(pk=zak_pk)
    pacijent.zavrseno = False
    pacijent.save()
    return redirect('home')

@login_required
def deleteZak(request,pk):
    Zakazivanje.objects.filter(pk=pk).delete()
    return redirect('home')

@login_required
def editZak(request,pk):
    zak = Zakazivanje.objects.get(pk=pk)
    form = ZakazivanjeqForm(instance=zak)
    if request.method == 'POST':
        filled_form = ZakazivanjeqForm(request.POST, instance=zak)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            #note = 'Pacijent je uređen'
            # return redirect('pacijent',pk=zak.ime_prezime_id)
            return redirect('home')
    return render(request,'appOM/editzak.html',{'form':form,'zak':zak})

######################## Pacijent ##############################
@login_required
def deleteMemo(request,pk):
    Pacijent_Memo.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def editMemo(request,pk):
    memo = Pacijent_Memo.objects.get(pk=pk)
    form = Pacijent_MemoForm(instance=memo)
    if request.method == 'POST':
        filled_form = Pacijent_MemoForm(request.POST, instance=memo)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            #note = 'Pacijent je uređen'
            return redirect('pacijent',pk=memo.idpacijenta_id)
    return render(request,'appOM/editmemo.html',{'form':form,'memo':memo})

@login_required
def addMemo(request):

    if request.method == 'POST':
        filled_form = Pacijent_MemoForm(request.POST)  # za prihvatanje fajlova
        if filled_form.is_valid():
            #cuva u bazu
            #filled_form.save()
            created_pacijent = filled_form.save()
            created_pacijent_pk = created_pacijent.id
            filled_form = Pacijent_MemoForm()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:   #ukoliko nije validan input  u html-u se postavlja novalidate
            created_pacijent_pk = None
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = Pacijent_MemoForm()
        return render(request,'appOM/addmemo.html', {'pacijentform':form})

@login_required
def deleteMemo(request,pk):
    Pacijent_Memo.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def PacijentAll(request,pk):
    query_memo = Pacijent_Memo.objects.filter(idpacijenta=pk)
    query_zak = Zakazivanje.objects.filter(ime_prezime=pk)
    query_pac = Pacijent.objects.filter(id=pk)
    query_file = Pacijent_File.objects.filter(imepacijenta=pk)
    return render(request,'appOM/pacijent.html',{'query_memo':query_memo,'query_zak':query_zak,'query_pac':query_pac,'query_file':query_file})


# za prihvatanje fajlova

@login_required
def PacijentFile(request):
    query_results = Pacijent_File.objects.all().order_by('-datum')
    if request.method == 'POST':
        filled_form = Pacijent_FileForm(request.POST,request.FILES)  # za prihvatanje fajlova
        if filled_form.is_valid():
            #cuva u bazu
            #filled_form.save()
            created_file = filled_form.save()
            created_file_pk = created_file.id
            note = " Uspesno ste dodali dokument"  
            filled_form = Pacijent_FileForm()
        else:   #ukoliko nije validan input  u html-u se postavlja novalidate
            created_file_pk = None
            note = 'Niste uspeli da dodate dokument'
        return render(request,'appOM/upload_file.html', {'file_pk':created_file_pk,'fileform':filled_form, 'note':note,'query_results':query_results})
    else:
        form = Pacijent_FileForm()
        return render(request,'appOM/upload_file.html', {'fileform':form,'query_results':query_results})

@login_required
def deletePacijentFile(request,pk):
    Pacijent_File.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


