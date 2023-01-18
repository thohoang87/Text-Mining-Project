### Dans un terminal de commande

## Vérifier que docker compose est installé

<pre><code>docker-compose -v<\pre><\code>

## Cloner le repo et créer les containers

<pre><code> git clone https://github.com/PierreDubrulle/scrap.git\
cd scrap\
docker compose up -d<\pre><\code>

## Services
<p>Pour chaque service recopier le lien correspondant dans un navigateur<\p>
<p>mongo-express => locahost:6082
   streamlit => localhost:8501<\p>
   
   
### PS : Vérifier que docker-desktop est lancé. Si ce n'est pas le cas, ouvir l'application
