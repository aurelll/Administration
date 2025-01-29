import customtkinter as ctk

class HoverButton(ctk.CTkButton):
    """
    Bouton personnalisé avec effet de survol.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_bg_color = self.cget("fg_color")
        self.hover_bg_color = self._apply_hover_effect(self.default_bg_color)

        # Lier les événements de survol
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def _apply_hover_effect(self, color):
        """
        Applique un effet de survol en modifiant la couleur.
        """
        return "#1E90FF"  # Exemple de couleur plus claire

    def _on_enter(self, event=None):  # Ajouter `event=None` pour gérer les appels sans argument
        """Effet au survol."""
        self.configure(fg_color=self.hover_bg_color)

    def _on_leave(self, event=None):  # Ajouter `event=None` pour gérer les appels sans argument
        """Effet à la sortie du survol."""
        self.configure(fg_color=self.default_bg_color)