You can create QPS configurations and bind keys in the usage plan you created, that is, you can limit the maximum number of calls under this usage plan.

For example, if you have created a pair of "secret_id + secret_key" and also a usage plan with a QPS of 1000, bind the "secret_id + secret_key" to the usage plan. Then bind the usage plan to the environment where you want to limit traffic, such as the publishing environment. For the APIs in the publishing environment, users who call "secret_id + secret_key" can call APIs in this environment with a QPS of 1000.

The maximum QPS for each usage plan is 2000.

