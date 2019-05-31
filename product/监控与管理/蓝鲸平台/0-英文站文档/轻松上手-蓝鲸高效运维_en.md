## 1. User Notice
The BlueKing platform offers various types of application with different features. The following describes the core application used to operate and maintain this platform efficiently, including:

1. 	"Configuration Platform": It is used to configure the relationship between businesses and servers. As the fundamental of all operations, the configuration platform should be operated first because it configures businesses, servers and responsible persons of these businesses to make it easy for users to isolate and manage servers based on permissions. Tencent Cloud's businesses and servers are automatically synchronized to the configuration platform.
2. 	"Agent": It is rather small and has no effects on servers.
3. 	"Job Platform": It is used to run scripts and issue files.
4. 	"Standard OPS": It is a mature process engine.
By using the above applications, you can achieve automatic OPS. The following introduces how to get started with BlueKing.

## 2. Sign up for BlueKing
- A user of Tencent Cloud does not need to sign up for BlueKing and can directly skip to the next step.
- If your colleague has the permission to use BlueKing, you can ask him/her to grant a BlueKing collaborator permission to you following the instructions below:
![](//mccdn.qcloud.com/static/img/9d3447aa5fea73dafb892cabe79520f6/image.jpg)

## 3. Use the Configuration Platform to Manage Servers
On the [BlueKing Configuration Platform](http://o.qcloud.com/console?app=cc-new), server topology is divided by `business`, `cluster`, and `module`.

Step 1: New business (if a Tencent Cloud sub-project is used, skip to the next step)

(1) "Developer View" -> "Business Management"
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/901c965e8636872834b55bec473c8d57/21.jpg) 

(2) Click "New Business", select a level (level-2 or level-3) for the business, and enter the information of the OPS personnel.
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/de298ef1ee4c10f948dc0c523c29cdf5/22.jpg)  

Step 2: Assign servers

(1) "Developer View" -> "Resource Pool Management" (Data from the Tencent Cloud CVM can be automatically synchronized to the server. Data from other clouds or IDCs need to be imported to the server.)
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/40af795553f21d959a3386d340bf0295/23.jpg) 
 
(2) Select a server and assign it to a business.
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/700415d52f854edcb01abccad716986b/24.jpg)  

Step 3: Create a module under the business

(1) Open "Business View" -> "Business Topology"
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/79f57f3242ce4db4d424b84f6383aa81/25.jpg)  

(2) It's a level-2 business. Click "New Module" to add a module and enter the information. 
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/795ce44c68be05c7395408a094a98edc/26.jpg)  

After a module is added

![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/c51a8cbef2439b581e861062edefbd93/27.jpg)  

Step 4: Assign the server to a module

(1) Open "Business View" -> "Server Management"
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/8d3c612a80086a73ff8ef8e86c6d6db3/28.jpg) 

(2) Migrate the servers in the idle server pool to the appropriate modules
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/31b4f9e032ac978b3c542274e5948d02/29.jpg) 
 
After that, each module have a server. The servers are successfully assigned.
![Use the Configuration Platform to Manage Servers](https://mc.qcloudimg.com/static/img/9629d655af6ae30c6afa4ca823792cff/210.jpg)

## 4. Install BlueKing Agent
You may use the [Agent Installation 2.0](http://o.qcloud.com/console?app=agent-setup) provided by BlueKing to install the BlueKing agent:

1. On the BlueKing desktop, click to open the "Agent Installation 2.0" application.
![Agent Installation Page](https://mc.qcloudimg.com/static/img/d42ac76270f7498ec6773dd2b04ffc1c/1.jpg)
2. Switch your business (for multiple businesses).
![Switch the Business](https://mc.qcloudimg.com/static/img/6d6417efcdfc390743e5b68583be0341/2.jpg)

3. Click "Cloud Zone Management" and select the cloud zone you need to work on. Later, a proxy will be assigned to this cloud zone.
![Select a Target Cloud Zone](https://mc.qcloudimg.com/static/img/00588b873a608384cb9b69b7dbaf86eb/3.jpg)

4. Assign a proxy agent for the cloud zone you selected.
![Assign a Proxy Agent to Each Cloud](https://mc.qcloudimg.com/static/img/1a3a0d3a3634e315dcc3d2bdf39d1332/4.jpg)

5. Enter the proxy agent information for the selected cloud. `Password verification` and `key verification` are supported.
![Enter the Proxy Agent Information](https://mc.qcloudimg.com/static/img/2adb9bd00b25f2743f452a4425980843/5.jpg)
6. Install the proxy agent. You can check the details during installation.
![Install a Proxy Agent](https://mc.qcloudimg.com/static/img/024e160ab131900c3b8b23b449a5719d/6.jpg)
![Install a Proxy Agent](https://mc.qcloudimg.com/static/img/87ab34d546df97929796e108beae4721/7.jpg)
7. Install agents to other servers after the proxy agent is installed.
![](https://mc.qcloudimg.com/static/img/a36afd570af671bd9c1e4bcbe1f6ecd0/8.jpg)
8. Enter the agent information for the selected cloud.
![](https://mc.qcloudimg.com/static/img/a8d7991f0a254e0289cfa29711929218/9.jpg)
9. Install the agent. You can check the details during installation.
![](https://mc.qcloudimg.com/static/img/860f44fe4af6b599b3f95a9ffc03b2c5/10.jpg)
![](https://mc.qcloudimg.com/static/img/7d2cd60f73643602a2c971e4feef0693/11.jpg)
10. After installation, go back to the homepage, and then you can see the information of the proxy agent in the business.
![](https://mc.qcloudimg.com/static/img/73ee86e7712e31e7293eecf254d49858/12.jpg)
11. If you want to use the BlueKing agent to manage Windows servers, install cygwin on the Window server. For specific installation procedure, please see the descriptions in the installation page.

## 5. Use the Job Platform to Output a HelloWorld
You can use the two features `script execution` and `file issuing ` provided by the BlueKing Job Platform to migrate your jobs to the cloud for management. The rapid script execution provided by the "[Job Platform](http://o.qcloud.com/console?app=job)" allows you to rapidly execute the script on the server:
1. Fast script execution
![Use the Job Platform to Output a HelloWorld](https://mc.qcloudimg.com/static/img/ba7c445ad89eb74b45d57cbb9ff88e12/31.jpg)
2. Rapid distribution of files
![Use the Job Platform to Output a HelloWorld](https://mc.qcloudimg.com/static/img/cf8636c3a4afee8ec7f1960a5b692a0e/32.jpg)
3. Common job execution
![Use the Job Platform to Output a HelloWorld](https://mc.qcloudimg.com/static/img/c7d50ce8452acd8b6368c2d0bb438a41/33.jpg)
4. New jobs
![Use the Job Platform to Output a HelloWorld](https://mc.qcloudimg.com/static/img/85d52e33ee64161b97ae9369368e4ffc/34.jpg)
5. Timed jobs
![Use the Job Platform to Output a HelloWorld](https://mc.qcloudimg.com/static/img/c0b03cbbf53e9110b64d224727ea51c4/35.jpg)
6. Script management
![Use the Job Platform to Output a HelloWorld](https://mc.qcloudimg.com/static/img/d5b9bac339e56886b3e9bc9c58652a90/36.jpg)

## 6. Standard OPS
Step 1: Create a process

(1) "Task Process" -> "New Process"
![Standard OPS](https://mc.qcloudimg.com/static/img/726ae221b6dba1fd2afbbf52ab76b465/41.jpg) 

(2) When the "New Process" page is opened, you can drag the atom into the process.
 A process contains multiple steps and a step contains multiple atomic nodes. An atom can be a Tencent Cloud API, a script on the Job Platform, and so on.
![Standard OPS](https://mc.qcloudimg.com/static/img/a1eecc110ac8b153e2b73f4cd6c5641c/42.jpg)  

(3) After a process is created, click "Save". Remember to save the atom's parameters as the parameters of the process as prompted. It's very simple.
![Standard OPS](https://mc.qcloudimg.com/static/img/b302868d5d5faf6f8ae86c5cd5977dbc/51.jpg)  

Step 2: Run a process

(1) Select "Task Process" and click "New Task". After entering the parameters of the data process, you can run the process.  
![Standard OPS](https://mc.qcloudimg.com/static/img/44720f20e0990e3715622552b4f03eed/45.jpg) 
![Standard OPS](https://mc.qcloudimg.com/static/img/b11c53915961ea223b744f5632888277/46.jpg) 

(2) Click "Next' and enter parameters
![Standard OPS](https://mc.qcloudimg.com/static/img/c99b5c0d460868bcabfdd9c5ff2a86ad/47.jpg)  

(3) Start running the process
![Standard OPS](https://mc.qcloudimg.com/static/img/a98c82550f79d24bf2473a541c5d4149/48.jpg)
  
(4) Test the process
![Standard OPS](https://mc.qcloudimg.com/static/img/55937aece48c415fa64b996db5e66772/49.jpg) 

The above description provides you an overview of BlueKing. To learn more features and functions, find them in BlueKing.

## 7. Ask for Help
If you have any question or suggestion, post it to our [Forum](http://bbs.bk.tencent.com/forum.php?mod=forumdisplay&fid=60).
