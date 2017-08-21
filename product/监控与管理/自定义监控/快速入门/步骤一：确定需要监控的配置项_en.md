In addition to the standard monitoring, CCM also monitors the metric you have interest in.

For example, a user needs to monitor the process CPU utilization on the CVM, and notify relevant admin of the process with 80% or higher CPU utilization (suppose that the user has configured the alarm receiving group with the ID of 8888 in Cloud Monitor console). In this example, we use API for API calling (suppose that user ID=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA). You can also operate in CCM console.

Configurations required are as follows:

- Namespace (namespace): proc_monitor (process monitoring)
- Metric (metricName): proc_cpu (process CPU utilization)
- Dimension: (dimensionNames): proc_name (process name), ip (reporting machine IP)
- Statistical method (statistics): Take max value from all the reported data within statistical period 
- Statistical period (period): Calculate data once every 5 minutes

