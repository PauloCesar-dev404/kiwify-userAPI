from .authenticate import KiwifyAuth

AUTH = KiwifyAuth()
HEADERS_USER = AUTH._load_headers()


