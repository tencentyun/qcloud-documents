## About Data Volumes
In Docker, a data volume is a directory in a disk or another container. Its lifecycle cannot be managed. Docker provides volume drivers, but their current features are limited. CCS employs the concept of Kubernetes volume, which supports specific lifecycle management and various volume types, and a pod is able to use any number of volumes.
For more information about Kubernetes volume, please see [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/).

## Volume Type Selection
Tencent Cloud CCS is built based on the Kubernetes orchestration system. The following volume types can be configured when you create a service:
-  **Local disk**: Mount the file directory of the host where the container resides to the specified path of the container (corresponding to Kubernetes' HostPath), or leave the source path (corresponding to Kubernetes's EmptyDir) empty. When it is left blank, mount the temporary directory to which the CVM is assigned to the mount point of the container. `The local disk volume specified with the source path is suitable for the persistent storage of the data to the host of the container`. For more information, please see [Use Local Disk Volume](https://cloud.tencent.com/document/product/457/12133).
- **Cloud disk**: A Kubernetes block storage plug-in extended based on Tencent Cloud CBS. You can specify a Tencent Cloud CBS to be mounted to a container path, and it is migrated along with the container. `The cloud disk volume is used for the persistent storage of data, and is suitable for stateful services such as MySQL. If the cloud disk volume is configured, the maximum number of pods is 1`. For more information, please see [Use Cloud Disk Volume](https://cloud.tencent.com/document/product/457/12131).
- **NFS disk**: You can use Tencent Cloud [CFS](https://cloud.tencent.com/document/product/582/9127) or self-built NFS, and you just need to enter the NFS path, `NFS volume is used for the persistent storage of data that can be read and written many times, and is suitable for scenarios such as big data analysis, media processing and content management`. For more information, please see [Use NFS Volume](https://cloud.tencent.com/document/product/457/12130).
- **Configuration item**: Map the specified key (as the file name) in the configuration file to the container. `Configuration item volume is mainly used for mounting the business configuration file and can be applied to mount the configuration file to the specified container directory`. For more information, please see [Use Configuration File Volume](https://cloud.tencent.com/document/product/457/12134).



## Notes
1. You need to set the mount point of the container after a volume is created.
2. The volume name and the mount point of the container under the same service must be unique.
3. If the source path for local disk volume is left empty, the system assigns a temporary directory at `/var/lib/kubelet/pods/pod_name/volumes/kubernetes.io~empty-dir`. The lifecycle of this volume is the same as that of the pod.
4. If the permission for the mounted volume is not configured, the "read/write" permission is used by default.

