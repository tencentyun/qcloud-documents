## Operating on Services on the Application Details Page

On the application details page, you can view the status for all services under the application. The service status includes deployment status and running status. Buttons for operations locate on the right side of the corresponding service. Multiple operations can be performed on the service.

![管理应用内服务-01.png-38.6kB][1]

**Deployment status: Describe whether to deploy the resources in the service**

| Status | Description | 
|------------------|-----------------------|
| Not deployed | Only the template content is edited but the service is not deployed |
| Deployed | The template content is edited and the service is deployed |
| Pending update | Re-edit the template content (or configuration items) after the service is deployed |
| Pending deletion | Delete the service from the template content after the service is deployed |

> After the application has been updated on the application updating page, if the template content of the service is modified, the service deployment status is also changed. However, the running status of the service remains unchanged.

**Running status: The actual running status after the service is deployed**

| Status | Description | 
|------------------|-----------------------|
| Running | Service is running normally after being deployed |
| Starting | Service is starting after being deployed |
| Exception | Service pod encountered exceptions while running after the service has been deployed |
| Exception occurred while querying | Failed to query the service information after the service has been deployed |
| - | Service is not deployed and service status information is empty |

## Operations Supported for Services under Different Deployment Statuses

The following operations are allowed to be performed on the services in the application: `Deploy`, `Undeploy`, `Update`, `Delete` and `View YAML. The operations supported for a service under each status are shown below:

| Status | Deploy | Undeploy | Update | Delete | View YAML |
|------------------|-----------------------|----------------------|
| To be deployed | Yes | No | No | No | Yes |
| Deployed | No | Yes | No | No | Yes|
| Pending update | No | Yes | Yes | No | Yes |
| Pending deletion | No | No | No | Yes | No |

## Description of Comparison Status for Service Differentiation
On the application updating page, the comparison between the template content to be modified and the existing template content in the application is automatically done. After this, statuses including `New`, `Unchanged`, `Changed` and `To be deleted` are used, which are described as follows:

| Status | Description |
|------------------|-----------------------|----------------------|
| New | The service is not available in the application but it is added to the modified content |
| Unchanged | There is no difference between the template content to be modified and the existing template content in the application |
| Changed | The template content to be modified is different from the existing template content in the application |
| To be deleted | The service is available in the application but does not exist in the modified content |

  [1]: https://mc.qcloudimg.com/static/img/b663221cda12d355f8019eac3deae488/image.png
