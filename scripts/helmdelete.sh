#!/bin/bash
export KUBECONFIG=/etc/kubernetes/admin.conf
helm delete $2 --purge



