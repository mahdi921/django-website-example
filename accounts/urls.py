from django.urls import path
from accounts.views import login_view #, logout_view, register_view, profile_view, profile_edit_view, password_change_view

app_name = 'accounts'

url_patterns = [
    path('login', login_view, name='login'),
    # path('logout', logout_view, name='logout'),
    # path('register', register_view, name='register'),
    # path('profile', profile_view, name='profile'),
    # path('profile/edit', profile_edit_view, name='profile-edit'),
    # path('profile/password', password_change_view, name='password-change'),
]