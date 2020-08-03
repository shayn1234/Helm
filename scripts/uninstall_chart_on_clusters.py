from cloudify.workflows import ctx
from cloudify.decorators import workflow

@workflow
def uninstall_chart_on_clusters(package_name, **kwargs):
      for node in ctx.nodes:
         for instance in node.instances:
                ctx.instance.runtime_properties['package_name'] = package_name
                instance.execute_operation('unhelm.install', kwargs={})

