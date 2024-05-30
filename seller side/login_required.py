from functools import wraps
from flask import redirect, url_for, session, flash

class login_required:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        if 'user' not in session:
            flash("You need to be signed in to view this page.")
            return redirect(url_for('signin'))
        return self.func(*args, **kwargs)
