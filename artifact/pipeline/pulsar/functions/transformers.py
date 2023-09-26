import json
from pulsar import Function


class PgEsTransformer(Function):

    def process(self, input, context):
        logger = context.get_logger()
        logger.info("Message {0} received\nContent: {1}".format(context.get_message_id(), input))
        logger.info(type(input))
        input = json.loads(input)
        output = input["after"]
        if not output:
            output = {"id": input["before"]["id"]}
        return json.dumps(output)

# To register the function run the following function creation command within pulsar broker.

# bin/pulsar-admin functions create   --py functions/transformers.py   --classname transformers.PgEsTransformer
# \ --inputs persistent://public/default/dbserver1.public.inventory_products
# \ --output persistent://public/default/elasticsearch-sink
