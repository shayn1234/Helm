#!/bin/bash
export KUBECONFIG=/etc/kubernetes/admin.conf
helm install --name $2 $1
