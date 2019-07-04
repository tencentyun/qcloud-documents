## Disk Mounting Configuration

### What is Volume?
As we know, a Docker image is constructed by overlaying multiple file systems together. When we launch a container, the Docker loads a read-only image layer and adds a read-and-write layer on top of it. Previous changes are lost when the Docker container is deleted and re-launched using this image. The Volume concept is introduced into Docker in order to keep the data and share data among containers. To put it simple, a Volume is a directory or file which can bypass the default integrated file system and exist on the host as a normal file or directory.

In Docker, a volume is just a directory in the disk or another container. Its lifecycle cannot be managed. Volumes supported by local disks became available just recently. Now, Docker provides volume drivers, but their current features are limited. Our containers use the Kubernetes volume concept. Kubernetes volumes supports specific lifecycle management features and various volume types, and a pod is able to use any number of volumes at a time.

For more information about Kubernetes volumes, please see [here](https://kubernetes.io/docs/concepts/storage/volumes/).
### How to Use Container Service Volumes
Tencent Cloud's CCS is built based on the Kubernetes orchestration system, and supports the following volume types:

- emptyDir: Used for temporary storage. Lifecycle is the same as pods. emptydir mode is used if you left the source volume path empty when creating service in Tencent Cloud's CCS.
- hostPath: Specifies that files or directories in the host file system are mounted to a certain path in the container. hostPath mode is used if you enter a source path when creating service in Tencent Cloud's CCS.
- Cloud Disk: Other third-party storage plug-ins similar to Kubernetes (Tencent Cloud is actively participating in open source development and will soon submit relevant plug-ins to the community). Here, it means to mount a Tencent Cloud CBS disk to a certain path in the container. Use this mode by choosing the corresponding CBS disk when creating the volume.
- nfs: Specify an nfs directory

Steps:

- Step 1: Add volume
![Alt text](https://mc.qcloudimg.com/static/img/95fa43aef0712a1c798ac2c762d1d43d/%7BFA88D589-64B7-4F27-90F2-1E8A86485DA6%7D.png)
- Step 2: Set a mount path for the volume in the container configuration
![Alt text](https://mc.qcloudimg.com/static/img/728edfe98f53421d0b621c4f2a290649/%7BE25FD03D-CEAC-406E-8582-913897778175%7D.png)
Note the following when using volumes:

>- The volume mount path can be empty when you create the service;
- The volume names and destination paths in volume mount path entries must be different from each other;
- If you need to mount volumes, the volume names and destination paths in volume mount path entries cannot be empty;
- If the source path for mounting volume is left empty, the system will assign a temporary directory at `/var/lib/kubelet/pods/pod_name/volumes/kubernetes.io~empty-dir`. This is not recommended as the lifecycle of this volume is the same as that of the pod;
- If you don't select permission for the mounted volume, the system will automatically set the permission as read-and-write;
- Volume naming rule: Volume names should consist of lower-case letters, numbers and en dash (-). It must start with a lower-case letter and cannot exceed 20 characters.


### PersistentVolume and PersistentVolumeClaim
Available soon


