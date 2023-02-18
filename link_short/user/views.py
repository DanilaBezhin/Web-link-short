from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'user/register.html',
        {'form': form}
    )



@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    date = {
        'updateUserForm': updateUserForm,
    }

    return render(request, 'user/profile.html', date)
