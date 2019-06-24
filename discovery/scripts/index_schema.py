'''
    Schema Indexer
'''
import logging

import requests

from biothings_schema import Schema as SchemaParser
from discovery.web.api.es.doc import Class, Schema


def index_schema(namespace, url, user):
    '''
        Indexing Script
    '''

    req = requests.get(url)
    schema_parser = SchemaParser(req.json())

    schema = Schema()
    schema.meta.id = namespace
    schema._meta.url = url
    schema._meta.username = user
    schema.context = schema_parser.context.get(namespace, None)
    schema.encode_raw(req.text)
    schema.save()

    Class.delete_by_schema(namespace)
    classes = Class.import_from_parser(schema_parser)

    logger = logging.getLogger('discovery.scripts.index_schema')
    logger.info("Indexing %s classes.", len(classes))

    for klass in classes:
        klass.save()

    logger.info("Indexed %s.", namespace)


def main():
    '''
        Interactive Prompt
    '''
    namespace = input("Enter the namespace of your schema:")
    if namespace == 'bts':
        url = ('https://raw.githubusercontent.com/data2health/schemas'
               '/biothings/biothings/biothings_curie.jsonld')
    else:
        url = input("Enter the url where the schema json is hosted:")
    user = input("Enter your github username:")
    index_schema(namespace, url, user)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S')
    logging.captureWarnings(True)
    main()
