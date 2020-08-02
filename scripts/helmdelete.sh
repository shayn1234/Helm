#!/bin/bash
export KUBECONFIG=/etc/kubernetes/admin.conf
helm delete my-package --purge



