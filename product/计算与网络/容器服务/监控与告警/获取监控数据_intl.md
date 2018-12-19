## Acquiring Monitoring Data
Tencent Cloud Monitor is enabled for all Tencent Cloud users FREE of charge by default.

You can view the monitoring data of TKE in the following ways:

### Monitoring on TKE Console

#### Cluster Monitoring

- Log in to [TKE Console](https://console.cloud.tencent.com/ccs), and select **Cluster**.
- Click the "Monitor" icon under the ID of cluster whose monitoring data is to be viewed in the cluster list, to view the cluster monitoring information.


#### Service Monitoring

- Log in to [TKE Console](https://console.cloud.tencent.com/ccs), and select **Service**.
- Click the "Monitor" icon under the name of the service whose monitoring data is to be viewed in the service list, to view the service monitoring information.

#### Pod Monitoring

- Log in to [TKE Console](https://console.cloud.tencent.com/ccs), and select **Service**.
- Click the ID of service whose monitoring data is to be viewed in the service list to enter the Service Details page.
- Click the "Monitor" icon under the name of the pod whose monitoring data is to be viewed in the pod list, to view the pod monitoring information.

### Monitoring via API
You can use ``GetMonitorData`` API to acquire the monitoring data of all products. For more information, please see API [Read Monitor Data](https://cloud.tencent.com/document/api/248/4667).
