After a service is published, you can use API Gateway usage plans for verification and control of traffic, quota, and users, as well as provision of permissions and controls to API users in a simple and easy manner.

A usage plan adjusts and controls the following:
* Verification and security control
* Traffic control


A usage plan takes effect by binding to a service's environment.

An environment of a service can bind multiple usage plans, and a usage plan can also bind environments of multiple services.

>**Note:** Two or more usage plans bound to the same key cannot be bound to the same environment of the same service. Similarly, if two or more usage plans are bound to the same environment of the same service, they cannot be bound to the same key.
