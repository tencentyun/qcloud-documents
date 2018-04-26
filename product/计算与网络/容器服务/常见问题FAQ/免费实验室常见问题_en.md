### Error occurs when creating custom application in the example Cluster
#### (-241007) Parameters Not Supported by Example Cluster PUBLIC_CLUSTER_PARAM_CHECK_ERROR[service(******): public cluster service namespace must be u*********]
**Description**: The example cluster isolates users through namespaces. The custom applications must be created under your namespaces, and you can get your namespaces by errors.
**Solution**: Change Namespace to your namespaces.

#### (-241007) Parameters Not Supported by the Example Cluster PUBLIC_CLUSTER_PARAM_CHECK_ERROR[service(******): public cluster pod's cpu limits cannot be zero]

**Description**: The CPU and memory limits of Request and Limit must be set for the POD created under the example cluster.
**Solution**: Complement the limits of Request and Limit at the "resources" field under the "containers" field of the template as shown below:
```yaml
......
containers:
      - image: nginx:latest
        imagePullPolicy: Always
        name: ng
        resources:
          requests:
            requests:
            cpu: 200m
            memory: 128M
          limits:
            cpu: 200m
            memory: 128M
        securityContext:    
          privileged: false
......
```

