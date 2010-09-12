from django.http import HttpResponse


class NoCacheMiddleware(object):

    def process_response(self, request, response):

        response['Pragma'] = 'no-cache'
        response['Cache-Control'] = 'no-cache must-revalidate proxy-revalidate'

        return response