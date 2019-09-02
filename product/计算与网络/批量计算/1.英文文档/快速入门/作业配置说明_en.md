## 1. Introduction
The job configuration of Batch is provided in JSON format as described below. Two tasks are contained in the following job.

```
{
    "JobName": "TestJob",       // Job name
    "JobDescription": "for test ",    // Job description
    "Priority": "1",            // Job priority
    "Tasks": [                  // Task list (this example contains two tasks)
        {       
            // Task 1 (the simplest task configuration without any non-required options) 
            "TaskName": "Task1",   // Name of task 1
            "Application": {        // Task execution command
                "DeliveryForm": "LOCAL",    // Delivery method of application
                "Command": "echo hello"     // Command content (output hello)
                
            },
            "ComputeEnv": {         // Computing environment configuration
                "EnvType": "MANAGED",   // Computing environment types: MANAGED and UNMANAGED
                "EnvData": {        // Detailed configuration (the current type is MANAGED. See description of CVM instance creation)
                    "InstanceType": "S1.SMALL1",    // CVM instance type
                    "ImageId": "img-m4q71qnf",      // CVM image ID
                }
            },
            "RedirectInfo": {       // Configuration of standard output redirection           
                "StdoutRedirectPath": "cos://dondonbatchv5- 1251783334.cosgz.myqcloud.com/logs/",  // Standard output (to be replaced)
                "StderrRedirectPath": "cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/"    // Standard error (to be replaced)
            },
            "Authentications": [        // Authentication information
                {
                    "Scene": "COS",     // Scenario (COS is set currently)
                    "SecretId": "***",  // SecretId (to be replaced)
                    "SecretKey": "***"  // SecretKey (to be replaced)
                }
            ]
        },
        {
            // Task 2
            "TaskName": "Task2",   // Name of task 2
            "TaskInstanceNum": 1,   // Number of instances running concurrently in task 2
            "Application": {        // Task execution command
                "DeliveryForm": "LOCAL",    // Execute local command
                "Command": "python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "   // Command content (Fibonacci summation)
            },
            "ComputeEnv": {         // Computing environment configuration
                "EnvType": "MANAGED",   // Computing environment types: MANAGED and UNMANAGED
                "EnvData": {        // Detailed configuration (the current type is MANAGED. See description of CVM instance creation)
                    "InstanceType": "S1.SMALL1",    // CVM instance type
                    "ImageId": "img-m4q71qnf",      // CVM image ID (replaceable)
                    "VirtualPrivateCloud": {        // CVM network configuration (optional)
                        "VpcId": "vpc-cg18la4l",             // VpcId (to be replaced)
                        "SubnetId": "subnet-8axej2jc"           // SubnetId (to be replaced)
                    },
                    "SystemDisk": {                 // CVM system disk configuration
                        "DiskType": "CLOUD_BASIC",
                        "DiskSize": 50
                    },
                    "DataDisks": [                  // CVM data disk configuration
                        {
                            "DiskType": "CLOUD_BASIC",
                            "DiskSize": 50
                        }
                    ]
                }
            },
            "RedirectInfo": {       // Configuration of standard output redirection           
                "StdoutRedirectPath": "cos://dondonbatchv5- 1251783334.cosgz.myqcloud.com/logs/",  // Standard output (to be replaced)
                "StderrRedirectPath": "cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/"    // Standard error (to be replaced)
            },
            "MaxRetryCount": 1,         // The maximum number of retry attempts
            "Authentications": [        // Authentication information
                {
                    "Scene": "COS",     // Scenario (COS is set currently)
                    "SecretId": "***",  // SecretId (to be replaced)
                    "SecretKey": "***"  // SecretKey (to be replaced)
                }
            ]
        }
    ],
    "Dependences": [
        {
            "StartTask": "Task1", 
            "EndTask": "Task2"
        }
    ]
}
```
## 2. Details

### I. Job
A job is a unit submitted by Batch. It contains its own information and the information of one or more tasks as well as the dependencies between tasks.

Name | Type | Required | Description  
-----|------|-----|------
JobName | String | No | Job name
JobDescription | String | No | Job description
Priority | Integer | Yes | Job priority. Task (Task) and task instance (TaskInstance) inherit the job priority
Task.N | array of Task objects | Yes | Task information
Dependences.N | array of Dependence objects | No | Dependency information

### II. Task
A job can contain multiple tasks. A task describes the environment (model, system, image) that the actual computing process depends on, the code package to be executed, command line, storage, network and other related information in batch data computing.

Name | Type | Required | Description | Example
-----|------|-----|------|------
TaskName | String | Yes | A unique task name in a job | Task1
TaskInstanceNum | Integer | Yes | The number of running task instances | 1
Application | Application object | Yes | Application information | 
ComputeEnv | ComputeEnv object | Yes | Running environment information |
RedirectInfo | RedirectInfo object | Yes | Path for Redirection |
InputMappings | array of InputMapping object | No | Input mapping |
OutputMappings | array of OutputMapping object | No | Output mapping |
Authentications | array of Authentication object | No | Authentication information |
MaxRetryCount | Integer | No | The maximum number of retry attempts after a task failed | 3
Timeout | Integer | No | Timeout after a task is launched (in sec) | 3600

#### Application
Name | Type | Required | Description | Example
-----|------|-----|------|------
Command | String | Yes | Task execution command
DeliveryForm | String | Yes | Delivery method of application | LOCAL (running locally), PACKAGE (remote code package)
PackagePath | String | No | Path for remote code package, which must be in .tgz format | ```http://batchdemo-1251783334.cosgz.myqcloud.com/codepkg/codepkg.tgz``` (PACKAGE only)

#### ComputeEnv
Name | Type | Required | Description | Example
-----|------|-----|------|------
EnvType | String | Yes | Computing environment management types (MANAGED and UNMANAGED). | LOCAL (running locally), PACKAGE (remote code package)
EnvData | EnvData object | Yes | The parameters of computing environment |

#### EnvData
Name | Type | Required | Description | Example
-----|------|-----|------|------
InstanceType | String | Yes | CVM instance type. This is required for MANAGED type | img-m4q71qnf
ImageId | String | Yes | CVM image ID. This is required for MANAGED type | S1.SMALL1
others | others | No | Refer to the parameters provided in the CVM API document [Create Instance](https://cloud.tencent.com/document/api/213/9384) | SystemDisk, DataDisks, and VirtualPrivateCloud are supported

#### RedirectInfo
Name | Type | Required | Description | Example
-----|------|-----|------|------
StdoutRedirectPath | String | No | Path for standard output redirection | cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/
StderrRedirectPath | String | No | Path for standard error redirection | cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/

#### InputMapping
Name | Type | Required | Description | Example
-----|------|-----|------|------
SourcePath | String | Yes | Source path | cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/input/
DestinationPath | String | Yes | Destination path | /data/input/

#### OutputMapping
Name | Type | Required | Description | Example 
-----|------|-----|------|------
SourcePath | String | Yes | Source path | /data/output/
DestinationPath | String | Yes | Destination path | cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/output/

#### Authentication 
Name | Type | Required | Description  
-----|------|-----|------
Scene | String | Yes | Authentication scenario, such as COS
SecretId | String | Yes | SecretId
SecretKey | String | Yes | SecretKey 

### III. Dependence
Dependence describes the priorities of tasks. If a job contains two tasks: StartTask for Task 1, EndTask for Task 2. Task 2 is launched only after the execution of Task 1 is completed. When Task 2 is completed, the entire job is finished.

Name | Type | Required | Description | Example
-----|------|-----|------|------
StartTask | String | Yes | Name of start task in dependency | Task1
EndTask | String | Yes | Name of end task in dependency | Task2

