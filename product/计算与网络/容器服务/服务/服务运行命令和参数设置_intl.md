When you create a service, an image is used to specify the process of the container in the pod. By default, the image runs a routine command. To run a specific command or to rewrite the default value of the image, the following two settings need to be used:

- command: the command for controlling the operation of the image
- args: the parameter that transferred to the command

### Executing Command and Parameter
The image from Docker has the metadata for storing the image information. If you do not specify a command and a parameter for the container, the container will run the default command and parameter used in the creation of the image. By default, they are "Entrypoint" and "CMD" in Docker. For more information, please see [Entrypoint](https://docs.docker.com/engine/reference/builder/#/entrypoint) and [CMD](https://docs.docker.com/engine/reference/builder/#/cmd) from Docker.
If you specify a command and a parameter for the container when creating the service, the default command "Entrypoint" and "CMD" generated in the creation of the image will be overwritten. The rules are as follows:

| Image Entrypoint | Image CMD | Container Command | Container Parameter | Final Execution |
| :-------- | :--------| :------ | :-------- | :------ |
| [ls]   | [/home]|  None  | None    |[ls /home]  |
| [ls]   | [/home]|  [cd]  | None    |	[cd]        |
| [ls]   | [/home]|  None  |[/data] |[ls /data]  |
| [ls]   | [/home]|  [cd]  |[/data] |[cd /data]  |

