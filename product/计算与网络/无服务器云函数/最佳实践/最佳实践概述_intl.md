Based on the features of Serverless Cloud Function (SCF), we recommend that you:

- Write function codes in a stateless style, to ensure that your codes are not maintained in any status. Use COS, Redis/Memcached and other services to cache intermediate information and implement the final computing results because the results of local storage and internal storage may be lost.
- Instantiate any objects that may be reused (such as database connections) other than execution methods.
- Configure +rx (read and execute) permission to your file in the uploaded ZIP to ensure successful execution of codes.
- Minimize the use of startup code that is not directly related to the processing of current event to reduce cost and improve performance if users want to minimize the startup latency. In addition, since the underlying computing resources may be reused to some extent, users can execute the function regularly to use "warm start" for the subsequent calling operations if they want to minimize the startup latency.
- Maximize the use of log/print statements in codes to provide sufficient information for debugging.
- You can use external code management services (such as Git) for the purpose of version and audit management of core codes, to ensure the completeness of codes (version management feature will be available soon).

