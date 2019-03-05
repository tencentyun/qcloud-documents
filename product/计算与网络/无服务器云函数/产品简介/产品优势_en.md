## Simple to Use

### Low Component Cost
When using SCF, users only need to compose the most important "core code" without being concerned about the other components such as load balancing, auto scaling, gateway and so on. This greatly reduces the complexity for constructing service structures.

### Auto Scaling
SCF automatically scales in/scales out based on the number of requests without the need for manual configuration. SCF can always assign a reasonable amount of computing resources automatically to satisfy your business requirement, be it regular services (such as log statistics) with only several requests each day, or those with thousands or even tens of thousands of requests every second (such as mobile application backend).

## Efficient, Innovative Development

### Accelerated Development
SCF does not require certain frameworks or dependent elements, thus developers can focus on developing their core code. At the same time, developers may establish multiple teams. The members who develop a certain module do not need to understand the code details of other teams. Independent development and iteration have become faster than ever, allowing users to seize the best chances to launch their products.

### Reusing Third-Party Services
You can use SCF to compose logically separated business modules with sole purposes, which is completely possible to achieve by reusing established third-party code. For example, realize login module by using oAuth.

### Simplified OPS
Each function is executed, deployed and scaled independently. The functions can be automatically deployed once users upload their code, avoiding deployment and upgrade difficulties of monolith applications.

## Stable and Reliable

### Highly Available Deployment
SCF automatically and randomly chooses available zones in each region to run. When a certain availability zone goes down due to disaster or power failure, infrastructures in another availability zone will be automatically chosen for the cloud function to run, eliminating the failure risk when function only runs in a single availability zone.

### Working Together with Other Computing Services
Permanent workload can be hosted by CVMs, and event-triggered workload can be hosted using SCF. Different cloud services can be used to satisfy different business scenarios and demands, making your service structure more robust.

## Simplified Management
### Simplified Security Configuration
Users do not need to perform complex configuration and management work regarding OS intrusion, login risk, file system security, network security and port listening, everything is handled by the platform, which ensures that every user is separated via customized containers.

### Visualized Management
Users can directly manage their function code and determine when to execute the functions (function triggers) from the console, as well as deploy and test the functions without the need for complicated configuration files.

## Greatly Reduced Cost

### No Service Fee When Idle
No service fee is charged when functions stay idle. This greatly reduces cost for non-permanent business processes. When functions are running, service fee is determined by number of requests and how long the computing resources have been running. This pricing advantage is exceptionally friendly to starter developers.


