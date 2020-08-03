from cloudify.workflows import ctx
from cloudify.decorators import workflow

@workflow
def install_chart_on_clusters(package_name, **kwargs):
      ctx.logger.info("1111")
      node = ctx.get_node('kubernetes_cluster1')
      ctx.logger.info("22222")
         for instance in node.instances:
             ctx.logger.info("33333")
                ctx.instance.runtime_properties['package_name'] = package_name
                instance.execute_operation('helm.install', kwargs={})