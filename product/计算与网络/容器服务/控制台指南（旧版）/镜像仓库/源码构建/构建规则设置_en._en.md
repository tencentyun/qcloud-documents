## Preconditions
If you want to build container images through a Git repository, you first need to complete [source code repository authorization](https://cloud.tencent.com/document/product/457/10153).

## Steps
1. Log in to the [Tencent CCS Console](https://console.cloud.tencent.com/ccs).
2. Click "Image Registry" on the left navigation bar, and click "My Images" in the drop-down list to go to "My Image Registries" page, and then click "Building Configuration" on the right side.
![](//mc.qcloudimg.com/static/img/450d3f500a9ceb3d2269e71a6ca3f9af/image.png)
3. Go to the "Building Rule" page and configure the relevant information:
### Github Building Rule
 - **Code source**: Select Github.
 - **Organization**: Select your organization (usually your Github account), or choose one of the organizations you belong to.
 - **Repository**: Select a registry through which you need to build a container image.
 - **Trigger method**: Check mode. The building of a container image can be automatically triggered when the code is pushed to a branch or a new Tag. You can also check none of these options, and directly go to the image registry details page, and then select "Build Image" tab to manually build one.
 - **Version naming rule**: The container image **Tag naming rule**. An image Tag name can be formatted and contain branch name/registry Tag name.
 i: **Update time**: The time when an image is built.
 ii: **commit number**: The latest commit number of branch/Tag.
 >**Note:**
 > If an image is automatically built on a branch or a Tag, and the version naming rule contains branch/Tag, the branch or Tag name can be a combination of uppercase/lowercase letters, underscores (_), and dashes (-), rather than such special characters as /, $, etc.
 - **Dockerfile path**: The **relative path** of Dockerfile in the registry. It is left empty by default. If it is not specified, Dockerfile is located in the project's root directory. The file name must be "Dockerfile". If Dockerfile is located in another directory (e.g. the build directory in the registry) and the file name is Dockerfile, the Dockerfile path is: `build/Dockerfile`.
![](//mc.qcloudimg.com/static/img/1f5a9fd325da7dd63ea4c4408f314d3f/image.png)

### Gitlab Building Rule
- **Code Source**: Select Gitlab.
- **Group**: Select a Gitlab Group.
- **Repository**: Select a registry through which you need to build a container image.
- **Trigger method**: Check mode. The building of a container image can be automatically triggered when the code is pushed to a branch or a new Tag. You can also check none of these options, and directly go to the image registry details page, and then select "Build Image" tab to manually build one.
- **Version naming rule**: The container image **Tag naming rule**. An image Tag name can be formatted and contain branch name/registry Tag name.
 i: **Update time**: The time when an image is built.
 ii: **commit number**: The latest commit number of branch/Tag.
 >**Note:**
 > If an image is automatically built on a branch or a Tag, and the version naming rule contains branch/Tag, the branch or Tag name can be a combination of uppercase/lowercase letters, underscores (_), and dashes (-), rather than such special characters as /, $, etc.
- **Dockerfile Path**: The **relative path** of Dockerfile in the registry. It is left empty by default. If it is not specified, Dockerfile is located in the project's root directory. The file name must be "Dockerfile". If Dockerfile is located in another directory (e.g. the build directory in the registry) and the file name is Dockerfile, the Dockerfile path is: `build/Dockerfile`.
![](//mc.qcloudimg.com/static/img/b5732ca8ff3d6e27efe562e0a2a534f6/image.png)

## Auto Building
If you complete the configuration of building rule, and select "When an new Tag is added" or "When code is submitted to branch" from Trigger Method, the building of a container image is automatically triggered when you submit a new branch or push the code to the specified registry. The entire building process is implemented on Tencent CCS platform. After you finish building, a new image is generated according to the version naming rule you defined, and uploaded to Tencent CCS image registry.




