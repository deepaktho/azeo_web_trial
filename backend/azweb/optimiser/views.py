from django.shortcuts import render
from .forms import OptimiserForm
from .models import Optimiseruser
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
    template = 'optimiser/registration.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OptimiserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if not Azeo_id_user.objects.filter(azeo_id=form.cleaned_data['member1']).exists():

                return render(request, template, {
                        'form': form,
                        'error_message': 'AZeo-ID does not exist'
                    })

            if Optimiseruser.objects.filter(member1=form.cleaned_data['member1']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Member 1 already registered.'
                })
            elif  form.cleaned_data.get('member2') and Optimiseruser.objects.filter(member2=form.cleaned_data['member2']).exists():

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

                extendeduser = Optimiseruser()
                extendeduser.member1 = form.cleaned_data['member1']
                extendeduser.member2 = form.cleaned_data['member2']
                team_id=f"OP-{Optimiseruser.objects.only('id').last().id+1}"
                extendeduser.team_id = team_id


                lst= [480900, 861718, 191272, 820673, 811406, 471259, 613688, 120682, 222548, 188856, 646239, 556454, 518151, 258621, 434139, 387304, 824825, 406525, 674734, 556139, 935531, 687526, 205057, 356924, 292781, 821187, 891520, 125308, 410961, 592862, 692244, 244766, 867285, 269484, 468133, 754747, 647849, 985614, 428016, 250067, 212512, 783204, 738020, 847296, 572397, 440504, 612722, 827656, 345954, 330980]
                user_id = random.choice(lst)
                lst.remove(user_id)

                extendeduser.user_id = user_id


                # extendeduser.user = user
                # extendeduser.save()

                subject = "Successfully registered for Optimiser Competition "
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

                html_message = render_to_string("optimiser/mail.html",{'name':name1,'team_id':team_id,'user_id':user_id,})
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

                    html_message = render_to_string("optimiser/mail.html",{'name':name2,'team_id':team_id,'user_id':user_id,})
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

                return render(request, "optimiser/confirmation.html", {"Team_ID":team_id})




                # redirect to home page:
                #return redirect('registration_ca:index')

   # No post data availabe, let's just show the page.
    else:
        form = OptimiserForm()

    return render(request, template, {'form': form})


