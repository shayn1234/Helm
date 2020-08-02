from cloudify.workflows import ctx
from cloudify.workflows import parameters as p

for node in ctx.nodes:
    for instance in node.instances:
        ctx.instance.runtime_properties['package_name'] = p.package_name
        instance.execute_operation('helm', kwargs={
        })