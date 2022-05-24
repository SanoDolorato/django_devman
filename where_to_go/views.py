from django.http import HttpResponse
from django.template import loader

def show_start(request):
    template = loader.get_template('show_start.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)