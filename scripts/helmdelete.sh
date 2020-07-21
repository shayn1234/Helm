#!/bin/bash
helm delete $1-$2 --purge
kubectl delete namespace $1
kubectl delete clusterrolebinding $1-admin-binding


