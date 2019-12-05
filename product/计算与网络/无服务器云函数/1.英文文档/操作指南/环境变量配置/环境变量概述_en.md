When creating or editing a cloud function, you can add, delete, or modify the environment variables for the operating environment of cloud function by modifying the environment variables in the advanced configurations.

## Adding Environment Variables

When creating or editing a function, click the **Show Advanced Settings** button to show the advanced settings.

Go to **Advanced Settings** -> **Environment Variable Configuration** -> **New Environment Variable**, and the pop-up Add Environment Variables box appears.

The environment variable is usually a key-value pair. Enter the environment variable key into the first input box, and the environment variable value into the second one.

## Viewing Environment Variables

You can learn about the configured environment variables by viewing the function configuration of cloud function. The environment variables are in the form of `key=value`.

## Using Environment Variables

The set environment variables will be configured in the operating environment of the function when it runs. You can use the codes to read the system environment variables to obtain the specific values and use them in the codes.

Assume that the key of the configured environment variable for the cloud function is `key`, the following are code examples to read and print the value of this environment variable in different operating environments.

In Python environment, the method to read the environment variable:
```
import os
value = os.environ.get('key')
print(value)
```

In Node.js environment, the method to read the environment variable:
```
var value = process.env.key
console.log(value)
```

In Java environment, the method to read the environment variable:
```
System.out.println("value: "+ System.getenv("key"));
```

## Application Scenarios

* Variable value extraction: The values that may vary in the business can be set as environment variables to avoid code modification caused by business changes.
* Encryption information: The keys related to verification and encryption can be set as environment variables to avoid the security risk caused by the keys hard-coded in the codes.
* Environment distinction: The configuration and database information can be set as environment variables to easily execute the corresponding databases in different development stages by modifying the values of the environment variables.

## Service Limits

Service limits on the environment variables of cloud function is as follows:

- A maximum of 128 environment variables can be set for a single cloud function. 
- For each environment variable, the maximum size of key is 64 bytes, and that of the value is 128 bytes, and the value is not allowed to be empty. 
- The key must begin with the letter **[a-zA-Z]** and can only contain letters, numbers and underscore (**[a-zA-Z0-9_]**).
- The reserved keys of environment variables cannot be configured, including the keys that begin with SCF\_ (e.g. SCF\_RUNTIME) and the keys that begin with QCLOUD\_ (e.g. QCLOUD\_APPID).

