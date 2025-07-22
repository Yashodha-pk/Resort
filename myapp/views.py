from idlelib.autocomplete import FILES

from django.shortcuts import render,redirect
from myapp.models import register,Event,Pay

# Create your views here.
def Home(request):
    return render(request,"home.html")


def Register(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        email=request.POST.get("email")
        pwd=request.POST.get("pwd")
        phn=request.POST.get("phn")
        reg=register.objects.create(fname=fname,email=email,
                                    pwd=pwd,Phn=phn)
        reg.save()
        msg="Registered succussfully..."

        return render(request, "register.html",{'msg':msg})
    return render(request, "register.html")



def Login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        if email=='admin@gmail.com' and pwd=='admin':
            return render(request,"adminpage.html")
        data=register.objects.all()
        is_present=False
        for d in data:
            if d.email==email and d.pwd==pwd:
                request.session["id"]=d.id
                name=d.fname
                email=d.email
                phn=d.Phn
                is_present=True
                break
        if is_present:
            return render(request,"user_page.html",{"name":name,"email":email,"phn":phn })
        else:
            msg="invalid username and password"
            return render(request,"login.html",{"msg":msg})


    return render(request,"login.html")


def admindashboard(request):
    return render(request,"adminpage.html")


def customerdetails(request):
    Data = register.objects.all()
    return render(request,"customerdetails.html",{"Data":Data})

def userdashboard(request):
    Data=register.objects.all()
    userid=request.session['id']
    for d in Data:
        if d.id == userid:
            name =d.fname
            email=d.email
            Phn=d.Phn
            break
    return render (request,"user_page.html",{"name":name,"email":email,"phone":Phn})


def Addevent(request):
    if request.method=="POST":
        etype=request.POST.get("etype")
        eroom=request.POST.get("eroom")
        eimage=request.FILES.get("eimage")
        eprice=request.POST.get("eprice")
        edes=request.POST.get("edes")
        if eimage:
            add_event=Event(etype=etype,eroom=eroom,eimage=eimage,eprice=eprice,edes=edes)
            add_event.save()
            msg="Event Added"
            return render(request, "Addevent.html",{"msg":msg})

    return render(request,"Addevent.html")

def Eventlist(request):
    data=Event.objects.all()
    return render(request,"Eventlist.html",{"data":data})


def Deleteevent(request,id):
    delete_event=Event.objects.get(id=id)
    delete_event.delete()
    return redirect("Eventlist")

def Updateevent(request,id):
    u_event=Event.objects.get(id=id)
    return render(request,"Updateevent.html",{"u_event":u_event})


def U_Event(request,id):
    up_event=Event.objects.get(id=id)
    etype=request.POST.get("etype")
    eimage=request.FILES.get("eimage")
    eprice=request.POST.get("eprice")
    edes=request.POST.get("edes")

    if eimage in request.FILES:
        up_event.eimage = eimage

    up_event.etype=etype
    up_event.eprice=eprice
    up_event.edes=edes
    up_event.save()
    return redirect("Eventlist")

def AvailableEvent(request):
    data=Event.objects.all()
    return render(request,"Available.html",{"data":data})


def Book_event(request,id):
    userid=request.session['id']
    data=Event.objects.get(id=id)
    print("data=",data)
    return render(request,"View_event.html",{'data':data,'userid':userid})

def Payment_success(request):
    return render(request,"Payment_success.html")

def Payment(request,id):
    user_id=request.session['id']
    data=Event.objects.get(id=id)

    if request.method=="POST":
        cardnum = request.POST.get('cardnum')
        cvvnum = request.POST.get('cvvnum')
        edate = request.POST.get('edate')
        eid = request.POST.get('eid')
        etype = request.POST.get('etype')
        eprice = request.POST.get('eprice')

        print(eid)
        payment=Pay.objects.create(userid=user_id,cardnum=cardnum,cvvnum=cvvnum,
                                   edate=edate,eid=eid,etype=etype,eprice=eprice)
        payment.save()
        return redirect("Payment_success")
    return render(request,"Payment.html",{"data":data,"user_id":user_id})

def Orderlist(request):
    data=Pay.objects.all()
    return render(request,"Orderlist.html",{"data":data})


def Logout(request):
    request.session.clear()
    return render(request,"home.html")

