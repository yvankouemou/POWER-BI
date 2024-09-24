import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Charger le jeu de données
dataset = pd.read_excel('publications_scientifiques_par_pays.xlsx')

# Calculer les valeurs moyennes pour chaque pays
country_means = dataset.groupby('Country').agg({
    'Documents': 'mean',
    'Citations': 'mean',
    'H.index': 'mean',
    'Rank': 'median'
}).reset_index()

# Normaliser l'indice H pour la taille dans le graphique
h_index_normalized = (country_means['H.index'] - country_means['H.index'].min()) / (country_means['H.index'].max() - country_means['H.index'].min())

# Préparer le graphique de dispersion avec Plotly Express
fig = px.scatter(country_means,
                 x='Documents',
                 y='Citations',
                 size=h_index_normalized * 100 + 10,  # Ajuster le facteur d'échelle pour la visibilité
                 color='Rank',
                 hover_name='Country',
                 color_continuous_scale='Viridis',  # Utiliser l'échelle de couleur Viridis
                 title='Relation entre les documents produits et les citations par pays')

# Calculer les valeurs moyennes pour les documents et les citations
mean_documents = country_means['Documents'].mean()
mean_citations = country_means['Citations'].mean()

# Ajouter une ligne horizontale pour les citations moyennes
fig.add_trace(go.Scatter(x=[0, country_means['Documents'].max()],
                         y=[mean_citations, mean_citations],
                         mode="lines",
                         line=dict(dash='dash', color='blue'),
                         name='Citations moyennes'))

# Ajouter une ligne verticale pour les documents moyens
fig.add_trace(go.Scatter(x=[mean_documents, mean_documents],
                         y=[0, country_means['Citations'].max()],
                         mode="lines",
                         line=dict(dash='dash', color='red'),
                         name='Documents moyens'))

# Mettre à jour la mise en page pour une meilleure apparence
fig.update_layout(
    xaxis_title="Nombre moyen de documents produits par an",
    yaxis_title="Nombre moyen de citations par an",
    legend_title="Rang médian"
)

fig.show()
