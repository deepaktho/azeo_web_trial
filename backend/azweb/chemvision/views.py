# Create your views here.
from django.shortcuts import render
import datetime
from .forms import Chemvision_Form
from .models import Chemvisionuser
from registration_ca.models import Azeo_id_user
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def Lecture_1(request):
    return render(request, "chemvision/lecture_1.html")

def Lecture_2(request):
    return render(request, "chemvision/lecture_2.html")

def Lecture_3(request):
    return render(request, "chemvision/lecture_3.html")

def Lecture_4(request):
    return render(request, "chemvision/lecture_4.html")

def Lecture_5(request):
    return render(request, "chemvision/lecture_5.html")

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'chemvision/registration.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Chemvision_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if  not (Azeo_id_user.objects.filter(azeo_id=form.cleaned_data['member1']).exists()) :

                return render(request, template, {
                        'form': form,
                        'error_message': 'AZeo-ID does not exist for member 1'
                    })
            elif Chemvisionuser.objects.filter(member1=form.cleaned_data['member1']).exists() :
                return render(request, template, {
                    'form': form,
                    'error_message': 'Member 1 already registered.'
                })
            else:
                # print('hellow world')
                # Create the user:

                # user = User.objects.create_user(
                #     # form.cleaned_data['username'],
                #     form.cleaned_data['email']

                # )


                extendeduser = Chemvisionuser()
                extendeduser.member1 = form.cleaned_data['member1']





                # extendeduser.user = user
                # extendeduser.save()

                subject = "Successfully registered for Chemvision Lecture Series"
                # message = f'congratulations {extendeduser.first_name}{extendeduser.last_name} have successfully registered on CA portal'
                azeo_id1 = str(extendeduser.member1)

                # sql_query = 'SELECT id, email FROM registration_ca_Azeo_id_user WHERE azeo_id = {azeo_id}'

                # to_email = Azeo_id_user.objects.raw(sql_query.format(azeo_id = azeo_id1))

                to_email = Azeo_id_user.objects.get(azeo_id = azeo_id1).email



                # for person in to_email:

                # tmp = to_email[0]
                # my_email = to_email[0].email

                # to_email = str(to_email).strip()

                name1 = Azeo_id_user.objects.get(azeo_id = azeo_id1).first_name

                html_message = render_to_string("chemvision/mail.html",{'name':name1})
                message = strip_tags(html_message)

                email3 = EmailMultiAlternatives(subject,
                            message,
                            'azeo2022@gmail.com',
                            [to_email],
                            )
                email3.attach_alternative(html_message,'text/html')
                email3.send()

                # send_mail(
                #             subject,
                #             message,
                #             from_email,
                #             [to_email],
                #             fail_silently=False,
                #         )
                extendeduser.save()

                return render(request, "chemvision/confirmation.html",)




                # redirect to home page:
                #return redirect('registration_ca:index')

   # No post data availabe, let's just show the page.
    else:
        form = Chemvision_Form()

    return render(request, template, {'form': form})

