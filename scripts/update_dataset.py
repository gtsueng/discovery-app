"""
Update meta guide field for existing docs prior to addition of such field.
"""

import logging

from tornado.options import options, parse_command_line

from discovery.utils.controllers import DatasetController
from discovery.data.dataset import DatasetMetadata

options.define('cd2h', default='/guide')
options.define('niaid', default='/guide/niaid/dataset')
options.define('outbreak', default='/guide/outbreak/dataset')
options.define('n3c', default='/guide/n3c/dataset')

options.define('test', default='/TEST')

def updateDocs():
    '''
        Update meta guide field
    '''
    docs = DatasetController.get_all(private=False)
    for doc in docs['hits']:
        has_guide = doc.get("_meta", {}).get('guide', None)
        if not has_guide:
            if doc['@type'] == "outbreak:Dataset":
                metadata = DatasetMetadata.get(doc["_id"])
                res = metadata.update(**{'_meta':{'guide':options.outbreak}})
                logging.info(f'[Outbreak] Updating guide field for doc {doc["_id"]}')
            elif doc['@type'] == "niaid:NiaidDataset":
                metadata = DatasetMetadata.get(doc["_id"])
                res = metadata.update(**{'_meta':{'guide':options.niaid}})
                logging.info(f'[NIAID] Updating guide field for doc {doc["_id"]}')
            elif doc['@type'] == "n3c:Dataset":
                metadata = DatasetMetadata.get(doc["_id"])
                res = metadata.update(**{'_meta':{'guide':options.n3c}})
                logging.info(f'[N3C] Updating guide field for doc {doc["_id"]}')
            else:
                metadata = DatasetMetadata.get(doc["_id"])
                res = metadata.update(**{'_meta':{'guide':options.cd2h}})
                logging.info(f'[Default] Updating guide field for doc {doc["_id"]}')
            logging.info(res)
        else:
            logging.info(f"Doc already has guide {has_guide}")


if __name__ == "__main__":
    updateDocs()
