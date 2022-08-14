from django.shortcuts import render,redirect
# Imports for the models, serializers
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.models import User
from .models import NewUser, Otp
# Imports For the api
import requests
# Imports for Otp and Mail
from django.core.mail import send_mail
import math
import random

#import forms from form.py
from .forms import LoginForm

User = get_user_model()

def get_reg(request):
    error = None
    # Generates The OTP
    def generate_otp():
        digits = '0123456789'
        otp = ''
        for i in range(6):
            otp+=digits[math.floor(random.random()*10)]
        print(otp)
        return otp
    if request.method == 'POST':
        registration_number = request.POST['reg_number']
        # Checks if the registration is already a user and returns to the reg page with a message if it is
        try:
            # if str(registration_number) == str(NewUser.objects.filter(reg_number=registration_number).values('reg_number')[0]['reg_number']):
            if NewUser.objects.filter(reg_number=registration_number).exists():
    
                print('You Are Already A User')
                return render(request, 'get_reg.html', {'already_user':'You Are Already A User, Try Logging In'})
        except:
            None

        # Pull the result from the api and checks for a user with the Reg Number    
        response = requests.get('https://onecubestudents.herokuapp.com/student/')
        ans = response.json()
        for i in ans:
            if i['registration_number'] == registration_number:
                student = {
                    'email': i['email'],
                    'first_name': i['first_name'],
                    'registration_number': i['registration_number'],
                }
                if not Otp.objects.filter(registration_number=student['registration_number']):
                    otp = generate_otp()
                    add_otp = Otp.objects.create(registration_number=student['registration_number'], otp_code=otp)
                    send_mail(
                        'Onecube Otp',
                        f'{otp} is your Otp',
                        'projectcolfilms@gmail.com',
                        [student['email']],
                        fail_silently=False
                    )
                else:
                    print('Otp already Exists')

                pret = Otp.objects.filter(registration_number=student['registration_number']).values('otp_code')[0]['otp_code']
                print(pret)
                
                request.session['session'] = request.POST # Passes the session data containing reg_number to the redirect
                return redirect('get_otp')

                # Return error message if reg number does notmatch
            elif i['registration_number'] != registration_number and registration_number == '':
                error = "Reg Number Can't Be Empty"

            elif i['registration_number'] != registration_number:
                error = 'No Reg Number Match'

        return render(request, 'get_reg.html', {'error':error})
    return render(request, 'get_reg.html', {})
    

def get_otp(request):
    error = None
    session = request.session.get('session')
    if not session:
        access_error = "You're Not Authorized To Be Here !!!"
        return render(request, 'get_otp.html', {'access_error':access_error})
    else:
        # Load The Session Data from the reg page 
        reg = session['reg_number']# Picks the reg_number from the session and passes it into the data loaded on the otp page
        pret = Otp.objects.filter(registration_number=reg).values('otp_code')[0]['otp_code']
        otp_num = pret

        if request.method == 'POST':
            otp1 = request.POST['otp1']
            otp2 = request.POST['otp2']
            otp3 = request.POST['otp3']
            otp4 = request.POST['otp4']
            otp5 = request.POST['otp5']
            otp6 = request.POST['otp6']
            otp = otp1+otp2+otp3+otp4+otp5+otp6
            # otp = request.POST['otp']
            if str(otp) == str(otp_num):
                Otp.objects.filter(registration_number=reg).delete()
                request.session['session'] = request.POST
                return redirect('create_user')
            elif str(otp) != str(otp_num):
                error = 'Not Valid OTP'
                return render(request, 'get_otp.html', {'data':reg, 'error':error})
    return render(request, 'get_otp.html', {'data':reg, 'error':error}) # Loads the reg_number and passes it as a value in the otp template.

def create_user(request):
    error = None
    no_permission = None
    # Load The Session Data from the reg page and pass the data into the return context
    session = request.session.get('session')
    if not session:
        access_error = "You're Not Authorized To Be Here !!!"
        return render(request, 'create_user.html', {'access_error':access_error})
    else:
        reg = session['reg']
        print(session)
        if request.method == 'POST':
            registration_number = request.POST['reg']
            user_name = request.POST.get('username')
            password = request.POST.get('password1')
            password2 = request.POST.get('password2')
            response = requests.get('https://onecubestudents.herokuapp.com/student/')
            ans = response.json()
            for i in ans:
                # Pull the result from the api and create a user with the details
                if i['registration_number'] == registration_number:
                    student = {
                        'first_name': i['first_name'],
                        'last_name': i['last_name'],
                        'email': i['email'],
                        'institution': i['institution_name'],
                        'registration_number': i['registration_number'],
                    }
                    # Check if the email is already in the database if it is don't create another one
                    try:
                        if str(student['email']) != str(NewUser.objects.get(email=student['email'])):
                            '''we are expected to get an error here as the email is not in the user db. so this error confirms 
                            that the person registering is not in our database already and proceeds to register him'''
                    except:
                        if password == password2:
                            User.objects.create_user(email=str(student['email']), password=password)
                        else:
                            password_error = 'Both Passwords Must Match'
                            return render(request, 'create_user.html', {'password_error':password_error})
                    else:
                        print('user already exists')
                        pass

                        '''
                        After the user email and password is created above, we then pull the remaining data 
                        from the api and append them to the user's profile.
                        '''
                    # if str(student['email']) == str(NewUser.objects.get(email=student['email'])):
                    if NewUser.objects.filter(email=student['email']).exists():
    
                        print('yes')
                        ret = NewUser.objects.filter(email=str(student['email']))
                        ret.update(
                                username = user_name,
                                first_name=student['first_name'],
                                last_name=student['last_name'],
                                college_name=student['institution'],
                                reg_number=student['registration_number'],
                        )
                        pret = NewUser.objects.filter(email=str(student['email']))
                        prat = pret.values_list('id')
                        success = 'Your Registration Was Successful'
                        return render(request, 'create_user.html', {'success':success})
                    else:
                        pass
                elif i['registration_number'] != registration_number:
                    error = 'No Reg Number Match'

                else:
                    student = {}
            else:
                pass

    return render(request, 'create_user.html', {'data':reg, 'error':error, 'no_permission':no_permission})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('emailInput','')
        password = request.POST.get('password','')
        user = authenticate(request, email = email, password = password)
        if user is not None:
            
            login(request, user)
        #redirect to dashboard
            return redirect("dashboard", user.id)
        else:
            messages.info(request, "Email or password is incorrect")
    return render(request, 'sign_in.html')

def user_logout(request):
    logout(request)
    return redirect('home')