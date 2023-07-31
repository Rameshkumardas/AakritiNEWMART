from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def superadmin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_verified and u.is_superadmin,
        login_url="/",
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
        Decorator for views that checks that the logged in user is a teacher,
        redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_verified and u.is_admin,
        login_url="/",
        redirect_field_name=""
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

# is_accountant
def manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a teacher,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_verified and u.is_manager,
        login_url="/",
        redirect_field_name=""
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def accountant_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a teacher,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_verified and u.is_accountant,
        login_url="/",
        redirect_field_name=""
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def user_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a teacher,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_verified and u.is_user,
        login_url="/",
        redirect_field_name=""
    )
    if function:
        return actual_decorator(function)
    return actual_decorator