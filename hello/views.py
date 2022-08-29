from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


class HelloRekruto(View):
    template_name = 'hello.html'

    def get(self, request):
        name = request.GET.get("name")
        message = request.GET.get("message")
        context = {
            'name': name,
            'message': message
        }
        # return HttpResponse(f"<p>Hello {name}! {message}!</p>")
        return render(request, template_name=self.template_name, context=context)