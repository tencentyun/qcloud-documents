## Practice: One Pod with Multiple Containers
### Advantages of Using One Pod with Multiple Containers
**Share resources and communications**: Containers under the same pod are able to share their data and communications in a more convenient manner. All the containers under the same pod use the same network namespace, IP address and port range. They can discover each other and communicate through localhost. In a flat shared network, every pod has an IP address used to communicate with other CPMs and containers. The pod name will be the CVM name used when communicating with containers. Containers that run inside the same pod also share the same storage volume space. Data in the storage volume is not lost upon container restart and can be read by other containers under the same pod.

**Management**: Compared to native container APIs, the pod provides abstract features on a higher level to simplify container deployment and management procedures. A pod is like a management unit governing management actions and horizontal deployment. It can automatically handle hosting, resource sharing, coordinative replicating and dependency management operations.


### Common Application Scenarios for Single Pod with Multiple Containers
Pod can be used to construct vertically-integrated application stack. However, its main purpose is to manage certain supportive programs in a centralized manner, such as:

- Content management, processes for loading files and data, processes for managing local cache, etc.
- Log compression, rotation, backup, snapshot, etc.
- Data change listening, log and monitor adapters, event distribution, etc.
- Proxies, network bridges, adapters and so on
- Program control, management, configuration, upgrade and so on

For more information, please see [Pod Application Scenarios](http://kubernetes.io/docs/user-guide/pods/#uses-of-pods)

