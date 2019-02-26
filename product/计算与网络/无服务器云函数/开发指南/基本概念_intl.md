When you write code using a language supported by the SCF platform, you need a general pattern which includes the following key concepts:

## Execution Method 
The execution method determines where the SCF platform begins to execute your code. It is specified in the format of `file name.method name` by the user. When calling a cloud function, SCF executes your code by searching for the execution method. For example, if you specify `index.handler` as the execution method, the platform first locates the index file in the code package and then finds the handler method in the file to start execution.

When writing the execution method, you need to follow the platform-specific programming model, which specifies fixed input parameters: event data "event" and context data "context". The execution method should process the parameters and can call any other methods in the code.
 
## Input Parameter event
SCF platform passes the event object to the execution method as the first parameter. With this event object, the code interacts with the event that triggers the function. For example, as the file upload triggers the function, the code can obtain all information of the file from the event parameter, including file name, download path, file type, size, etc.
 
## Log
 
SCF platform stores all the function call records and the output in function codes in the log. Please use the specific log statement in programming languages to generate the output for debugging and troubleshooting.

## Notes
Based on the features of SCF, you *must* write function code in a stateless style. The status features within a function lifecycle such as local file storage will be terminated with the function at the end of a function call. Therefore, persistent statuses should be stored in COS, Memcached or other cloud storage services.


