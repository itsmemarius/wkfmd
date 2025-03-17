# a_core/middleware.py
class UTMParameterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of UTM parameters to track
        utm_params = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']
        for param in utm_params:
            if param in request.GET:
                value = request.GET.get(param)
                request.session[param] = value
                # Log the utm_source in the terminal
                if param == 'utm_source':
                    print("UTM Source:", value)
        response = self.get_response(request)
        return response
