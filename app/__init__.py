from .views.login_view import LoginView

def create_app():
    # Initialisation de la vue de login
    login_view = LoginView()
    return login_view  # Retourner l'objet login_view