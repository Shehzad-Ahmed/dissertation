import json
from pulsar import Function


class PgEsTransformer(Function):

    def process(self, input, context):
        logger = context.get_logger()
        logger.info("Message {0} received\nContent: {1}".format(context.get_message_id(), input))
        logger.info(type(input))
        input = json.loads(input)
        ouptput = {"_id": str(input["after"]["id"]), "id": str(input["after"]["id"]), "name": input["after"]["category"]}
        return json.dumps(ouptput)
