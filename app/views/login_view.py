import customtkinter as ctk
from tkinter import messagebox
from ..controllers.auth_controller import AuthController
from ..widgets.hover_button import HoverButton

class LoginView:
    def __init__(self):
        self.auth_controller = AuthController()
        self.root = ctk.CTk()
        self.root.title("Connexion")
        self.root.geometry("400x300")
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
        x = (screen_width - 400) // 2
        y = (screen_height - 300) // 2
        self.root.geometry(f"400x300+{x}+{y}")

    def _create_widgets(self):
        # Titre
        title_label = ctk.CTkLabel(self.root, text="Connexion", font=("Arial", 20))
        title_label.pack(pady=20)

        # Champ Domaine
        self.domain_entry = ctk.CTkEntry(self.root, placeholder_text="Domaine")
        self.domain_entry.pack(pady=5)

        # Champ Serveur
        self.server_entry = ctk.CTkEntry(self.root, placeholder_text="Serveur LDAP (ex : ldap://10.0.0.1)")
        self.server_entry.pack(pady=5)

        # Champ Utilisateur
        self.username_entry = ctk.CTkEntry(self.root, placeholder_text="Utilisateur")
        self.username_entry.pack(pady=5)

        # Champ Mot de passe
        self.password_entry = ctk.CTkEntry(self.root, placeholder_text="Mot de passe", show="*")
        self.password_entry.pack(pady=5)

        # Bouton Connexion
        self.login_button = HoverButton(self.root, text="Se connecter", command=self._on_login)
        self.login_button.pack(pady=20)

        # Lier la touche "Entrer" au bouton de connexion
        self.root.bind("<Return>", lambda event: self._on_login())

    def _on_login(self):
        # Récupérer les valeurs des champs
        domain = self.domain_entry.get()
        server = self.server_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Authentification
        if self.auth_controller.authenticate(domain, server, username, password):
            self.root.destroy()  # Fermer la fenêtre de login
            from .home_view import HomeView  # Importer ici pour éviter la circularité
            home_view = HomeView()  # Ouvrir la page d'accueil
            home_view.show()
        else:
            # Afficher un message d'erreur
            messagebox.showerror("Erreur", "Échec de la connexion. Vérifiez vos identifiants ou le serveur LDAP.")

    def show(self):
        self.root.mainloop()