from cloudify.workflows import ctx
from cloudify.manager import get_rest_client
from cloudify.state import ctx_parameters as input

#for node in ctx.nodes:
#    for instance in node.instances:
#        ctx.instance.runtime_properties['package_name'] = input
#        instance.execute_operation('unhelm.install', kwargs={})


client = get_rest_client()
for ni in client.node_instances.list():
    client.node_instances.update(
        ni.id,
        version=ni.version,
        runtime_properties={'package_name': input}
    )
    ni.execute_operation('unhelm.install', kwargs={})
