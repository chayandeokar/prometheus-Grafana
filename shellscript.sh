#!/bin/bash

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install prometheus prometheus-community/prometheus

helm install grafana grafana/grafana

kubectl expose service grafana — type=LoadBalancer -- name=grafana-ext