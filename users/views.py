# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data.get('username')
			messages.success(request, "Account created for, %s" %username)
			return redirect('login')
			
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html', {"form": form})


@login_required
def profile(request):

	if request.method == 'POST':
		userupdate_form = UserUpdateForm(request.POST, instance=request.user)
		profileupdate_form = ProfileUpdateForm(request.POST, 
											request.FILES, 
											instance=request.user.profile)
	

		if userupdate_form.is_valid() and profileupdate_form.is_valid():

			userupdate_form.save()
			profileupdate_form.save()

			messages.success(request, f"Your account has been update!")
			return redirect('profile')
			




	else: 
		userupdate_form = UserUpdateForm(request.POST, instance=request.user)
		profileupdate_form = ProfileUpdateForm(request.POST,
											instance=request.user.profile)
	
	
	context = {
			"userupdate_form": userupdate_form,
			"ProfileUpdateForm": ProfileUpdateForm 


			}
	return render (request, 'users/profile.html', context)


