## Variable Substitution

Variable substitution is supported in application templates. A variable has a structure of `{{.}}`, with a variable name following the `.`. The variables to be substituted are substituted by the values of configuration items in the configuration file when the template is parsed. For example, if you define FRONTEND_REPLICAS in the template:
```
spec:
 replicas: {{.FRONTEND_REPLICAS}}
```

And set the FRONTEND_REPLICAS variable value in the configuration item to:

```
FRONTEND_REPLICAS: 2
```
Then, the `{{.FRONTEND_REPLICAS}}` in the template file is substituted with "2" in the configuration file when the template is parsed.

Note: The variable name needs to satisfy the regular expression "[A-Za-z_][A-Za-z0-9_]*", with a maximum of 64 characters.

## Custom Variable - ReleaseCBS

If you need to mount a CBS disk in TKE, the description is specified as follows:

```
      volumes:
      - name: vol
        qcloudCbs:
          cbsDiskId: 'disk-pr47vtvt'
          fsType: ext4
```
```
        volumeMounts:
        - mountPath: /mnt
          name: vol
```
(The above description means that the CBS disk disk-pr47vtvt is mounted as a vol disk to the container's /mnt directory.)

A CBS disk can only be mounted to one container at a time. You need to specify different CBS disks when deploying applications in different environments with application templates. Therefore, TKE provides variable ReleaseCBS to represent CBS disk. During the application deployment, the **specific CBS disks available for the applications** are selected for deployment. The example is as follows:

```
      volumes:
      - name: vol
        qcloudCbs:
          cbsDiskId: '{{.ReleaseCBS_pr47vtvt}}'
          fsType: ext4
```

[Screenshot of CBS disk selection for CBS application deployment]

## Custom Variable - ReleaseSubnetId

In TKE, if the service access method is set to "Access in VPC", you need to specify the SubnetId for the Lb in the description file by defining the following result in the service description file. The subnet-s1jz1ycx is the specified SubnetId.
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: 'subnet-s1jz1ycx'
```
SubnetId must be under the VPC (virtual private cloud) where the cluster resides, so it may vary with different clusters. To make it easer to set SubnetId in application deployment, the SubnetId to be set is identified by the variable ReleaseSubNetId in the template. The example is as follows:
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: '{{.ReleaseSubnetId_XXXX}}'
```
In the process of application deployment, a SubnetId is specified for the variable ReleaseSubnetId_XXXX in the configuration file.

Note: Different SubnetIds may be set for the multiple services in the application. Therefore, a "_" (underscore) and service name are added after the ReleaseSubnetId name to distinguish between SubnetIds for services.

## Custom Variable - ReleaseConfig

Configuration file is very important for running a program. Many programs need to read the configuration files from a certain location on the disk. Kubernetes supports mounting a key in confimap to the specified directory of the container. For more information on Kubernetes configmap, please see [Kubernetes offical documents][1].

If the application contains a configuration file, you can mount the key in the application's configuration file to the specified directory of the container.

The example is as follows:
```
      volumes:
      - configMap:
          Name: '{{.ReleaseConfig}}'
          items:
          - key: NAMESPCE
            mode: 511
            path: NAMESPCE
          - key: FRONTEND_REPLICAS
            mode: 511
            path: FRONTEND_REPLICAS
        name: data
```

The mount point is set as follows:
```
        volumeMounts:
        - mountPath: /mnt
          name: data
```

The application's configuration information:
```
NAMESPACE: default
FRONTEND_REPLICAS: 2
```

In this way, the keys NAMESPACE and FRONTEND_REPLICAS in the configuration file will be mounted to the container's /mnt directory, with the filenames being NAMESPACE and FRONTEND_REPLICAS respectively. The file content is the content of the keys in the configuration file.

[1]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
