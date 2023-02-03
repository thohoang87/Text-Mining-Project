### Projet Text Mining en partenariat avec DisneyLand Paris

L’objectif de ce projet et de fournir une solution pour analyser les commentaires des différents sites de Disney sur la plateforme TripAdvisor. Cet outil a pour objectif de fournir un aide à la décision et permettre aux utilisateurs de réaliser une veille constante sur les commentaires de leurs différents sites. L’application présentera différents résultats plus ou moins adaptable selon les besoin des utilisateurs.

Cette solution sera capable de récupérer elle même les commentaires de TripAdvisor pour les stocker et les analyser. Elle présentera les analyses dans une application web qui sera utilisable et compréhensible par le plus grand nombre. Enfin, il faudra également prendre en compte que cette solution sera hébergée par Disney et son système d’information, donc il faudra prendre en compte les problématiques classiques de déploiement et de performance de notre solution.

# 1. web scrapping
Dans un premier temps, nous avons scrappé tous les commentaires et les autres informations nécessaires pour l'analyse en utilisant les 2 packages BeautifulSoup et Selenium.

# 2. Datawarehouse
Après web scrapping, nous avons stoké tous les éléments dans Mongodb et on a également mis en place la mise à jour pour cette dw au cours du temps.

# 3. Analyse et Streamlit
Nous avons réalisé les analyses et construit une application Streamlit pour déployer ces analyses.

# 4. Docker
En fin, nous avons déployé le tout sur Docker.

Pour pouvoir accéder à ces différentes ressources, il faut installer Docker et suivre bien les étapes suivantes:

## Dans un terminal de commande

# Vérifier que docker compose est installé

<pre><code>docker-compose -v</code></pre>

# Cloner le repo et créer les containers

<pre><code> git clone https://github.com/PierreDubrulle/scrap.git && cd scrap && docker compose up -d</code></pre>

# Services
<p>Pour chaque service recopier le lien correspondant dans un navigateur</p>
<p>mongo-express => locahost:6082
   streamlit => localhost:8501</p>
   
   
# PS : Vérifier que docker-desktop est lancé. Si ce n'est pas le cas, ouvir l'application
