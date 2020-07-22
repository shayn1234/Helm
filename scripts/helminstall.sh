#!/bin/bash
export KUBECONFIG=/etc/kubernetes/admin.conf
env
helm install --name $2 $1
