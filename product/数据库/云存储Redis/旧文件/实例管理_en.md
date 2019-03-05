## 1	Working with Cloud Redis Store (CRS)

  You can purchase CRS directly in the product purchase page.
  [Click to Purchase](https://buy.cloud.tencent.com/redis)
## 2	Managing Instances

### 2.1	Creating an Instance

You can create a instance in the console.
	
1) Click **New** to create an instance.
 
2) Select the instance region.
  
3) If VPC has been created, you can specify the VPC for the instance in its network. If VPC is not available, this option is invisible.
  
4) Select the desired capacity.
 
5) Check whether the information entered is correct, and click **OK**.
  
6) Check the status of the instance to be created.
- If it is in a status of "Creating", please wait a few minutes.
- If it is in a status of "To be initialized", it has been created.

7) After creating, initialize the password for the instance.

8) Note: You can access the instance by using <instance ID: user password> as the access password.
 

Create a instance:
![](https://mc.qcloudimg.com/static/img/ec6230710cd809df88c4ab7d3eb93c27/xinjian.png)




Initialize password for the instance:
	
![](//mccdn.qcloud.com/img569de0e096f15.png)

After the initialization of password, the instance can be put into use:
	
![](//mccdn.qcloud.com/img569de0f790f16.png)

### 2.2	Modifying the Instance Name

When the cursor slides over the instance name, a "Modify" button will appear. Click the button to modify the instance name.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Resis-4.png)

### 2.3	Dynamic Expansion of Instance
1) In the instance list page, select the instance to be expanded, and click the "Expand" button.

2) Drag the bar to the capacity you want the instance to be expanded to, and click "OK" button.

![](https://mccdn.qcloud.com/static/img/263f91ce89177779c35aff6a97389c5a/danji.png)

Note: 	During the expansion of a standalone instance, if the remaining capacity of the machine is insufficient, a migration may be triggered, causing a brief disconnection.
  
## 3	Monitoring Instances

### 3.1	Operation Steps

1) Click on the line of the instance you want to view. The instance monitor console will pop up in the right panel.

2) Choose the time period for which you want to view the monitor data.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Resis-8.png)

## 4	Clearing Instances

You can clear up all the data inside an instance in the instance details page of the console.
	
<span style = "color:#F00">Note: Clearing up data will affect the services provided by the instance, and the instance will become inaccessible during the process. Please proceed with caution.</span>

1) Click the instance name in the instance list and enter its details page.
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Resis-9.png)

2) Click the "Clear Instance" button in the instance details page.
![](//mccdn.qcloud.com/img569de2e0ae341.png)

3) Enter the instance password and click "Clear".
 <span style = "color:#F00"> Note: The password here is the instance password set by the user, rather than the<instance ID: instance password>link password for accessing the instance.</span>
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Resis-11.png)
 
4) When the task is submitted, the instance goes into a "Clearing" status
![](//mccdn.qcloud.com/img569de2a1b3a44.png)
  
5) When the task is completed, the instance goes into a "Running" status and can work normally.
	
