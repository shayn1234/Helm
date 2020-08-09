from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from cloudify.manager import get_rest_client

client=get_rest_client()
for deployment in inputs['regions']:
    client.executions.start(deployment_id=deployment, workflow_id='uninstall_charts_on_clusters', parameters=inputs['package_name'])