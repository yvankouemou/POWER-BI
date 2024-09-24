# Importer la bibliothèque pandas
import pandas as pd
 
# Charger le jeu de données pour examiner sa structure et son contenu
df = pd.read_excel('publications_scientifiques_par_pays.xlsx')
 
# Afficher les premières lignes du dataframe pour comprendre sa structure
df.head(), df.describe(), df.info()



import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
 
# Calculer les valeurs moyennes pour chaque pays
country_means = df.groupby('Country').agg({
    'Documents': 'mean',
    'Citations': 'mean',
    'H.index': 'mean',
    'Rank': 'median'
}).reset_index()
 
# Normaliser l'indice H pour la taille dans le graphique
h_index_normalized = (country_means['H.index'] - country_means['H.index'].min()) / (country_means['H.index'].max() - country_means['H.index'].min())
 
# Préparer le graphique de dispersion
plt.figure(figsize=(14, 10))
scatter = plt.scatter(
    x=country_means['Documents'],
    y=country_means['Citations'],
    s=h_index_normalized * 1000 + 10,  # Échelle des tailles pour une meilleure visibilité
    c=country_means['Rank'],
    cmap='viridis',
    alpha=0.6,
    edgecolors='w',
    linewidths=0.5
)
 
# Ajouter des annotations pour les pays
for i, txt in enumerate(country_means['Country']):
    plt.annotate(txt, (country_means['Documents'][i], country_means['Citations'][i]), fontsize=8, alpha=0.7)
 
# Ajouter une barre de couleur
plt.colorbar(scatter, label='Rang médian')
 
# Ajouter des lignes moyennes
plt.axvline(country_means['Documents'].mean(), color='r', linestyle='--', label='Documents moyens')
plt.axhline(country_means['Citations'].mean(), color='b', linestyle='--', label='Citations moyennes')
 
plt.xlabel('Nombre moyen de documents produits par an')
plt.ylabel('Nombre moyen de citations par an')
plt.title('Relation entre les documents produits et les citations par pays')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
 
plt.show()

