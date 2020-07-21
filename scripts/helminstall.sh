#!/bin/bash
printf `pwd`
printf "%s" "Helm install ---------------"
kubectl create namespace $1-$2
kubectl create clusterrolebinding $1-$2-admin-binding --clusterrole=cluster-admin --serviceaccount=$1-$2:default
helm install $2 --name $1-$2 --namespace $1 --set nsPrefix=$1
