# seafile

## Restore

<p class="callout info">If you change location, don't forget to check 'pids\_dir' in conf/gunicorn.conf and other path-specific options in conf/  
Don't forget to remove /tmp/seahub\_cache</p>

## OAUTH

### Google

```python
# OAUTH
ENABLE_OAUTH = True
OAUTH_ENABLE_INSECURE_TRANSPORT = True

OAUTH_CREATE_UNKNOWN_USER = False
OAUTH_ACTIVATE_USER_AFTER_CREATION = True

OAUTH_CLIENT_ID = "..."
OAUTH_CLIENT_SECRET = "..."
OAUTH_REDIRECT_URL = 'https://domain.com/oauth/callback/'

# The following shoud NOT be changed if you are using Google as OAuth provider.
OAUTH_PROVIDER_DOMAIN = 'google.com'
OAUTH_AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/auth'
OAUTH_TOKEN_URL = 'https://oauth2.googleapis.com/token'
OAUTH_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v1/userinfo'
OAUTH_SCOPE = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]
OAUTH_ATTRIBUTE_MAP = {
    "email": (True, "email"),
    "name": (False, "name"),
}
```
