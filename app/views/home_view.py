import customtkinter as ctk
from ..widgets.hover_button import HoverButton

class HomeView:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Accueil")
        self.root.geometry("600x400")
        self.root.configure(bg="#2E2E2E")

        # Centrer la fenêtre
        self._center_window()

        # Style
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Widgets
        self._create_widgets()

    def _center_window(self):
        # Centrer la fenêtre sur l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 400) // 2
        self.root.geometry(f"600x400+{x}+{y}")

    def _create_widgets(self):
        # Titre
        title_label = ctk.CTkLabel(self.root, text="Bienvenue", font=("Arial", 24))
        title_label.pack(pady=50)

        # Message
        message_label = ctk.CTkLabel(self.root, text="Vous êtes connecté avec succès !", font=("Arial", 16))
        message_label.pack(pady=20)

        # Bouton Déconnexion
        logout_button = HoverButton(self.root, text="Se déconnecter", command=self._on_logout)
        logout_button.pack(pady=20)

    def _on_logout(self):
        """Déconnexion et retour à la page de login."""
        self.root.destroy()  # Fermer la fenêtre d'accueil
        from .login_view import LoginView  # Importer ici pour éviter la circularité
        login_view = LoginView()  # Ouvrir la page de login
        login_view.show()

    def show(self):
        self.root.mainloop()