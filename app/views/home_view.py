import customtkinter as ctk
from ..widgets.sidebar import Sidebar

class HomeView:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Accueil")
        self.root.geometry("800x600")  # Taille ajustée pour la barre latérale
        self.root.configure(bg="#2E2E2E")

        # Centrer la fenêtre
        self._center_window()

        # Style
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Widgets
        self._create_sidebar()  # Créer la barre latérale
        self._create_main_content()  # Créer le contenu principal

    def _center_window(self):
        # Centrer la fenêtre sur l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 800) // 2
        y = (screen_height - 600) // 2
        self.root.geometry(f"800x600+{x}+{y}")

    def _create_sidebar(self):
        # Créer la barre latérale
        self.sidebar = Sidebar(
            self.root,
            logout_callback=self._on_logout,
            home_callback=self._show_home,
            gestion_callback=self._show_gestion
        )
        self.sidebar.pack(side="left", fill="y")

    def _create_main_content(self):
        # Cadre pour le contenu principal
        self.main_content = ctk.CTkFrame(self.root)
        self.main_content.pack(side="right", fill="both", expand=True)

        # Titre du contenu principal
        self.content_title = ctk.CTkLabel(self.main_content, text="Bienvenue", font=("Arial", 24))
        self.content_title.pack(pady=50)

        # Message de bienvenue
        self.content_message = ctk.CTkLabel(self.main_content, text="Vous êtes connecté avec succès !", font=("Arial", 16))
        self.content_message.pack(pady=20)

    def _show_home(self):
        """Afficher la page d'accueil."""
        self.content_title.configure(text="Bienvenue")
        self.content_message.configure(text="Vous êtes connecté avec succès !")

    def _show_gestion(self):
        """Afficher la page de gestion."""
        self.content_title.configure(text="Gestion")
        self.content_message.configure(text="Page de gestion des PC.")

    def _on_logout(self):
        """Déconnexion et retour à la page de login."""
        self.root.quit()  # Fermer proprement la fenêtre
        self.root.destroy()  # Détruire la fenêtre
        from .login_view import LoginView  # Importer ici pour éviter la circularité
        login_view = LoginView()  # Ouvrir la page de login
        login_view.show()

    def show(self):
        self.root.mainloop()