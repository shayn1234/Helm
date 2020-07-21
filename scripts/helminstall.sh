#!/bin/bash
printf `pwd`
printf "%s" "Helm install ---------------"
kubectl create namespace $1
kubectl create clusterrolebinding $1-admin-binding --clusterrole=cluster-admin --serviceaccount=$1:default
helm install --name $1-$2 --namespace $1 --set nsPrefix=$1
