#!/bin/bash
env   
kubectl get pods
helm install --name $2 $1
