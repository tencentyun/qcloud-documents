## Overview
When you create a service, an image is used to specify the process of the container in the pod. By default, the image runs a default command. To run a specific command or to rewrite the default value of the image, the following three settings need to be used:

- `WorkingDir`: Current working directory
- `Command`: The command used to control the image
- `Args`: Arguments transferred to the command

## Working Directory
Specify the current working directory. Create one if it does not exist. If no directory is specified, you can use the default value during the operation of container. If not specified, WorkingDir defaults to "/".

## Command and Arguments
For more information on how to adapt "docker run" command to Tencent CCS, click to view [Details](/doc/product/457/9883).
 
The image from Docker has the metadata for storing the image information. If you do not specify a command and a parameter for the container, the container may run the default command and parameter used in the creation of the image. By default, they are "Entrypoint" and "CMD" in Docker. For more information, please see [Entrypoint](https://docs.docker.com/engine/reference/builder/#/entrypoint) and [CMD](https://docs.docker.com/engine/reference/builder/#/cmd) from Docker.
If you specify a command and a parameter for the container when creating the service, the default commands "Entrypoint" and "CMD" generated in the creation of the image are overwritten. The rules are as follows:

| Image Entrypoint | Image CMD | Container Command | Container Parameter | Final Execution |
| :-------- | :--------| :------ | :-------- | :------ |
| [ls]   | [/home]|  None  | None    |[ls / home]  |
| [ls]   | [/home]|  [cd]  | None    |	[cd]        |
| [ls]   | [/home]|  None  |[/data] |[ls / data]  |
| [ls]   | [/home]|  [cd]  |[/data] |[cd / data]  |

>**Note:**
>Docker `entrypoint` corresponds to the `Command` on CCS console, and the `CMD` of Docker run corresponds to `Args` on CCS console. When there are multiple parameters, enter these parameters in the parameter field of CCS with each per line.

