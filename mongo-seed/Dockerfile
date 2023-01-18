from mongo

COPY db_disney.json /db_disney.json

CMD mongoimport --host mongodb --db disney --collection Tripadvisor --type json --file /db_disney.json
