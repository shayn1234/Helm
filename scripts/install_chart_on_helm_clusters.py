from cloudify.workflows import ctx
from cloudify.manager import get_rest_client
from cloudify.state import workflow_parameters as input

#for node in ctx.nodes:
#    for instance in node.instances:
#        ctx.instance.runtime_properties['package_name'] = input
#        instance.execute_operation('helm.install', kwargs={})

def update_props(ni):
    client=get_rest_client()
    client_ni = client.node_instances.get(ni.id)
    props = client_ni.runtime_properties
    props['package_name'] = input['package_name']
    client.node_instances.update(
        client_ni.id,
        version=client_ni.version,
        runtime_properties=props
    )

for ni in ctx.node_instances:
    if ni.node.type == 'kubernetes_helm_cluster_settings':
        update_props(ni)

ctx.refresh_node_instances()

for ni in ctx.node_instances:
    if ni.node.type == 'kubernetes_helm_cluster':
        ni.execute_operation('cloudify.interfaces.lifecycle.helm_create', kwargs={})
        ni.execute_operation('cloudify.interfaces.lifecycle.helm_configure', kwargs={})
        ni.execute_operation('cloudify.interfaces.lifecycle.helm_install', kwargs={})
