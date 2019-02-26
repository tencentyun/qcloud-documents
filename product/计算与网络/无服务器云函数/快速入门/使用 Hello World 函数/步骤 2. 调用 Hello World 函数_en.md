Please use the test template provided by the console to call Hello World function you just created.

1) Click Hello World function you just created in the list page to enter the function details page, and click "Test" button on the right.

2) In the pop-up of testing function, select `Hello World Test Code` from test templates, and the following data will appear in the window. You can make any changes to the value of JSON data (for example, change `test_1` to `my_own_data`), but the modification of sample data structure is not allowed.
```
{
  "key1": "test value 1",
  "key2": "test value 2"
}
```

3) Click "Run" button, and the code starts running and displays test result. Note:
 - The running result (successful or failed) and the function execution result returned by `return` statement in the code will appear in the function return value.
 - The execution time, memory and other information of the function will appear in running information
 - Logs generated during the execution of function will appear in the log, including print statement in user code, trace stack for function execution failure, and so on, and will be written in the log module.

4) You can run the code a couple of times, and click **Logs** tab to check the log information of each run.
