# By default grafana username and  password is admin 

# Intergation of Grafana with Prometheus it can be done by Adding Data source 

# https://devops4solutions.com/monitoring-using-prometheus-and-grafana-on-aws-ec2/

# prometheus-Grafana

This is a **Work-In-Progress** Repo for learning how monitor your kubernetes clusters using prometheus and visualize using grafana.

Both Prometheus and Grafana have a very good documentation 

[Prometheus Docs]("https://prometheus.io/docs/introduction/overview/")

[Grafana Docs]("https://grafana.com/docs/grafana/latest/")

## Pre-Requisite

- Kubernetes Cluster
- Helm 
- Kubectl perfection 

If you don't have them installed. Follow the below links:

[Install Minikube]("https://minikube.sigs.k8s.io/docs/start/")

[Install Helm]("https://helm.sh/docs/intro/install/")

<br></br>

## It all starts with Monitoring 

Monitoring your Kubernetes cluster is essential for ensuring the health and performance of your applications and infrastructure. Here are some reasons why monitoring your Kubernetes cluster is important:

- Identify issues and troubleshoot: 
- Optimize performance and capacity:
- Ensure high availability: 
- Security and compliance:

<br></br>

## Using Prometheus for monitoring

Prometheus is an open-source monitoring and alerting system that helps you collect and store metrics about your software systems and infrastructure, and analyze that data to gain insights into their health and performance. It provides a powerful query language, a flexible data model, and a range of integrations with other tools and systems. 

--> With Prometheus, you can easily monitor metrics such as CPU usage, memory usage, network traffic, and application-specific metrics, and use that data to troubleshoot issues, optimize performance, and create alerts to notify you when things go wrong.

<br></br>

## Why Prometheus over other monitoring tools ?

Prometheus is a popular choice for Kubernetes monitoring for several reasons:

- Open-source: Prometheus is an open-source project that is free to use and has a large community of contributors. This means that you can benefit from ongoing development, bug fixes, and feature enhancements without paying for a commercial monitoring solution.

- Native Kubernetes support: Prometheus is designed to work seamlessly with Kubernetes, making it easy to deploy and integrate with your Kubernetes environment. It provides pre-configured Kubernetes dashboards and supports auto-discovery of Kubernetes services and pods.

- Powerful query language: Prometheus provides a powerful query language that allows you to easily retrieve and analyze metrics data. This allows you to create custom dashboards and alerts, and to troubleshoot issues more easily.

- Scalability: Prometheus is designed to be highly scalable, allowing you to monitor large and complex Kubernetes environments with ease. It supports multi-node architectures and can handle large volumes of data without significant performance degradation.

- Integrations: Prometheus integrates with a wide range of other tools and systems, including Grafana for visualization, Alertmanager for alerting, and Kubernetes API server for metadata discovery.

<br></br>

## Prometheus Architecture

<br></br>
![Alt text](https://prometheus.io/assets/architecture.png)

<br></br>

## What is Grafana ?

Grafana is a popular open-source data visualization and analytics platform that allows you to create custom dashboards and visualizations based on a variety of data sources. Grafana is often used for monitoring and analyzing metrics and logs in real-time, making it an ideal tool for monitoring systems and applications, including Kubernetes environments.

Grafana supports a wide range of data sources, including databases, time-series databases, and other data storage systems. It provides a powerful query language that allows you to retrieve and analyze data from these sources, and to create custom dashboards and alerts based on that data.

In addition to its powerful data visualization and analysis capabilities, Grafana is also highly extensible. It supports a wide range of plugins and integrations, including integrations with popular monitoring and logging tools like Prometheus, Elasticsearch, and InfluxDB.
