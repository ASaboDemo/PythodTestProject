def site_defaults(request):
    return {
        'site_name': 'DaCMS',
        'current_language': getattr(request, 'LANGUAGE_CODE', 'en'),
    }
