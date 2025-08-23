import random
from .models import registrations
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from humayan.forms import registration_forms
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import check_password
from services.models import footer,homepage_banner,homepage_box,homepage_box2



# Create your views here.


def regview(request):
    foot = footer.objects.all()                    
    banner = homepage_banner.objects.first()
    box=homepage_box.objects.all() 
    box2=homepage_box2.objects.all()  
       

    context = {
        'foot': foot,
        'banner': banner,
        'box':box,
        'box2':box2,
    }
    return render(request, 'homepage.html', context)

def profileview(request):
    if not request.session.get('user_id'):
        return redirect('/') 

    user = registrations.objects.get(id=request.session['user_id'])
    
    context = {
        'user': user
    }
    return render(request, 'profileview.html', context)
 

def registration(request):
    if request.method=='POST':
        fr=registration_forms(request.POST)
        if fr.is_valid():
         fr.cleaned_data
                                       #hash password
         user = fr.save(commit=False)         
         user.Pass = make_password(fr.cleaned_data['Pass'])
         user.Repass = make_password(fr.cleaned_data['Repass'])
         user.save() 
         return HttpResponseRedirect('/homepage')
    
    else:
     fr= registration_forms(auto_id=True)
    return render(request,'reg.html', {'fo':fr})
 



def loging(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # database থেকে user বের করা
            user = registrations.objects.get(Email=email)

            # hashed password check করা
            if check_password(password, user.Pass):
                # ✅ success হলে session এ user info রাখা
                request.session['user_id'] = user.id
                request.session['username'] = user.Name
                return HttpResponseRedirect('/homepage/')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        
        except registrations.DoesNotExist:
            return render(request, 'login.html', {'error': 'User not found'})
    
    return render(request, 'login.html')



def logout_view(request):
    # session clear করে logout করানো
    auth_logout(request)
    return redirect('')   





def password_change(request):
    if request.session.get('user_id'):  # ✅ session দিয়ে check
        if request.method == "POST":
            old_password = request.POST.get("old_password")
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")

            try:
                user = registrations.objects.get(id=request.session['user_id'])

                # পুরোনো password check
                if not check_password(old_password, user.Pass):
                    return render(request, 'cpass.html', {'error': 'Old password is incorrect'})

                if new_password != confirm_password:
                    return render(request, 'cpass.html', {'error': 'Passwords do not match'})

                # নতুন password hash করে save
                user.Pass = make_password(new_password)
                user.Repass = user.Pass  # confirm field update
                user.save()

                return HttpResponseRedirect('succ/')
            except registrations.DoesNotExist:
                return HttpResponseRedirect('/log/')

        return render(request, 'cpass.html')
    else:
        return HttpResponseRedirect('/log/')
    




# 1. Forgot password -> Email দিয়ে OTP পাঠানো
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = registrations.objects.get(Email=email)

            # 6 digit OTP generate
            otp = random.randint(100000, 999999)

            # session এ save করা
            request.session['reset_email'] = email
            request.session['reset_otp'] = str(otp)

            # Email পাঠানো
            send_mail(
                'Password Reset OTP',
                f'Your OTP is {otp}',
                'your_email@gmail.com',   # settings.py এ সেট করা email
                [email],
                fail_silently=False,
            )

            return redirect('verify_otp')  # Next page
        except registrations.DoesNotExist:
            return render(request, 'forgot.html', {'error': 'Email not found'})

    return render(request, 'forgot.html')


# 2. OTP Verify + New Password Set
def verify_otp(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        new_pass = request.POST.get("new_pass")
        confirm_pass = request.POST.get("confirm_pass")

        # OTP match check
        if otp == request.session.get('reset_otp'):
            if new_pass == confirm_pass:
                email = request.session.get('reset_email')
                user = registrations.objects.get(Email=email)

                # Password hash করে save
                user.Pass = make_password(new_pass)
                user.Repass = user.Pass
                user.save()

                # Session clear
                del request.session['reset_email']
                del request.session['reset_otp']

                return redirect('/log/')
            else:
                return render(request, 'verify.html', {'error': 'Passwords do not match'})
        else:
            return render(request, 'verify.html', {'error': 'Invalid OTP'})

    return render(request, 'verify.html')



from .forms import ProfileUpdateForm

def profile_settings(request):
    if not request.session.get('user_id'):
        return redirect('/log/')

    user = registrations.objects.get(id=request.session['user_id'])

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            profile = form.save(commit=False)

            # যদি ফাইল না আসে, আগের ফাইল retain করা
            if not request.FILES.get('profile_pic'):
                profile.profile_pic = user.profile_pic

            profile.save()
            return redirect('/homepage/')
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'settings.html', {'form': form, 'user': user})



#Home view

from django.shortcuts import render
from .models import registrations

def home(request):
    return render(request, 'home.html' )
   
