from cloudify.workflows import ctx
from cloudify.manager import get_rest_client
from cloudify.state import workflow_parameters as wf_input


def update_props(ni):
    client = get_rest_client()
    client_ni = client.node_instances.get(ni.id)
    props = client_ni.runtime_properties
    props['package_name'] = wf_input['package_name']
    client.node_instances.update(
        client_ni.id,
        version=client_ni.version,
        runtime_properties=props
    )


for ni in ctx.node_instances:
    if ni.node.type == 'kubernetes_helm_cluster_settings':
        update_props(ni)

ctx.refresh_node_instances()

op_base = 'cloudify.interfaces.lifecycle.'

graph = ctx.graph_mode()
seq = graph.sequence()
for ni in ctx.node_instances:
    if ni.node.type == 'kubernetes_helm_cluster':
        for op in ['helm_create', 'helm_configure', 'helm_install']:
            seq.add(ni.execute_operation(op_base + op, kwargs={}))
graph.execute()
