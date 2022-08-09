from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import Qviz_it_iitb_Form
from .forms import Qviz_it_non_iitb_Form
from .models import Qviz_it_iitb
from .models import Qviz_it_noniitb
from registration_ca.models import Azeo_id_user
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random



# Create your views here.

def Leaderboard(request):
    return render(request,"qviz_it/leaderboard.html",)

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'qviz_it/registration_iitb.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Qviz_it_iitb_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if not Azeo_id_user.objects.filter(azeo_id=form.cleaned_data['member1']).exists():

                return render(request, template, {
                        'form': form,
                        'error_message': 'AZeo-ID does not exist'
                    })

            if Qviz_it_iitb.objects.filter(member1=form.cleaned_data['member1']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'You are already registered.'
                })





            else:
                # print('hellow world')
                # Create the user:

                # user = User.objects.create_user(
                #     # form.cleaned_data['username'],
                #     form.cleaned_data['email']

                # )

                extendeduser = Qviz_it_iitb()
                extendeduser.member1 = form.cleaned_data['member1']






                # extendeduser.user = user
                # extendeduser.save()

                subject = "Q-Viz-It 2022 | AZeotropy 2022 "
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

                html_message = render_to_string("qviz_it/mail_iitb.html",{'name':name1})
                message = strip_tags(html_message)

                email3 = EmailMultiAlternatives(subject,
                            message,
                            'azeo2022@gmail.com',
                            [to_email],
                            )
                email3.attach_alternative(html_message,'text/html')
                email3.send()
                extendeduser.save()

                return render(request, "qviz_it/confirmation.html",)




                # redirect to home page:
                #return redirect('registration_ca:index')

   # No post data availabe, let's just show the page.
    else:
        form = Qviz_it_iitb_Form()

    return render(request, template, {'form': form})


def user_register_non_iitb(request):
    # if this is a POST request we need to process the form data
    template = 'qviz_it/registration_non_iitb.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Qviz_it_non_iitb_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if not Azeo_id_user.objects.filter(azeo_id=form.cleaned_data['member1']).exists():

                return render(request, template, {
                        'form': form,
                        'error_message': 'AZeo-ID does not exist'
                    })

            if Qviz_it_noniitb.objects.filter(member1=form.cleaned_data['member1']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'You are already registered.'
                })





            else:
                # print('hellow world')
                # Create the user:

                # user = User.objects.create_user(
                #     # form.cleaned_data['username'],
                #     form.cleaned_data['email']

                # )

                extendeduser = Qviz_it_noniitb()
                extendeduser.member1 = form.cleaned_data['member1']






                # extendeduser.user = user
                # extendeduser.save()

                subject = "Successfully registered for Q-Viz-It Competition "
                # # message = f'congratulations {extendeduser.first_name}{extendeduser.last_name} have successfully registered on CA portal'
                azeo_id1 = str(extendeduser.member1)

                # # sql_query = 'SELECT id, email FROM registration_ca_Azeo_id_user WHERE azeo_id = {azeo_id}'

                # # to_email = Azeo_id_user.objects.raw(sql_query.format(azeo_id = azeo_id1))

                to_email = Azeo_id_user.objects.get(azeo_id = azeo_id1).email



                # # for person in to_email:

                # # tmp = to_email[0]
                # # my_email = to_email[0].email

                # # to_email = str(to_email).strip()

                name1 = Azeo_id_user.objects.get(azeo_id = azeo_id1).first_name

                html_message = render_to_string("qviz_it/mail_non_iitb.html",{'name':name1})
                message = strip_tags(html_message)

                email3 = EmailMultiAlternatives(subject,
                            message,
                            'azeo2022@gmail.com',
                            [to_email],
                            )
                email3.attach_alternative(html_message,'text/html')
                email3.send()
                extendeduser.save()

                return render(request, "qviz_it/confirmation.html",)




                # redirect to home page:
                #return redirect('registration_ca:index')

   # No post data availabe, let's just show the page.
    else:
        form = Qviz_it_non_iitb_Form()

    return render(request, template, {'form': form})

