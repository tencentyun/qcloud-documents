## Collecting Container Logs

Log collection feature is used to collect logs of the specified container in the Kubernetes cluster. You can configure containers from which logs are required to be collected in a flexible manner based on your own needs. Collected log information is output to the user-specified output end in the format of json, and attached with related Kubernetes metadata, including label and annotation of the pod to which the container belongs.

## How to Make the Configuration

1. Create a log collector and specify the service.
![][1]

2. Specify the consumer end of logs.
![][2]

3. View received logs.
![][3]


## What is Log Metadata
Field Name | Meaning
--- | ---
docker.container_id | ID of the container to which logs belong
kubernetes.annotations | Annotations of the pod to which logs belong
kubernetes.container_name | Name of the container to which logs belong
kubernetes.host | IP of machine in which the pod of logs resides
kubernetes.labels | Labels of the pod to which logs belong
kubernetes.namespace_name | Namespace of the pod to which logs belong
kubernetes.pod_id | ID of the pod to which logs belong
kubernetes.pod_name | Name of the pod to which logs belong
log | Log information

[1]:https://mc.qcloudimg.com/static/img/9551fc9f7594eded7e24a3c09486bd43/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/0fe6bed71772b09231771e320a789e9d/image.jpeg
[3]:https://mc.qcloudimg.com/static/img/1424653e838aeb76be107f7cf07eb3bc/containerlog.jpeg


