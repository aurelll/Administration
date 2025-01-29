import customtkinter as ctk
from ..widgets.hover_button import HoverButton

class Sidebar(ctk.CTkFrame):
    """
    Widget pour une barre latérale avec un menu.
    """
    def __init__(self, parent, logout_callback, home_callback, gestion_callback, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(width=200, corner_radius=0)

        # Titre de la barre latérale
        sidebar_title = ctk.CTkLabel(self, text="Menu", font=("Arial", 18))
        sidebar_title.pack(pady=20)

        # Bouton Accueil
        home_button = HoverButton(self, text="Accueil", command=home_callback)
        home_button.pack(pady=10)

        # Bouton Gestion
        gestion_button = HoverButton(self, text="Gestion", command=gestion_callback)
        gestion_button.pack(pady=10)

        # Bouton Déconnexion
        logout_button = HoverButton(self, text="Déconnexion", command=logout_callback)
        logout_button.pack(pady=10)