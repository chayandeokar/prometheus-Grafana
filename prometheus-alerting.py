apiVersion: v1
data:
  alertmanager.yaml: |-
    global:
      resolve_timeout: 5m
    route:
      group_by: ['alertname', 'cluster', 'service']
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 3h
      receiver: 'slack'
    receivers:
    - name: 'slack'
      slack_configs:
      - channel: '#alerts'
        send_resolved: true
    inhibit_rules:
      - source_match:
          severity: 'critical'
        target_match:
          severity: 'warning'
        equal: ['alertname', 'dev', 'instance']

    groups:
      - name: kafka_consumer_lag_alerts
        rules:
          - alert: KafkaConsumerGroupLagTooHigh
            expr: kafka_consumergroup_lag{group="console-consumer-93245"} > 100
            for: 5m
            annotations:
              summary: "Kafka Consumer Group Lag Too High"
              description: "The Kafka consumer group lag for group 'console-consumer-93245' is too high."
