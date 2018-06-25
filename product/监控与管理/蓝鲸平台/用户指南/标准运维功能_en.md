## 1 Foreword 
"[Standard OPS](http://o.qcloud.com/console?app=gcloud-v2)" is an SaaS service that helps OPS implement automatic cross-system scheduling by using a mature and stable task scheduling engine to integrate the jobs of multiple systems into a single process.
## 2. Product Overview
### 2.1 Features
The process of Standard OPS consists of multiple steps which can be executed automatically or manually in serial or parallel mode. An atom contained in the steps can be a script on the Job Platform, a Tencent Cloud API, or a custom API.
During the task execution, you can suspend the task or skip a failed atom. After parameters are modified for the failed atom, the task can be re-executed.
### 2.2 Benefits
Proper use of Standard OPS can help minimize the error rate during multi-system operation, reduce duplicate work and enhance work efficiency.
### 2.3 Permission System
The role permission of Standard OPS is divided into two types: business admin and business follower.

1.	A business admin inherits from the business OPS role of the configuration platform and has the permissions to create a business process, a task, or a light App.
2.	A business follower needs to be authorized and designated in Standard OPS. The personnel list in the personnel selector is composed of the personnel related to the corresponding businesses in the configuration platform.

The introduction of business admin and follower allows more and more basic OPS work in the enterprise to be done directly by the demand side.
### 3. Term Definition
### 3.1 Component
In BlueKing system, a third-party API interfaced with Enterprise Service Bus (ESB) is called a component.
### 3.2 Atom
According to the business logic of each ESB component, Standard OPS performs secondary encapsulation and add more table interfaces and verification logics, which are called atoms. An atom can be a script job on the Job Platform, a calling of a Tencent Cloud service API or a timer.
### 3.3 Process
In Standard OPS, each operation procedure of a basic OPS scenario is a process. Process is the template of task creation.
### 3.4 Task
In Standard OPS, we can create a task based on a process. Each task is a job of real business scenario, which can be suspended or forcibly terminated.
### 3.5 Step
Step is introduced to help divide different business logics during process execution. A process can be composed of multiple steps, and a step can contain multiple atoms. Steps are executed in serial mode. Atoms in each step can be set to be executed in "serial" or "parallel" mode. The former means that the atoms in a step are executed in order. The latter means that all atoms in a step are executed at the same time.
### 3.6 Business Configuration
If some variables are required in different processes, you can put them in the business configuration.
### 3.7 Variable
When you create or edit a process, variable configuration feature is provided. Different from business configuration, variable configuration in a process can only work on the current process.
Proper use of variable configuration can greatly reduce the input of parameters during task execution.
### 3.8 Light App
Light App is added for finer permission control. You can create a light App out of an executed task and authorize a personnel to run the App. Then, the light App is automatically displayed on the personnel's BlueKing desktop. The user-friendly task interface of Standard OPS allows any person to execute the task, even those with no technical background.
## 4. Product Features
BlueKing Standard OPS has the following features:
![Standard OPS Features](https://mc.qcloudimg.com/static/img/511b4db41d5200f7524d447944effa57/1.jpg)

### 4.1 New Process
Path: "Task Process" -> "New Process"
![Standard OPS New Process](https://mc.qcloudimg.com/static/img/3f3c443fd37cec059abefaacb21d0496/2.jpg)

1. Rename the default process
![Standard OPS New Process](https://mc.qcloudimg.com/static/img/ba0216da64c0c6ac788a8879a534cbc8/3.jpg) 

2. Set the basic attributes of the process
 - a. Select a proper type for the process such as: publishing, region opening, capacity expansion, capacity reduction, migration, server merge and troubleshooting.
 - b. Configure a method via which the message indicating whether process execution is successful or failed is sent. WeChat, email and SMS are supported for now.
 - c. Configure the timeout period for process execution. This is optional.
 - d. Specify a person who is notified of a message indicating whether the task execution is successful or failed.
![Standard OPS New Process](https://mc.qcloudimg.com/static/img/a71254a203bd82cb0807baa716ba4614/4.jpg) 

3. Select a proper atom node from the atom library and drag it to the corresponding step.
![Standard OPS New Process](https://mc.qcloudimg.com/static/img/edb8b8ff0718406bf617e3f9a72bd0d1/5.jpg)
	 
4. Click the corresponding atom in the step and configure the default parameters for atom execution. You can also use variables for replacement.
![Standard OPS New Process](https://mc.qcloudimg.com/static/img/dd132f35a730fe9e6f5488cbf0baa992/6.jpg)

5. If too many steps and atoms are configured, you can click "Preview" button to preview the entire process and then click "Save".
![Standard OPS New Process](https://mc.qcloudimg.com/static/img/aaaaad44c9337ff46d678248a828bcdd/7.jpg)

### 4.2 Task Execution
1. In "Task Process" page, click "New Task" button of each process to create a task.	
![Task Execution](https://mc.qcloudimg.com/static/img/1d14abaf23ab6b2c12d0628e953b1f24/421.jpg) 

2. Select the atom of the step to be executed (you can also select the atom quickly by clicking the corresponding view) and click "Next".
![Task Execution](https://mc.qcloudimg.com/static/img/89980ce64765d5be3bb30f3d43ad0e89/422.jpg)
  
3. Enter the variable parameters to be replaced during task execution and click "Next".
![Task Execution](https://mc.qcloudimg.com/static/img/ec818a8a7c15268816740b16a72e802f/423.jpg) 

4. In the last step, you can check the execution parameters again, or modify the parameters. Upon confirmation of all parameters, click "Start Execution". During the task execution, you can suspend or terminate the task. If an atom is failed, you can skip it or modify the parameters and try again.
![Task Execution](https://mc.qcloudimg.com/static/img/77f46262b7ee4b02fbed42c07fbae06a/424.jpg)
  
### 4.3 New Light App
You can create a light App out of a successfully executed task, which can be displayed on the BlueKing desktop of an authorized user. For this authorized user, the light App only has two stages: "Enter Parameters" -> "Run". The task interface is user-friendly and simple enough that even a person with no technical background can run the Light App.
![New Light App](https://mc.qcloudimg.com/static/img/9e9129cf5778b9e38f60c66c353d5ae2/431.jpg) 

## 5. Cases
### 5.1 Tencent Cloud CDN Prefetch
#### 5.1.1 Create a new process, rename it to "CDN Prefetch", and select "Publish" as the process type
![Case](https://mc.qcloudimg.com/static/img/cf77b0acc3890faf86c6392c45e4ee93/511.jpg) 

#### 5.1.2 Drag CDN prefetch atom to the process, and click the atom to open parameter configuration page
○	Select whether to force a refresh as needed

○	Select "Add as a Variable" for prefetch URL

○	Select "Operation Execution" as the timing type
![Case](https://mc.qcloudimg.com/static/img/5a0fa35e4b07042f1bdfcb1cac297ac9/512.jpg)  

#### 5.1.3 Drag consistency verification atom to the process, and click the atom to open parameter configuration page
○	Click variable configuration tab to copy the KEY of prefetch URL variable and paste it into the URL of consistency verification atom
![Case](https://mc.qcloudimg.com/static/img/83e5332b238954ddf4d55d1b5d7b26d6/513.jpg) 
 
○	Select "Operation Execution" as the timing type
Drag CDN prefetch atom to the process, and click the atom to open parameter configuration page

#### 5.1.4 Click "Save" and then click "Create Task"
![Case](https://mc.qcloudimg.com/static/img/1d8bb8302917ecefb21bc157c46cd08f/514.jpg)  

#### 5.1.5 Select the steps to be executed (all selected by default), and click "Next"
#### 5.1.6 Enter the actual value of prefetch URL variable
![Case](https://mc.qcloudimg.com/static/img/bec71f0306d57664acfe3ca599d4d573/515.jpg) 
 
#### 5.1.7 Click "Next" to start task execution

## 6. Ask for Help
If you have any question or suggestion, post it to our [Forum](http://bbs.bk.tencent.com/forum.php?mod=forumdisplay&fid=60).
