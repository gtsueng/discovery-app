
from config_key import *

# *****************************************************************************
# Credentials
# *****************************************************************************
# Define in <project_folder>/config_key.py:
#   COOKIE_SECRET = '<Any Random String>'
#   GITHUB_CLIENT_ID = '<your Github application Client ID>'
#   GITHUB_CLIENT_SECRET = '<your Github application Client Secret>'

# *****************************************************************************
# Elasticsearch
# *****************************************************************************
ES_INDICES = {
    # INTERNAL: 'discover_schema',
    'schema': 'discover_schema_class',
    'dataset': 'discover_dataset'
}

# *****************************************************************************
# Tornado URL Patterns
# *****************************************************************************
APP_LIST = [
    (r"/api/query/?", "biothings.web.handlers.QueryHandler", {"biothing_type": "schema"}),
    (r"/api/registry/query/?", "biothings.web.handlers.QueryHandler", {"biothing_type": "schema"}),
    (r"/api/registry/([^/]+)/([^/]+)/?", "discovery.web.api.SchemaRegistryHandler"),
    (r"/api/registry/([^/]+)/?", "discovery.web.api.SchemaRegistryHandler"),
    (r"/api/registry/?", "discovery.web.api.SchemaRegistryHandler"),
    (r"/api/dataset/query/?", "biothings.web.handlers.QueryHandler", {"biothing_type": "dataset"}),
    (r"/api/dataset/([^/]+)/?", "discovery.web.api.DatasetMetadataHandler"),
    (r"/api/dataset/?", "discovery.web.api.DatasetMetadataHandler"),
    (r"/api/view/?", "discovery.web.api.SchemaViewHandler"),
    (r"/api/gh/([^/]+)/?", "discovery.web.api.GHHandler"),
    (r"/api/gh/?", "discovery.web.api.GHHandler"),
]

# biothings web tester will read this
API_VERSION = ''
API_PREFIX = 'api'

# *****************************************************************************
# Biothings SDK Settings
# *****************************************************************************
ES_QUERY_BUILDER = "discovery.pipeline.DiscoveryQueryBuilder"
DISABLE_CACHING = True  # TODO
