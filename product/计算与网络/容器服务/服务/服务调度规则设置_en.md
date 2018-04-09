## Overview
By setting the scheduling rules for the alarm settings under the service, you can specify how the containers under the service are scheduled within the cluster. Here are the application scenarios:
- Run Pod on the specified node.
- Run Pod on the node of a scope.
>Note: The scope can be attributes such as availability zone and model.
- Scatter the Pods on nodes (one Pod for each node, and the scheduling for unqualified Pod is disabled).
- Specify coexistence rules for this Pod and other Pods.

## Procedures
### Preconditions
1. Set the scheduling rules in the service advanced settings. The Kubernetes version of the cluster must be 1.7 or later.
2. To ensure that your Pod can be scheduled successfully, make sure that the node has free resources for container scheduling after you completed the scheduling rules setting.

### Configuring Scheduling Rules
If the version of your cluster is 1.7 or later, you can set the scheduling rules in Create Service or Update Service.
![][1]
Here are two scheduling types:
- Node-based scheduling: set Pod scheduling on the node with specified rule, and match the node label.
- Pod-based scheduling: set the scheduling rules between this Pod and Pods under other services, and match Pod tag.

Multiple scheduling rules can be added for the two scheduling types. The description of each rule is as follows:
- In: The value of Label is in the list.
- NotIn: The value of Label is not in the list.
- Exists: The key of Label exists.
- DoesNotExits: The key of Label does not exist.
- Gt: The value of Label is greater than the list value (string match).
- Lt: The value of Label is less than the list value (string match).

Mandatory scheduling switch enables the same Pod not to run on the same node, and the scheduling is disabled for unqualified Pods. If this feature is enabled, each node has only one pod allocated for this service.

## Principles
The scheduling rules of service are mainly implemented by issuing Yaml to Kubernetes cluster. Affinity and anti-affinity mechanism of kubernetes enables the Pod to be scheduled based on certain rules. For more information on Affinity and anti-affinity mechanism of kubernetes, please see [View Details](https://kubernetes.io/docs/concepts/configuration/assign-Pod-node/).

[1]:https://main.qcloudimg.com/raw/8dda9c19080b2a5beda3133b13fa3ace.png

