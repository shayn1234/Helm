#!/bin/bash
export KUBECONFIG=/etc/kubernetes/admin.conf
helm install --name my-package $1
