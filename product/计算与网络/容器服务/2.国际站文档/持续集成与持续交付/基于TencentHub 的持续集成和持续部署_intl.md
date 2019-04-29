## Overall Process
### Graphic illustration

![Alt text][tencenthubcicd]
1. Configure image sources via TKE Image Registry. `Build with Source Code`, `Build with Dockerfile`, `Manual Upload` are supported.
2. If you configure "Build with Source Code", container image feature is generated automatically every time you submit code.
3. To automatically trigger the update of service upon the generation of image, you need to set a trigger for the image.
4. After "Build with Source Code" and trigger are configured, the building of image is automatically triggered once you submit code, and then the generation of image triggers the update of service automatically.

> #### Notes
>- "Build with Source Code" and trigger are two modules configured independently, so you can choose any steps from one of them.
>- For more information about "Build with Source Code" and "Build with Dockerfile", please see [Overview of Building with Source Code](https://cloud.tencent.com/document/product/457/10151).
>- Trigger supports multiple trigger actions. For more information, please see [Overview of Image Trigger](https://cloud.tencent.com/document/product/457/10155).

## Procedure
### Step 1: Configure continuous building of image with source code
1. Create an image repository `helloworld` to be tested, and enter the helloworld details page.
![Alt text][step1]
2. Note the following when configuring image building:

 - Code source: GitHub and Gitlab are supported.
 - Source code repository: Dockerfile file needs to be included. It is a description of steps for building images. Code is also required. Add code into Dockerfile. For more information, please see [How to Write Dockerfile](https://cloud.tencent.com/document/product/457/9115#dockerfile-.E8.87.AA.E5.8A.A8.E7.BC.96.E8.AF.91.E7.94.9F.E6.88.90.EF.BC.88.E6.8E.A8.E8.8D.90.E4.BD.BF.E7.94.A8.EF.BC.89).
 - The following provides Dockerfile and index files required to test Helloworld. Place Dockerfile and index.html in one root directory.
 
**Dockerfile file**:
```shell
FROM nginx
#file author
MAINTAINER tencentcloudccs
ADD ./ /usr/share/nginx/html
```
**index.html file**:
```shell
hello world
```
- Trigger method: Configure to submit code to branch.
- Dockerfile path: Since both Dockerfile and index.html locate in the same root directory, you can directly enter the path of Dockerfile. For more information, please see [Configuration of Dockerfile Path in Building with Source Code Feature](https://cloud.tencent.com/document/product/457/10618).
![Alt text][step2]

After the configuration for step 1 is completed, the container image is generated automatically every time you submit code. You can submit code for testing, or directly build an image manually.
![Alt text][step3]

### Step 2: Configure continuous deployment for image repository trigger
1. First, you need a target service for the continuous deployment. Create one if no service exists. In this example, we create a [Nginx service](https://cloud.tencent.com/document/product/457/7851).
2. Go to the details page of helloworld image repository that has been configured with "Build with Source Code", to configure a trigger.
![Alt text][step4]
3. After a trigger is added, you should note that:

 - Triggering condition: Determine whether to perform trigger action based on the generated image version number (tag). The trigger action is performed if the trigger condition is met. In this example, we choose "All", which means that the trigger action is performed whenever a new image tag is generated.
 - Trigger Action: The update of specified container of service is supported. Select the service/container that requires continuous deployment.

![Alt text][step5]

After the configuration for step 2 is completed, you can upload/build image manually to verify the trigger. The following is a test for verification of manual building.
### Step 3: Submit code for verification
The continuous integration of image and the continuous delivery of service have been configured in step 1 and step 2. Next, you need to submit code to verify the whole process.
1. Access Nignx service through public network, and you can get the following result.
![Alt text][step6]
2. Update index.html file and submit it to Github. You can check the deployment process.
![Alt text][step7]
3. Access the service again.
![Alt text][step8]

Now, the deployment of continuous integration and delivery based on TencentHub is completed.


[tencenthubcicd]:https://mc.qcloudimg.com/static/img/34c83b4280eb33e35197083330dbad7d/%7BE5F1B207-719E-4F6D-B0AB-D390CED90D22%7D.png

[step1]:https://mc.qcloudimg.com/static/img/9b6de96e4af4dfa36e31e0f5608033e4/%7B8657D57E-E403-4E63-B5EC-894CF5BC864E%7D.png

[step2]:https://mc.qcloudimg.com/static/img/17fcb5e01643d923bb6ea15e83eef439/step2.png

[step3]:https://mc.qcloudimg.com/static/img/1f9872b83b828d91bc2df9a7fb2fe08f/%7B8EA0E3A0-0A0A-451A-85BC-AEF63B74406E%7D.png

[step4]:https://mc.qcloudimg.com/static/img/2c8746f2d4d3c317a3a5afbfd1ed0469/%7BC573A8FF-341A-40DD-A6F3-28D2F0E3EC6B%7D.png

[step5]:https://mc.qcloudimg.com/static/img/46a872c20298deb9d8877e13bfc482a3/%7B29136692-0878-4F89-A14A-6BE54C200129%7D.png

[step6]: https://mc.qcloudimg.com/static/img/f79a067501bb84f32344413000a692c4/%7B90C6BA00-8B63-4194-9FBA-6B60336F584D%7D.png

[step7]:https://mc.qcloudimg.com/static/img/7336d8db7e93d20f2771b4ce31d62a8d/%7B43F6A977-2B44-498B-85A7-B7CA55510738%7D.png

[step8]:https://mc.qcloudimg.com/static/img/4b3e5492bcaa316aba457b1b141ce90b/%7BA5FB88F5-697E-468C-9732-E1893D932875%7D.png

