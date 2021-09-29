from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/login/')
def logOut(request, *args, **kwargs):
    logout(request)
    return redirect(userLogin)

def userLogin(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(dashboard)

    return render(request, 'SkyTravel/login.html')


def userRegistration(request, *args, **kwargs):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if first_name and last_name and username and email and password:
            user = User.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name, password=password)

            if user:
                login(request, user)
                return redirect(dashboard)
            else:
                context = {
                    'error': "Username is already taken, please choose another username and try again!"
                }
                return render(request, 'SkyTravel/error.html', context)
        else:
            context = {
                'error': "Please fill up all the fields and try again!"
            }
            return render(request, 'SkyTravel/error.html', context)
    return render(request, 'SkyTravel/registration.html')

@login_required(login_url='/login/')
def dashboard(request, *args, **kwargs):
    return render(request, 'SkyTravel/dashboard.html')

@login_required(login_url='/login/')
def air(request, *args, **kwargs):
    airchart = AirChart.objects.all()
    context = {
        'airchart': airchart,
    }
    return render(request, 'SkyTravel/air.html', context)

@login_required(login_url='/login/')
def bus(request, *args, **kwargs):
    buschart = BusChart.objects.all()
    context = {
        'buschart': buschart,
    }
    return render(request, 'SkyTravel/bus.html', context)

@login_required(login_url='/login/')
def bookTripAir(request, id):
    if request.method == "POST":
        tripid = request.POST['id']
        date = request.POST['date']
        adult = request.POST['adult']
        child = request.POST['child']
        baby = request.POST['baby']
        if date and adult and child and baby:
            adult = int(adult)
            baby = int(baby)
            child = int(child)
            if not adult == 0:
                trip = AirChart.objects.get(id=tripid)
                adultcost = trip.adultcost
                childcost = trip.childcost
                total = (adult * adultcost) + (child * childcost)
                user = User.objects.get(id=request.user.id)
                airtrip = AirTrip.objects.create(user=user, flight=trip, adult=adult, child=child, baby=baby, departureDate=date, totalcost=total, payment="Incomplete")
                context = {
                    'flight': airtrip,
                    'trip': trip,
                    'user': user,
                    'tripby': "Air"
                }
                return render(request, 'SkyTravel/checkout.html', context)
            else:
                context = {
                    'error': "Trip can't be booked without any Adult Member!"
                }
                return render(request, 'SkyTravel/error.html', context)
        else:
            context = {
                'error': "Please fill up all the fields (Date, Adult, Child, Baby) and try again!"
            }
            return render(request, 'SkyTravel/error.html', context)
    trip = AirChart.objects.get(id=id)
    context = {
        'trip': trip,
        'tripby': "Air"
    }
    return render(request, 'SkyTravel/tripform.html', context)


@login_required(login_url='/login/')
def bookTripBus(request, id):
    if request.method == "POST":
        tripid = request.POST['id']
        date = request.POST['date']
        adult = request.POST['adult']
        child = request.POST['child']
        baby = request.POST['baby']
        if date and adult and child and baby:
            adult = int(adult)
            baby = int(baby)
            child = int(child)
            if not adult == 0:
                trip = BusChart.objects.get(id=tripid)
                adultcost = trip.adultcost
                childcost = trip.childcost
                total = (adult * adultcost) + (child * childcost)
                user = User.objects.get(id=request.user.id)
                bustrip = BusTrip.objects.create(user=user, flight=trip, adult=adult, child=child, baby=baby, departureDate=date, totalcost=total, payment="Incomplete")
                context = {
                    'flight': bustrip,
                    'trip': trip,
                    'user': user,
                    'tripby': "Bus"
                }
                return render(request, 'SkyTravel/checkout.html', context)
            else:
                context = {
                    'error': "Trip can't be booked without any Adult Member!"
                }
                return render(request, 'SkyTravel/error.html', context)
        else:
            context = {
                'error': "Please fill up all the fields (Date, Adult, Child, Baby) and try again!"
            }
            return render(request, 'SkyTravel/error.html', context)
    trip = BusChart.objects.get(id=id)
    context = {
        'trip': trip,
        'tripby': "Bus",
    }
    return render(request, 'SkyTravel/tripform.html', context)


@login_required(login_url='/login/')
def payAir(request, id):
    context = {
        'id': id,
    }
    if request.method == "POST":
        id = request.POST['id']
        airtrip = AirTrip.objects.get(id=id)
        airtrip.payment = "Complete"
        airtrip.save()
        return redirect(mytripAir)
    return render(request, 'SkyTravel/pay.html',  context)


@login_required(login_url='/login/')
def payBus(request, id):
    context = {
        'id': id,
    }
    if request.method == "POST":
        id = request.POST['id']
        bustrip = BusTrip.objects.get(id=id)
        bustrip.payment = "Complete"
        bustrip.save()
        return redirect(mytripBus)
    return render(request, 'SkyTravel/pay.html', context)


@login_required(login_url='/login/')
def mytripAir(request, *args, **kwargs):
    uid = request.user.id
    user = User.objects.get(id=uid)
    trip = AirTrip.objects.filter(user=user).order_by('departureDate')

    context = {
        'trip': trip,
        'tripby': "Air"
    }

    return render(request, 'SkyTravel/mytrip.html', context)


@login_required(login_url='/login/')
def mytripBus(request, *args, **kwargs):
    uid = request.user.id
    user = User.objects.get(id=uid)
    trip = BusTrip.objects.filter(user=user).order_by('departureDate')

    context = {
        'trip': trip,
        'tripby': "Bus"
    }

    return render(request, 'SkyTravel/mytrip.html', context)


@login_required(login_url='/login/')
def incompleteAir(request, *args, **kwargs):
    uid = request.user.id
    user = User.objects.get(id=uid)
    trip = AirTrip.objects.filter(payment="Incomplete", user=user).order_by('departureDate')

    context = {
        'trip': trip,
        'tripby': "Air"
    }

    return render(request, 'SkyTravel/incompletepay.html', context)


@login_required(login_url='/login/')
def incompleteBus(request, *args, **kwargs):
    uid = request.user.id
    user = User.objects.get(id=uid)
    trip = BusTrip.objects.filter(payment="Incomplete", user=user).order_by('departureDate')

    context = {
        'trip': trip,
        'tripby': "Bus"
    }

    return render(request, 'SkyTravel/incompletepay.html', context)


@login_required(login_url='/login/')
def busticket(request, id):
    uid = request.user.id
    user = User.objects.get(id=uid)
    bustrip = BusTrip.objects.get(id=id)
    context = {
            'flight': bustrip,
            'trip': bustrip.flight,
            'user': user,
            'tripby': "Bus"
        }
    return render(request, 'SkyTravel/ticket.html', context)


@login_required(login_url='/login/')
def airticket(request, id):
    uid = request.user.id
    user = User.objects.get(id=uid)
    airtrip = AirTrip.objects.get(id=id)
    context = {
            'flight': airtrip,
            'trip': airtrip.flight,
            'user': user,
            'tripby': "Air"
        }
    return render(request, 'SkyTravel/ticket.html', context)



@login_required(login_url='/login/')
def businvoice(request, id):
    uid = request.user.id
    user = User.objects.get(id=uid)
    bustrip = BusTrip.objects.get(id=id)
    context = {
            'flight': bustrip,
            'trip': bustrip.flight,
            'user': user,
            'tripby': "Bus"
        }
    return render(request, 'SkyTravel/invoice.html', context)


@login_required(login_url='/login/')
def airinvoice(request, id):
    uid = request.user.id
    user = User.objects.get(id=uid)
    airtrip = AirTrip.objects.get(id=id)
    context = {
            'flight': airtrip,
            'trip': airtrip.flight,
            'user': user,
            'tripby': "Air"
        }
    return render(request, 'SkyTravel/invoice.html', context)

