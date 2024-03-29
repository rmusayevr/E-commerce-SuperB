from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
from django.http import HttpResponseForbidden
from Core.models import BlockedIP

class BlockIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        blocked_IPs = BlockedIP.objects.all()
        blocked_IP_QS = [ip.ip_addr for ip in blocked_IPs]
        if request.META['REMOTE_ADDR'] in blocked_IP_QS:
            return HttpResponseForbidden('<h1>Access Denied</h1>')
    
    def process_exception(self, request, exception):
        print(exception)
        return render(request, "404error.html", {})
