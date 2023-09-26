To execute pipeline with different replication factors: 
    delete container volumes and container itself for each validation scenario to run without any issues.

### To remove containers
docker rm broker bookie bookie2 bookie3 zookeeper pulsar-init

--------------------------------------------------------------------------------------

# Replication factor 1 with 0 topic partitions for each relevant topic.

# Set the following replication values in broker container.
      - managedLedgerDefaultEnsembleSize=1
      - managedLedgerDefaultWriteQuorum=1
      - managedLedgerDefaultAckQuorum=1

# Since default partitions are zero, so no need to create explicitly create topics.

# Register source, transformer function, and sink.
bin/pulsar-admin source create --source-config-file connectors/debezium-postgres-source-config.yaml
bin/pulsar-admin sinks create --sink-config-file connectors/elasticsearch-sink.yml
bin/pulsar-admin functions create   --py functions/transformers.py   --classname transformers.PgEsTransformer   
\--inputs persistent://public/default/dbserver1.public.inventory_products   
\--output persistent://public/default/elasticsearch-sink


# Collect first and last documents.
curl -X GET "localhost:9200/products/_search?pretty&search_type=dfs_query_then_fetch&size=1&from=0" -H 'Content-Type: application/json' -d'
{
  "sort" : [
    { "_indexed_at" : {"order" : "asc", "format": "strict_date_optional_time_nanos"}},
    "_score"
  ],
  "track_total_hits": true
}
' > first-indexed-entry-replication-1-partition-0.txt

curl -X GET "localhost:9200/products/_search?pretty&search_type=dfs_query_then_fetch&size=1&from=0" -H 'Content-Type: application/json' -d'
{
  "sort" : [
    { "_indexed_at" : {"order" : "desc", "format": "strict_date_optional_time_nanos"}},
    "_score"
  ],
  "track_total_hits": true
}
' > last-indexed-entry-replication-1-partition-0.txt


--------------------------------------------------------------------------------------

# Replication factor 2 with 3 topic partitions for each relevant topic.

# Set the following replication values in broker container.
      - managedLedgerDefaultEnsembleSize=2
      - managedLedgerDefaultWriteQuorum=2
      - managedLedgerDefaultAckQuorum=2

# Create topics with 3 partitions
bin/pulsar-admin topics create-partitioned-topic \
    persistent://public/default/dbserver1.public.inventory_products \
    --partitions 3

bin/pulsar-admin topics create-partitioned-topic \
    persistent://public/default/debezium-postgres-topic \
    --partitions 3

bin/pulsar-admin topics create-partitioned-topic \
    persistent://public/default/debezium-postgres-source-debezium-offset-topic \
    --partitions 3

bin/pulsar-admin topics create-partitioned-topic \
    persistent://public/default/elasticsearch-sink \
    --partitions 3

bin/pulsar-admin topics list public/default
# Register source, transformer function, and sink.
bin/pulsar-admin source create --source-config-file connectors/debezium-postgres-source-config.yaml
bin/pulsar-admin sinks create --sink-config-file connectors/elasticsearch-sink.yml
bin/pulsar-admin functions create   --py functions/transformers.py   --classname transformers.PgEsTransformer   --inputs persistent://public/default/dbserver1.public.inventory_products   --output persistent://public/default/elasticsearch-sink

# Collect first and last documents.
curl -X GET "localhost:9200/products/_search?pretty&search_type=dfs_query_then_fetch&size=1&from=0" -H 'Content-Type: application/json' -d'
{
  "sort" : [
    { "_indexed_at" : {"order" : "asc", "format": "strict_date_optional_time_nanos"}},
    "_score"
  ],
  "track_total_hits": true
}
' > first-indexed-entry-replication-2-partition-3.txt

curl -X GET "localhost:9200/products/_search?pretty&search_type=dfs_query_then_fetch&size=1&from=0" -H 'Content-Type: application/json' -d'
{
  "sort" : [
    { "_indexed_at" : {"order" : "desc", "format": "strict_date_optional_time_nanos"}},
    "_score"
  ],
  "track_total_hits": true
}
' > last-indexed-entry-replication-2-partition-3.txt


------------------------------------------------------------------------------------------------------------------------

# Replication factor 3 with 10 topic partitions for each relevant topic.

# Set the following replication values in broker container.
      - managedLedgerDefaultEnsembleSize=3
      - managedLedgerDefaultWriteQuorum=3
      - managedLedgerDefaultAckQuorum=3

# Create topics with 10 partitions
bin/pulsar-admin topics create-partitioned-topic \
    persistent://public/default/dbserver1.public.inventory_products \
    --partitions 10

bin/pulsar-admin topics create-partitioned-topic \
    persistent://public/default/debezium-postgres-topic \
    --partitions 10

bin/pulsar-admin topics create-partitioned-topic \
    persistent://public/default/debezium-postgres-source-debezium-offset-topic \
    --partitions 10

bin/pulsar-admin topics create-partitioned-topic \
    persistent://public/default/elasticsearch-sink \
    --partitions 10

bin/pulsar-admin topics list public/default

# Register source, transformer function, and sink.
bin/pulsar-admin source create --source-config-file connectors/debezium-postgres-source-config.yaml
bin/pulsar-admin sinks create --sink-config-file connectors/elasticsearch-sink.yml
bin/pulsar-admin functions create   --py functions/transformers.py   --classname transformers.PgEsTransformer   --inputs persistent://public/default/dbserver1.public.inventory_products   --output persistent://public/default/elasticsearch-sink

# Collect first and last documents.
curl -X GET "localhost:9200/products/_search?pretty&search_type=dfs_query_then_fetch&size=1&from=0" -H 'Content-Type: application/json' -d'
{
  "sort" : [
    { "_indexed_at" : {"order" : "asc", "format": "strict_date_optional_time_nanos"}},
    "_score"
  ],
  "track_total_hits": true
}
' > first-indexed-entry-replication-3-partition-10.txt
curl -X GET "localhost:9200/products/_search?pretty&search_type=dfs_query_then_fetch&size=1&from=0" -H 'Content-Type: application/json' -d'
{
  "sort" : [
    { "_indexed_at" : {"order" : "desc", "format": "strict_date_optional_time_nanos"}},
    "_score"
  ],
  "track_total_hits": true
}
' > last-indexed-entry-replication-3-partition-10.txt



------------------------------------------------------------------------------------------------------------------------

# Helper commands

bin/pulsar-admin topics delete public/default/elasticsearch-sink
bin/pulsar-admin topics delete public/default/dbserver1.public.django_content_type
bin/pulsar-admin topics delete public/default/dbserver1.public.inventory_categories
bin/pulsar-admin topics delete public/default/dbserver1.public.django_migrations
bin/pulsar-admin topics delete public/default/dbserver1.public.auth_permission
bin/pulsar-admin topics delete public/default/dbserver1.public.inventory_subcategories
bin/pulsar-admin topics delete public/default/debezium-postgres-source-debezium-offset-topic
bin/pulsar-admin topics delete public/default/dbserver1.public.django_session
bin/pulsar-admin topics delete public/default/dbserver1.public.users
bin/pulsar-admin topics delete public/default/dbserver1.public.inventory_products
bin/pulsar-admin topics delete public/default/debezium-postgres-topic

docker rm broker bookie bookie2 bookie3 zookeeper pulsar-init

curl -X GET "localhost:9200/products/_search?pretty&search_type=dfs_query_then_fetch&size=1&from=0" -H 'Content-Type: application/json' -d'
{
  "sort" : [
    { "_indexed_at" : {"order" : "desc", "format": "strict_date_optional_time_nanos"}},
    "_score"
  ],
  "track_total_hits": true
}
'

CSRF_TOKEN=$(curl http://localhost:7750/pulsar-manager/csrf-token)
curl \
   -H 'X-XSRF-TOKEN: $CSRF_TOKEN' \
   -H 'Cookie: XSRF-TOKEN=$CSRF_TOKEN;' \
   -H "Content-Type: application/json" \
   -X PUT http://localhost:7750/pulsar-manager/users/superuser \
   -d '{"name": "admin", "password": "apachepulsar", "description": "test", "email": "username@test.org"}'

docker-compose up --build --force-recreate --no-deps -d
