#pull and run container for mongodb
docker run -d -p 27017:27017 --name mongodb mongo

#create network docker
docker network create elastic

#pull and run elastic
docker run --name es --net elastic -p 9200:9200 -it\
-e "discovery.type=single-node" -e\
"xpack.security.enabled=false"\
-e "ES_JAVA_OPTS=-Xms1g -Xmx1g"\
-e 'xpack.security.enrollment.enabled=true'\
-m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.15.0

#pull and run kibana
docker run --name kib --net elastic -p 5601:5601/
 -e "xpack.security.enabled=false"/
  -e ELASTICSEARCH_HOSTS="http://es:9200" kibana:8.15.0

#connect es to network
docker network connect elastic es

#connect kib to network
docker network connect elastic kib

#Retrieve the login token
docker exec -it es /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

#Login password recovery
docker exec -it es /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic

#create docker image
docker build -t consumer-image:latest .
docker build -t stt-image:latest .
docker build -t analysis-image:latest .

#run docker image
docker run -d --name consumer-container consumer-image:latest
docker run -d --name stt-container stt-image:latest
docker run -d --name analysis-container analysis-image:latest



