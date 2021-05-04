from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View, FormView
from visit.models import User
from visit.forms import UserForm


def get_user_by_id(request, user_id):

    user = User.objects.get(id=user_id)

    contact = {
        'username': user.username,
        'email': user.email,
        'text': f'Info about user # {user_id}'
    }

    return contact



class GetInfoView(View):

    def get(self, request, user_id):
        contact = get_user_by_id(request, user_id)

        return render(
            template_name='user_view.html',
            request=request,
            context=contact,
        )


class User_list(ListView):
    model = User
    template_name = 'index.html'



class Add_user(FormView):
    form_class = UserForm
    template_name = 'add_user_f.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        responce = super().form_valid(form)



        return responce


class Edit_user(View):



    def get(self,request, user_id):

        return render(
            template_name='add_user.html',
            request=request,
            context={},
        )


    def post(self, request, user_id):


        username = request.POST['username']
        email=request.POST['email']

        if username:
            User.objects.filter(pk=user_id).update(username=username)
        if email:
            User.objects.filter(pk=user_id).update(email=email)
        contact = get_user_by_id(request, user_id)
        contact['text'] = 'Contact edited'

        return render(
            template_name='user_view.html',
            request=request,
            context=contact,
        )


class Dell_user(View):

    def get(self,request, user_id):

        cont = {
            'user_id': user_id
        }
        return render(
            template_name='dell_user.html',
            request=request,
            context=cont,
            )


    def post(self, request, user_id):


        if 'Yes' in request.POST:

            try:
                user = get_object_or_404(User, id=user_id)


                user.delete()
                cont = {'text':(f'User # {user_id} delleted')}
            except:
                cont = {'text':(f'User # {user_id} not found')}

        elif 'Cancel' in request.POST :
            cont = {'text':(f'User # {user_id} was not delleted')}


        return render(
            template_name='text.html',
            request=request,
            context=cont,
        )