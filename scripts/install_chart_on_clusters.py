from cloudify.workflows import ctx
from cloudify.manager import get_rest_client
from cloudify.state import ctx_parameters as input

#for node in ctx.nodes:
#    for instance in node.instances:
#        ctx.instance.runtime_properties['package_name'] = input
#        instance.execute_operation('helm.install', kwargs={})


client = get_rest_client()
for n in client.nodes.list():
    ctx.logger.info("node {0}".format(n.id))
    if (n.type=='kubernetes_cluster'):
        for ni in client.node_instances.list(node_id=n.id):
            ctx.logger.info("node {0}".format(ni.id))
            client.node_instances.update(
            ni.id,
            version=ni.version,
            runtime_properties={'package_name': input}
            )
            ctx.logger.info("node {0}".format(input))
            ni.execute_operation('helm.install', kwargs={})
