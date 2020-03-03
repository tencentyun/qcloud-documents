
Tencent Cloud container cluster kernel supports periodic detection of the container based on kubernetes and kubernetes, which allows you to check the health status of the container and perform the following operations accordingly.

## Health Check Types ##
1. Container liveness check. It is used to check whether the container is alive, similar to the process check via ps. If the container liveness check fails, the cluster will restart the container; if the check succeeds, no operation will be performed.
2. Container readiness check. It is used to check whether the container is ready to handle the user requests. For some programs, it takes a long time for them to start, because they require loading disk data or starting up external modules before providing services. During the startup period, although the process happens, the service cannot be provided. That's where the container readiness check comes in. If the container readiness check fails, the cluster will block the requests for access to the container; if the check succeeds, the container will be available to access.

## Health Check Methods ##

### TCP Port Probe ###
The principle of TCP port probe is as follows: For a container that provides TCP communication service, the cluster periodically establishes a TCP connection to the container. If the connection succeeds, the probe is considered to be successful. Otherwise, the probe fails. To select TCP port probe, a listening port need to be specified for the container. For example, if a redis container with the service port of 6379 is configured with TCP port probe, and its port 6379 is specified as a listening port, the cluster will periodically initiate TCP connection to the listening port. If the connection succeeds, the check is considered to be successful. Otherwise, the check fails.

### HTTP Request Probe ###
HTTP request probe is used to detect the container that provides HTTP/HTTPS service. The cluster periodically initiates HTTP/HTTPS GET requests to the container. If the error code range of HTTP/HTTPS response is 200 - 399, the probe is considered to be successful. Otherwise, the probe fails. When you use HTTP request probe, you must specify a listening port and HTTP/HTTPS request path for the container. For example, if a container provides HTTP services with a service port of 80 and the HTTP check path is /health-check, the cluster periodically initiates the following request for the container:
```GET http://containerIP:80/health-check```

### Check by Executing a Command ###
Check by executing a command is a powerful check method. After the user specify an executable command within the container, the cluster periodically executes the command in the container. If the result is 0, the check is considered successful. Otherwise, the check fails.
Check by executing a command can be used as an alternative to TCP port probe and HTTP request probe:

1. For TCP port probe, a specific program is written to connect the port of the container. If the connection succeeds, the script returns 0; otherwise, it returns -1.
2. For HTTP request probe, a specific script is written to wget the container.
```wget http://127.0.0.1:80/health-check```
Check the returned response. If the code is within 200 - 399, the script returns 0; otherwise, it returns -1.

**Note:** The program to be executed must be placed in the image of the container. Otherwise, the execution will fail because the program cannot be found.

**Note:** If the command is a shell script that cannot be directly specified as a command to execute, a script interpreter needs to added. For example, if the script is /data/scripts/health_check.sh, the program "sh / data/scripts/health_check.sh" needs to be specified when check by executing a command is used. This happens when the cluster is not in the terminal environment when executing the program in the container.

## Other Common Parameters ##
1. initialDelay (in seconds). This parameter specifies when the probe starts after the container is started. For example, if it is set to 5, the health check starts 5 seconds after the container starts.
2. intervalTime (in seconds). This parameter specifies the frequency of health check. For example, if it is set to 10, the cluster will check every 10 seconds.
3. timeOut (in seconds). This parameter specifies the timeout for the health probe, For TCP port probe, HTTP request probe, and check by executing a command, the parameter means TCP connection timeout, HTTP request response timeout, and timeout for executing a command respectively.
4. healthNum (in counts). This parameter specifies the number of successively successful health checks before a container is identified healthy. For example, if it is set to 3, it indicates that the container is considered healthy only when it is detected successfully for 3 times in a row. **Note:** If liveness check is selected, the healthNum can only be set to 1, and other values are invalid. This is because the container can be identified alive with only one successful probe.
5. unhealthNum (in counts). This parameter specifies the number of successively unsuccessful health checks before a container is identified unhealthy. For example, if it is set to 3, it indicates that the container is considered unhealthy only when it is detected unsuccessfully for 3 times in a row.

