import customtkinter as ctk

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

    def show(self):
        self.root.mainloop()