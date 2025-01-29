from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException

class AuthController:
    def authenticate(self, domain, server_address, username, password):
        """
        Authentifie l'utilisateur via LDAP.
        :param domain: Domaine LDAP (ex : "example.com").
        :param server_address: Adresse du serveur LDAP (ex : "ldap://mon.super.server.com").
        :param username: Nom d'utilisateur (ex : "user" ou "user@example.com").
        :param password: Mot de passe.
        :return: True si l'authentification réussit, False sinon.
        """
        try:
            # Configuration du serveur LDAP
            server = Server(server_address, get_info=ALL)
            
            # Connexion au serveur LDAP
            conn = Connection(server, user=f"{username}@{domain}", password=password)
            
            if not conn.bind():
                print("Échec de la connexion LDAP : identifiants incorrects ou serveur indisponible.")
                return False
            
            print("Connexion LDAP réussie !")
            return True
        
        except LDAPException as e:
            print(f"Erreur LDAP : {e}")
            return False