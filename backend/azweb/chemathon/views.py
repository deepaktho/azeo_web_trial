# Create your views here.
from django.shortcuts import render
from . import forms
from .forms import Chemathon_questions_Form
from .forms import QuestionForm
from .models import Chemathon_questions
from .models import Chemathon_questions_admin
import datetime
from .forms import Chemathon_Form
from .models import Chemathonuser
from registration_ca.models import Azeo_id_user
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags




# Create your views here.




def Chemathon_question(request):
    # if this is a POST request we need to process the form data
    template = 'chemathon/chemathon_question.html'

    if request.method == 'POST':

            timestamp = str(datetime.datetime.now())

            # create a form instance and populate it with data from the request:
            form = Chemathon_questions_Form(request.POST)
            # check whether it's valid:
            range_q1 = [3.9, 4]
            range_q2 = [0.2, 0.3]
            range_q3 = [1, 1]
            range_q4 = [930, 940]
            range_q5 = [40, 42]
            range_q6 = [0.82, 0.87]
            range_q7 = [92, 94]

            if form.is_valid():

                if not Chemathonuser.objects.filter(team_id=form.cleaned_data['team_id']).exists():

                    return render(request, template, {
                            'form': form,
                            'error_message': 'Team-ID does not exist'
                        })

                elif form.cleaned_data['question1'] and (range_q1[0]>form.cleaned_data['question1'] or range_q1[1]<form.cleaned_data['question1'] ):
                    return render(request, template, {
                            'form': form,
                            'error_message': 'Answer for question1 part (i) is out of range!'
                        })
                elif form.cleaned_data['question2'] and (range_q2[0]>form.cleaned_data['question2'] or range_q2[1]<form.cleaned_data['question2'] ):
                    return render(request, template, {
                            'form': form,
                            'error_message': 'Answer for question1 part (ii) is out of range!'
                        })
                elif form.cleaned_data['question3'] and (range_q3[0]>form.cleaned_data['question3'] or range_q3[1]<form.cleaned_data['question3'] ):
                    return render(request, template, {
                            'form': form,
                            'error_message': 'Answer for question2 part (i) is out of range!'
                        })
                elif form.cleaned_data['question4'] and (range_q4[0]>form.cleaned_data['question4'] or range_q4[1]<=form.cleaned_data['question4'] ):
                    return render(request, template, {
                            'form': form,
                            'error_message': 'Answer for question2 part (ii) is out of range!'
                        })
                elif form.cleaned_data['question5'] and (range_q5[0]>form.cleaned_data['question5'] or range_q5[1]<form.cleaned_data['question5'] ):
                    return render(request, template, {
                            'form': form,
                            'error_message': 'Answer for question3 part (i) is out of range!'
                        })
                elif form.cleaned_data['question6'] and (range_q6[0]>form.cleaned_data['question6'] or range_q6[1]<form.cleaned_data['question6'] ):
                    return render(request, template, {
                            'form': form,
                            'error_message': 'Answer for question3 part (ii) is out of range!'
                        })
                elif form.cleaned_data['question7'] and (range_q7[0]>form.cleaned_data['question7'] or range_q7[1]<form.cleaned_data['question7'] ):
                    return render(request, template, {
                            'form': form,
                            'error_message': 'Answer for question4  is out of range!'
                        })





                else:
                    # print('hellow world')
                    # Create the user:

                    # user = User.objects.create_user(
                    #     # form.cleaned_data['username'],
                    #     form.cleaned_data['email']

                    # )

                    chemathon_answers = Chemathon_questions()
                    chemathon_answers.team_id = form.cleaned_data['team_id']
                    chemathon_answers.question1 = form.cleaned_data['question1']
                    chemathon_answers.question2 = form.cleaned_data['question2']
                    chemathon_answers.question3 = form.cleaned_data['question3']
                    chemathon_answers.question4 = form.cleaned_data['question4']
                    chemathon_answers.question5 = form.cleaned_data['question5']
                    chemathon_answers.question6 = form.cleaned_data['question6']
                    chemathon_answers.question7 = form.cleaned_data['question7']
                    chemathon_answers.submitted_at = timestamp
                    chemathon_answers.save()

                    return render(request, "chemathon/confirmation.html",)




                    # redirect to home page:
                    #return redirect('registration_ca:index')
            else:

                    return render(request, template, {
                            'form': form,
                            'error_message': 'Answer for question6 is out of range!'
                        })

   # No post data availabe, let's just show the page.
    else:
        form = Chemathon_questions_Form()
        return render(request, template, {'form': form})




def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'chemathon/registration.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Chemathon_Form(request.POST)
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


            elif Chemathonuser.objects.filter(member1=form.cleaned_data['member1']).exists() or Chemathonuser.objects.filter(member2=form.cleaned_data['member1']).exists()  :
                return render(request, template, {
                    'form': form,
                    'error_message': 'Member 1 already registered.'
                })
            elif  form.cleaned_data.get('member2') and (Chemathonuser.objects.filter(member2=form.cleaned_data['member2']).exists() or Chemathonuser.objects.filter(member1=form.cleaned_data['member2']).exists() ):

                    return render(request, template, {
                        'form': form,
                        'error_message': 'Member 2 already registered.'
                    })
            else:
                # print('hellow world')
                # Create the user:

                # user = User.objects.create_user(
                #     # form.cleaned_data['username'],
                #     form.cleaned_data['email']

                # )
                if Chemathonuser.objects.only('id').last().id+1 < 10:
                    team_id=f"CHE-0{Chemathonuser.objects.only('id').last().id+1}"
                else:
                    team_id=f"CHE-{Chemathonuser.objects.only('id').last().id+1}"


                extendeduser = Chemathonuser()
                extendeduser.member1 = form.cleaned_data['member1']
                extendeduser.member2 = form.cleaned_data['member2']

                extendeduser.team_id = team_id





                # extendeduser.user = user
                # extendeduser.save()

                subject = "Successfully registered for Chemathon Competition "
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

                html_message = render_to_string("chemathon/mail.html",{'name':name1,'team_id':team_id,})
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

                    html_message = render_to_string("chemathon/mail.html",{'name':name2,'team_id':team_id,})
                    message = strip_tags(html_message)

                    email4 = EmailMultiAlternatives(subject,
                                message,
                                'azeo2022@gmail.com',
                                [to_email2],
                                )
                    email4.attach_alternative(html_message,'text/html')
                    email4.send()
                # send_mail(
                #             subject,
                #             message,
                #             from_email,
                #             [to_email],
                #             fail_silently=False,
                #         )
                extendeduser.save()

                return render(request, "chemathon/confirmation_registration.html", {"Team_ID":team_id})




                # redirect to home page:
                #return redirect('registration_ca:index')

   # No post data availabe, let's just show the page.
    else:
        form = Chemathon_Form()

    return render(request, template, {'form': form})

