## Container

The container structure in a container instance

Referenced by the following API: CreateContainerInstance, DescribeContainerInstance, DescribeContainerInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Image | String | Yes | Image |
| Name | String | Yes | Container name, which is composed of lowercase letters, numbers and "-", with a length not more than 63 characters. It begins with a lowercase letter and ends with a lowercase letter or a number. |
| Cpu | Float | Yes | CPU (in cores) |
| Memory | Float | Yes | Memory (in Gi) |
| Command | String | No | Container startup command |
| Args | Array of String | No | Container startup parameters |
| EnvironmentVars | Array of [EnvironmentVar](#EnvironmentVar) | No | Container environment variables |
| RestartCount | Integer | No | Number of times the container restarts |
| CurrentState | [ContainerState](#ContainerState) | No | Current status |
| PreviousState | [ContainerState](#ContainerState) | No | Last status |
| WorkingDir | String | No | Container working directory |
| ContainerId | String | No | Container ID |

## ContainerInstance

Specific information about container instances

Referenced by the following API:  DescribeContainerInstance, DescribeContainerInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| InstanceName | String | Yes | Container instance name |
| VpcId | String | Yes | ID of the VPC to which the container instance belongs |
| SubnetId | String | Yes | ID of the subnet to which the container instance belongs |
| Containers | Array of [Container](#Container) | Yes | Container list |
| RestartPolicy | String | Yes | Restart policy |
| Zone | String | Yes | Availability zone |
| InstanceId | String | No | Container instance ID |
| State | String | No | Container instance status |
| CreatedTime | Timestamp | No | Creation time |
| StartTime | Timestamp | No | Start time |
| VpcName | String | No | VPC name |
| VpcCidr | String | No | VPC CIDR |
| SubnetName | String | No | Subnet name |
| SubnetCidr | String | No | Subnet CIDR |
| LanIp | String | No | Private IP |

## ContainerLog

Container logs

Referenced by the following API: DescribeContainerLog.

| Name | Type | Description |
|------|------|-------|
| Name | String | Container name |
| Log | String | Log |
| Time | String | Logging time |

## ContainerState

Container Status

Referenced by the following API: CreateContainerInstance, DescribeContainerInstance, DescribeContainerInstances.

| Name | Type | Description |
|------|------|-------|
| StartTime | Timestamp | Time when the container starts running |
| State | String | Container status |
| Reason | String | Status details |
| FinishTime | Timestamp | Time when the container finishes running |
| ExitCode | Integer | Exit code of the container |

## EnvironmentVar

Container environment variables

Referenced by the following API: CreateContainerInstance, DescribeContainerInstance, DescribeContainerInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | Environment variable name |
| Value | String | Yes | Environment variable value |

## Event

Container instance events

Referenced by the following API: DescribeContainerInstanceEvents.

| Name | Type | Description |
|------|------|-------|
| FirstSeen | String | First time when the event occurred |
| LastSeen | String | Last time when the event occurred |
| Level | String | Event level |
| Count | String | Event occurrences |
| Reason | String | Event reason |
| Message | String | Event message |

## Filter

Filter conditions

Referenced by the following API: DescribeContainerInstances.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | Available values: Zone, VpcId, and InstanceName |
| ValueList | Array of String | Yes | Filter value list |

## Price

Prices

Referenced by the following API: InquiryPriceCreateCis.

| Name | Type | Description |
|------|------|-------|
| DiscountPrice | Float | Discount price (in CNY) |
| OriginalPrice | Float | Original price (in CNY) |


