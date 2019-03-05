## Overview of Image Building
Continuous integration for container enables a container image to be built automatically or manually on Tencent CCS Platform.

### Auto Building
The auto building of container images based on github or gitlab code repository requires that **the code repository must contain Dockerfile**. You need to register the token of github/gitlab server first. The **gitlab server used for the code repository must be accessed through public network**. You can configure an auto building rule for a specific code repository. When you push code to the code repository, if the auto building rule is matched, an container image is automatically built on Tencent CCS Platform and then automatically pushed into Tencent CCS image repository.
You need to follow these steps for auto building:
- Step 1: [Source Code Repository Authorization](https://cloud.tencent.com/document/product/457/10153)
- Step 2: [Building Rule Configuration](https://cloud.tencent.com/document/product/457/10152)
- Step 3: Submit the code for auto building.

### Manual Building
Manual building is divided into two categories:

- **Based on github and gitlab code repositories**
Similar to auto building, a code repository also needs to contain Dockerfile. Gitlab in which a code repository locates should be accessed through public network. Different from an auto building rule in which a container image is automatically built when you push code to the repository, manual building requires you to built an image on the console by manually clicking build button.

- **Based on uploaded Dockerfile**
On the image repository console, you can upload a Dockerfile based on which Tencent CCS platform builds a container image.

### Building Description
- For Dockerfile that is in git repository or manually uploaded, if any external resource is relied on in Dockerfile, the external resource must also be accessed through public network.
- Manual building and auto building are performed on the Tencent CCS platform, so you don't need to provide building environment or server resources.


