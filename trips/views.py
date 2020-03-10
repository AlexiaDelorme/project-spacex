# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def faq_page(request):
    return render(request, "faq.html", {"page_title": "FAQs"})
