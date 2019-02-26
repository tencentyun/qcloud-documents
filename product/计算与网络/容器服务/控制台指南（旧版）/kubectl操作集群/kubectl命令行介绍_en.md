## Overview of Kubectl CLI
kubectl is a CLI for operating on the Kubernetes cluster. This document introduces kubectl syntax, common command operations and examples. For more information on each command (including all main commands and subcommands), please see [Reference Documentation of kubectl](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/), or obtain detailed help by executing the "kubectl help" command. For more information on installation instructions, please see [Install kubectl](https://cloud.tencent.com/document/product/457/8438).

## Creating nginx with kubectl
The following examples can help you get familiar with common operations on kubectl:
### kubectl create
Create a resource from a file or standard input.
> Since a naming conflict always occurs when you create nginx 

```shell
$ kubectl create -f nginx.yaml # nginx-test.yaml file is as follows
```
nginx-test.yaml file is shown below:

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-test
  labels:
    qcloud-app: nginx-test
spec:
  replicas: 1
  revisionHistoryLimit: 5
  selector:
    matchLabels:
      qcloud-app: nginx-test
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        qcloud-app: nginx-test
    spec:
      containers:
      - image: nginx:latest
        imagePullPolicy: Always
        name: nginx-test
        resources:
          limits:
            cpu: 200m
            memory: 128Mi
          requests:
            cpu: 200m
            memory: 128Mi
        securityContext:
          privileged: false
      serviceAccountName: ""
      volumes: null
      imagePullSecrets:
      - name: qcloudregistrykey
status: {}
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-test
  labels:
    qcloud-app: nginx-test
spec:
  ports:
  - name: tcp-80-80-ogxxh
    nodePort: 0
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    qcloud-app: nginx-test
  type: LoadBalancer
status:
  loadBalancer: {}
```

![Alt text][create]



Obtain public network access address through "kubectl get services", enter the IP in the browser, and then you can directly access the nginx service.
![Alt text][get]
![Alt text][show]

### kubectl logs
Print logs in the container.
```shell
// Return a snapshot of the logs from pod <pod-name>.
$ kubectl logs <pod-name>
```
![Alt text][logs]



[create]:https://mc.qcloudimg.com/static/img/a33b8f47e796374d5c457542c1569a9c/image.png
[get]:https://mc.qcloudimg.com/static/img/fb095179d54e49e0287ba3020f7835cf/image.png

[show]:https://mc.qcloudimg.com/static/img/e09ab193d3f1732cc435ba53235094c1/image.png
[logs]:https://mc.qcloudimg.com/static/img/2c34aca3e996296742e6fa9a9be77432/image.png
