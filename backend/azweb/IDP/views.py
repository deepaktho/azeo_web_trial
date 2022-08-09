from django.shortcuts import render
from .forms import IDPForm
from .models import IDPuser
from registration_ca.models import Azeo_id_user
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random



# Create your views here.



def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'IDP/registration.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IDPForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if  not (Azeo_id_user.objects.filter(azeo_id=form.cleaned_data['member1']).exists()) :

                return render(request, template, {
                        'form': form,
                        'error_message': 'AZeo-ID does not exist for member 1'
                    })
            elif form.cleaned_data.get('member2') and not (Azeo_id_user.objects.filter(azeo_id=form.cleaned_data['member2']).exists()):
                return render(request, template, {
                        'form': form,
                        'error_message': 'AZeo-ID does not exist for member 2'
                    })

            elif form.cleaned_data.get('member3') and not (Azeo_id_user.objects.filter(azeo_id=form.cleaned_data['member3']).exists()):
                return render(request, template, {
                        'form': form,
                        'error_message': 'AZeo-ID does not exist for member 3'
                    })

            elif IDPuser.objects.filter(member1=form.cleaned_data['member1']).exists() or IDPuser.objects.filter(member2=form.cleaned_data['member1']).exists() or IDPuser.objects.filter(member3=form.cleaned_data['member1']).exists() :
                return render(request, template, {
                    'form': form,
                    'error_message': 'Member 1 already registered.'
                })
            elif  form.cleaned_data.get('member2') and (IDPuser.objects.filter(member2=form.cleaned_data['member2']).exists() or IDPuser.objects.filter(member1=form.cleaned_data['member2']).exists() or IDPuser.objects.filter(member3=form.cleaned_data['member2']).exists()):

                    return render(request, template, {
                        'form': form,
                        'error_message': 'Member 2 already registered.'
                    })

            elif  form.cleaned_data.get('member3') and (IDPuser.objects.filter(member3=form.cleaned_data['member3']).exists() or IDPuser.objects.filter(member2=form.cleaned_data['member3']).exists() or IDPuser.objects.filter(member1=form.cleaned_data['member3']).exists()):

                    return render(request, template, {
                        'form': form,
                        'error_message': 'Member 3 already registered.'
                    })






            else:
                # print('hellow world')
                # Create the user:

                # user = User.objects.create_user(
                #     # form.cleaned_data['username'],
                #     form.cleaned_data['email']

                # )

                extendeduser = IDPuser()
                extendeduser.member1 = form.cleaned_data['member1']
                extendeduser.member2 = form.cleaned_data['member2']
                extendeduser.member3 = form.cleaned_data['member3']
                team_id=f"IDP-{IDPuser.objects.only('id').last().id+1}"
                extendeduser.team_id = team_id





                # extendeduser.user = user
                # extendeduser.save()

                subject = "Successfully registered for IDP Competition "
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

                html_message = render_to_string("IDP/mail.html",{'name':name1,'team_id':team_id,})
                message = strip_tags(html_message)

                email3 = EmailMultiAlternatives(subject,
                            message,
                            'azeo2022@gmail.com',
                            [to_email],
                            )
                email3.attach_alternative(html_message,'text/html')
                email3.send()

                if  form.cleaned_data.get('member2'):
                    azeo_id2 = str(extendeduser.member2)
                    to_email2 = Azeo_id_user.objects.get(azeo_id = azeo_id2).email
                    name2 = Azeo_id_user.objects.get(azeo_id = azeo_id2).first_name

                    html_message = render_to_string("IDP/mail.html",{'name':name2,'team_id':team_id,})
                    message = strip_tags(html_message)

                    email4 = EmailMultiAlternatives(subject,
                                message,
                                'azeo2022@gmail.com',
                                [to_email2],
                                )
                    email4.attach_alternative(html_message,'text/html')
                    email4.send()

                if  form.cleaned_data.get('member3'):
                    azeo_id3 = str(extendeduser.member3)
                    to_email3 = Azeo_id_user.objects.get(azeo_id = azeo_id3).email
                    name3 = Azeo_id_user.objects.get(azeo_id = azeo_id3).first_name

                    html_message = render_to_string("IDP/mail.html",{'name':name3,'team_id':team_id,})
                    message = strip_tags(html_message)

                    email5 = EmailMultiAlternatives(subject,
                                message,
                                'azeo2022@gmail.com',
                                [to_email3],
                                )
                    email5.attach_alternative(html_message,'text/html')
                    email5.send()




                # send_mail(
                #             subject,
                #             message,
                #             from_email,
                #             [to_email],
                #             fail_silently=False,
                #         )
                extendeduser.save()

                return render(request, "IDP/confirmation.html", {"Team_ID":team_id})




                # redirect to home page:
                #return redirect('registration_ca:index')

   # No post data availabe, let's just show the page.
    else:
        form = IDPForm()

    return render(request, template, {'form': form})


