# -*- coding: utf-8 -*-

from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import Http404
from django.core.urlresolvers import reverse
from django import forms
from django.core.mail import send_mail


def index(request):
    return render(request, "index.html")

def my_courses_view(request):
    return render(request, "my_courses.html")

def course_item_view(request):
    return render(request, "course_item.html")


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

from django.template import RequestContext

def cources(request):
    course = Cource.objects.all()
    return {'cource': course}


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['date'] = datetime.now()
            message = render_to_string("contact_mail.txt",
                     RequestContext(request, data, [cources, ]))

            send_mail("Contact Form From M-Up", message, data['email'],
                ["dixon.che@gmail.com"])

            messages.success(request, u'Сообщение было удачно отправлено')
            return redirect(reverse('contact_page'))
    else:
        form = ContactForm()

    return render(request, "contact.html", {'form': form})
