import datetime # necesary for JWT

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # IsAuthenticated

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # Django-filter Dependecies
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

# dependencies for JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(hours=1),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id'
}

# Configure Cors | use Origins_All or Allow_Credentials but not all
#CORS_ORIGIN_WHITELIST = os.environ.get("DJANGO_ALLOWED_ORIGINS").split(' ')
CORS_ALLOW_ORIGINS_ALL = True
#CORS_ALLOW_CREDENTIALS = True
