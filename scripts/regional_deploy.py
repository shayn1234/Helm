from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from cloudify.manager import get_rest_client

client=get_rest_client()
params= inputs.copy()
params.pop('regions')
for deployment in inputs['regions']:
    client.executions.start(deployment_id=deployment, workflow_id='install_charts_on_clusters', parameters=params)