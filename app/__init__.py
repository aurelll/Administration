from .views.login_view import LoginView

def create_app():
    # Initialisation de la vue de login
    login_view = LoginView()
    login_view.show()