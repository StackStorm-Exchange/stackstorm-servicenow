# ServiceNow Integration Pack

This integration allows bi-directional communication between StackStorm and ServiceNow REST API

# Overview

This action provides the basic REST primitives necessary to allow communication between StackStorm and ServiceNow. Ideally, this integration will be consumed in a site-specific integration pack that defines actions to specific ServiceNow specific business logic.

ServiceNow provides two videos to demonstrate how to setup Inbound and Outbound Web Service integrations.

* Inbound Integration - https://www.youtube.com/watch?v=EhxgEECd7mQ
* Outbound Integration - https://www.youtube.com/watch?v=WeeDW_iRM8k

An example pack has been included in this pack to show the integration of ServiceNow with these two integration examples.

## Configuration

### Outgoing Integration

Copy the example configuration [servicenow.yaml.example](./servicenow.yaml.example) to
`/opt/stackstorm/configs/servicenow.yaml` and edit as required. It should contain:

* `instance_name` - Upstream Instance Name (e.x.: stackstorm)
* `username` - Username of service account
* `password` - Password of service account
* `custom_params` - Common supported parameters that will be passed to all calls. [Example](https://developer.servicenow.com/app.do#!/rest_api_doc?v=jakarta&id=c_TableAPI)

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

### Incoming Integration

In your ServiceNow Outbound integration, REST endpoints accept JSON payloads. In addition, you must specify the following headers in your payload request:

```
Accept: application/json
Content-Type: application/json
```


## Actions

* `servicenow.approve_change` Set a change request number to approved
* `servicenow.assign_incident_to` assign an incident to a username
* `servicenow.get` - Get an entry using a dictionary query from a ServiceNow Table
* `servicenow.get_non_structured` - Get an entry using a string query from a ServiceNow Table
* `servicenow.get_incidents_assigned_to` - Get incidents assigned to a particular user
* `servicenow.update` - Update an entry in a ServiceNow Table
* `servicenow.set_incident_owner` - Set the owner of an incident record
* `servicenow.insert` - Insert an entry to a ServiceNow Table
* `servicenow.delete` - Delete an entry from a ServiceNow Table
* `servicenow.create_record` - Create an entry to a ServiceNow Table
* `servicenow.get_attachments` - Gets the metadata of all attachments to a ServiceNow Table
* `servicenow.get_attachment` - Gets the metadata of an attachment on a ServiceNow Table
* `servicenow.upload_attachment` - Uploads an attachment to an entry on a ServiceNow Table
