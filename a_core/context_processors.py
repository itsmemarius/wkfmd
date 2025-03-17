def user_context(request):
    return {
        "user_id": request.user.id if request.user.is_authenticated else None,
        "utm_source": request.session.get("utm_source", ""),
        "utm_medium": request.session.get("utm_medium", ""),
        "utm_campaign": request.session.get("utm_campaign", ""),
        "utm_term": request.session.get("utm_term", ""),
        "utm_content": request.session.get("utm_content", ""),
    }
