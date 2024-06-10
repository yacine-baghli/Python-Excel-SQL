import pandas as pd

# Liste des noms de fichiers
noms_fichiers = [
    "course24_05_2022-17h34m18s",
    "course24_05_2022-17h37m50s",
    "course07_06_2022-15h30m42s",
    "course14_06_2022-16h15m45s",
    "course24_06_2022-17h26m41s",
    "course24_06_2022-17h33m57s",
    "course24_06_2022-18h48m17s",
    "course28_06_2022-15h44m07s",
    "course28_06_2022-17h31m59s"
]

# Dictionnaire pour stocker le REF_RELEVE associé à chaque fichier
ref_releve_dict = {}

# Valeur initiale du REF_RELEVE
ref_releve = 22001

# Associer un REF_RELEVE à chaque fichier
for nom_fichier in noms_fichiers:
    ref_releve_dict[nom_fichier] = ref_releve
    ref_releve += 1

# Ouvrir le fichier texte en mode écriture
with open("requetes_sql.txt", "w") as fichier:
    # Initialiser l'ID
    id_value = 1

    # Parcourir les fichiers et générer les requêtes SQL
    for nom_fichier in noms_fichiers:
        # Lecture du fichier Excel
        df = pd.read_excel(nom_fichier + ".xlsx")  # Ajoutez l'extension de fichier correcte si nécessaire

        # Parcourir les lignes du dataframe
        for index, row in df.iterrows():
            # Convertir les valeurs nulles en "NULL" pour la requête SQL
            row = row.fillna("NULL")

            # Convertir le format de temps en string
            temps = str(row.iloc[0])  # Convertir en chaîne de caractères
            if pd.isnull(temps) or temps.lower() == "null":
                temps = "NULL"
            else:
                temps = temps.replace(" ", "")  # Supprimer les espaces
                temps = temps.replace("min", "m")  # Standardiser le format
                temps = temps.replace("s", "")  # Supprimer les "s"
                temps = f"'{temps}'"

            # Convertir la dernière case en entier
            row.iloc[-1] = int(row.iloc[-1])

            # Récupérer le REF_RELEVE associé à ce fichier
            ref_releve = ref_releve_dict[nom_fichier]

            # Créer la requête SQL avec l'ID et les variables entières à zéro
            sql = f"INSERT INTO `points` VALUES ({id_value}, {ref_releve}, {temps}, {', '.join(map(str, row.values[1:]))}, 0.0, 0, '0000-00-00 00:00:00');\n"

            # Écrire la requête SQL dans le fichier texte
            fichier.write(sql)

            # Incrémenter l'ID
            id_value += 1
