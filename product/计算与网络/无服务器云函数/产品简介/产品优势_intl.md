## Ease of Use

### Low component cost
When using SCF, users only need to compose the most important "core code" without caring about the other components such as load balance, auto scaling, and gateway. This greatly reduces the complexity of constructing service structures.

### Auto scaling
SCF can automatically increase or decrease resources according to the number of requests without any manual configuration. SCF can assign a reasonable amount of computing resources automatically to satisfy your business requirements, regardless of whether your application deals with only several requests per day (log statistics and other periodic transactions) or tens of thousands of requests per second (such as mobile application backend).

## Efficient and Innovative Development

### Accelerated development
SCF does not require specific frameworks or dependencies, allowing developers to focus on developing the core code. In addition, developers can be divided into teams for different modules, and the developers in each team do not need to care about the code details of other teams. In this way, independent development and iteration have become faster than ever, allowing users to seize the best chance to launch their products.

### Reuse of third-party services
You can use SCF to compose logically separated business modules with sole purposes by reusing established third-party code. For example, implementing the login module by using oAuth.

### Simplified OPS
Each function is executed, deployed and scaled independently. The functions can be automatically deployed after users upload their codes, which solves the deployment and upgrade difficulties of monolithic applications.

## Stability and Reliability

### Highly available deployment
SCF can automatically choose availability zones in each region. When an availability zone goes down due to disaster or power failure, the SCF will automatically run on the infrastructure in another availability zone, which eliminates the risk of failure of a single availability zone.

### Used with other computing services
Permanent workload can be hosted by CVMs, and event-triggered workload can be hosted using SCF. Different cloud services can be used to satisfy different business scenarios and demands, making your service structure more robust.

## Simplified Management
### Simplified security configuration
Users do not need to configure and manage OS intrusion, login risk, file system security, network security and port listening. The platform will manage all the complicated configurations, and use customized containers to ensure isolation of users.

### Visualized management
Users can directly manage their function code and determine when to run the functions (function triggers) in the console, and deploy and test the functions without using any complicated configuration files.

## Greatly Reduced Cost

### No service fee during idle periods
No service fee is charged when functions stay idle, which greatly reduces the cost of non-permanent business processes. The service fee of running functions is charged by the number of requests and the running duration of computing resources. The favorable price is exceptionally friendly to starter developers.


