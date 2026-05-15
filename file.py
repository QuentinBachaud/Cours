def write_text(filename, content):
    """
    Écrit du contenu dans un fichier texte.
    
    Args:
        filename (str): Le nom du fichier à créer ou modifier
        content (str): Le contenu à écrire dans le fichier
    
    Returns:
        bool: True si l'opération a réussi, False sinon
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Contenu écrit avec succès dans '{filename}'")
        return True
    except Exception as e:
        print(f"Erreur lors de l'écriture dans '{filename}': {e}")
        return False


if __name__ == "__main__":
    # Exemple d'utilisation
    write_text("exemple.txt", "Bonjour, ceci est un fichier texte!")
