An image registry trigger automatically performs trigger actions, such as service update, webhook and messaging, after it helps you create an image. By combining continuous integration, you can implement continuous deployment via trigger.

An image registry trigger has the following four attributes:
- Trigger Name: The name of the created trigger.
- Image Registry: Specify an image registry to be bound with triggers. Currently, an image registry can be bound with up to 10 triggers.
- Trigger Condition: With this attribute configured, a trigger action can be performed only if an image that conforms to a specific Tag (image version) format is submitted.
- Trigger Action: Currently supported trigger action is update of CCS. More trigger actions, such as webhook and messaging, will be available soon.

## Trigger Condition
Currently, Tencent CCS image registry supports three types of Tag trigger expressions which can be used to configure trigger conditions:
- All: Action is triggered when a Tag is created or updated in image registry.
- Specified Tag: Enter multiple Tag names which are separated by semicolons. Action is triggered when a specified Tag is created or updated in image registry.
- Regular Expression: Specify regular expressions for Tag. Action is triggered when a matching Tag is created or updated in image registry.

## Trigger Action
Currently supported trigger action is service update. The configuration of trigger action involves the settings of region, cluster, Namespace, service, container image, and other parameters of CCS.
When a trigger condition is met, a specified container image of the service is updated with the configured parameters.

## Trigger Log
Trigger logs are generated every time a registry trigger performs a trigger action. Trigger logs record various information such as trigger name, trigger condition, trigger action, trigger result, trigger time, etc.

