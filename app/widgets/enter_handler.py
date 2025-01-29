def bind_enter_to_button(root, button):
    """
    Lie la touche "Entrer" à un bouton.
    :param root: La fenêtre principale.
    :param button: Le bouton à déclencher.
    """
    root.bind("<Return>", lambda event: button.invoke())