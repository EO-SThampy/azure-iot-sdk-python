# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class RegistryManagerOperations(object):
    """RegistryManagerOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the Api. Constant value: "2020-03-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.api_version = "2020-03-01"

    def get_device_statistics(self, custom_headers=None, raw=False, **operation_config):
        """Retrieves statistics about device identities in the IoT hub’s identity
        registry.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RegistryStatistics or ClientRawResponse if raw=true
        :rtype: ~protocol.models.RegistryStatistics or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_device_statistics.metadata["url"]

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("RegistryStatistics", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_device_statistics.metadata = {"url": "/statistics/devices"}

    def get_service_statistics(self, custom_headers=None, raw=False, **operation_config):
        """Retrieves service statistics for this IoT hub’s identity registry.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ServiceStatistics or ClientRawResponse if raw=true
        :rtype: ~protocol.models.ServiceStatistics or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_service_statistics.metadata["url"]

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("ServiceStatistics", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_service_statistics.metadata = {"url": "/statistics/service"}

    def get_devices(self, top=None, custom_headers=None, raw=False, **operation_config):
        """Get the identities of multiple devices from the IoT hub identity
        registry. Not recommended. Use the IoT Hub query language to retrieve
        device twin and device identity information. See
        https://docs.microsoft.com/en-us/rest/api/iothub/service/queryiothub
        and
        https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-query-language
        for more information.

        :param top: This parameter when specified, defines the maximum number
         of device identities that are returned. Any value outside the range of
         1-1000 is considered to be 1000.
        :type top: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~protocol.models.Device] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_devices.metadata["url"]

        # Construct parameters
        query_parameters = {}
        if top is not None:
            query_parameters["top"] = self._serialize.query("top", top, "int")
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("[Device]", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_devices.metadata = {"url": "/devices"}

    def bulk_device_crud(self, devices, custom_headers=None, raw=False, **operation_config):
        """Create, update, or delete the identities of multiple devices from the
        IoT hub identity registry.

        Create, update, or delete the identiies of multiple devices from the
        IoT hub identity registry. A device identity can be specified only once
        in the list. Different operations (create, update, delete) on different
        devices are allowed. A maximum of 100 devices can be specified per
        invocation. For large scale operations, consider using the import
        feature using blob
        storage(https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities).

        :param devices:
        :type devices: list[~protocol.models.ExportImportDevice]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BulkRegistryOperationResult or ClientRawResponse if raw=true
        :rtype: ~protocol.models.BulkRegistryOperationResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.bulk_device_crud.metadata["url"]

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        header_parameters["Content-Type"] = "application/json; charset=utf-8"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(devices, "[ExportImportDevice]")

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 400]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("BulkRegistryOperationResult", response)
        if response.status_code == 400:
            deserialized = self._deserialize("BulkRegistryOperationResult", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    bulk_device_crud.metadata = {"url": "/devices"}

    def query_iot_hub(
        self,
        query_specification,
        x_ms_continuation=None,
        x_ms_max_item_count=None,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """Query an IoT hub to retrieve information regarding device twins using a
        SQL-like language.

        Query an IoT hub to retrieve information regarding device twins using a
        SQL-like language. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language
        for more information. Pagination of results is supported. This returns
        information about device twins only.

        :param query_specification:
        :type query_specification: ~protocol.models.QuerySpecification
        :param x_ms_continuation:
        :type x_ms_continuation: str
        :param x_ms_max_item_count:
        :type x_ms_max_item_count: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~protocol.models.Twin] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.query_iot_hub.metadata["url"]

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        header_parameters["Content-Type"] = "application/json; charset=utf-8"
        if custom_headers:
            header_parameters.update(custom_headers)
        if x_ms_continuation is not None:
            header_parameters["x-ms-continuation"] = self._serialize.header(
                "x_ms_continuation", x_ms_continuation, "str"
            )
        if x_ms_max_item_count is not None:
            header_parameters["x-ms-max-item-count"] = self._serialize.header(
                "x_ms_max_item_count", x_ms_max_item_count, "str"
            )

        # Construct body
        body_content = self._serialize.body(query_specification, "QuerySpecification")

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize("[Twin]", response)
            header_dict = {"x-ms-item-type": "str", "x-ms-continuation": "str"}

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized

    query_iot_hub.metadata = {"url": "/devices/query"}

    def get_device(self, id, custom_headers=None, raw=False, **operation_config):
        """Retrieve a device from the identity registry of an IoT hub.

        Retrieve a device from the identity registry of an IoT hub.

        :param id: Device ID.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Device or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Device or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_device.metadata["url"]
        path_format_arguments = {"id": self._serialize.url("id", id, "str")}
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("Device", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_device.metadata = {"url": "/devices/{id}"}

    def create_or_update_device(
        self, id, device, if_match=None, custom_headers=None, raw=False, **operation_config
    ):
        """Create or update the identity of a device in the identity registry of
        an IoT hub.

        Create or update the identity of a device in the identity registry of
        an IoT hub. An ETag must not be specified for the create operation. An
        ETag must be specified for the update operation. Note that generationId
        and deviceId cannot be updated by the user.

        :param id: Device ID.
        :type id: str
        :param device:
        :type device: ~protocol.models.Device
        :param if_match:
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Device or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Device or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_or_update_device.metadata["url"]
        path_format_arguments = {"id": self._serialize.url("id", id, "str")}
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        header_parameters["Content-Type"] = "application/json; charset=utf-8"
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters["If-Match"] = self._serialize.header("if_match", if_match, "str")

        # Construct body
        body_content = self._serialize.body(device, "Device")

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("Device", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    create_or_update_device.metadata = {"url": "/devices/{id}"}

    def delete_device(self, id, if_match=None, custom_headers=None, raw=False, **operation_config):
        """Delete the identity of a device from the identity registry of an IoT
        hub.

        Delete the identity of a device from the identity registry of an IoT
        hub. This request requires the If-Match header. The client may specify
        the ETag for the device identity on the request in order to compare to
        the ETag maintained by the service for the purpose of optimistic
        concurrency. The delete operation is performed only if the ETag sent by
        the client matches the value maintained by the server, indicating that
        the device identity has not been modified since it was retrieved by the
        client. To force an unconditional delete, set If-Match to the wildcard
        character (*).

        :param id: Device ID.
        :type id: str
        :param if_match:
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_device.metadata["url"]
        path_format_arguments = {"id": self._serialize.url("id", id, "str")}
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters["If-Match"] = self._serialize.header("if_match", if_match, "str")

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    delete_device.metadata = {"url": "/devices/{id}"}

    def purge_command_queue(self, id, custom_headers=None, raw=False, **operation_config):
        """Deletes all the pending commands for this device from the IoT hub.

        Deletes all the pending commands for this device from the IoT hub.

        :param id: Device ID.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PurgeMessageQueueResult or ClientRawResponse if raw=true
        :rtype: ~protocol.models.PurgeMessageQueueResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.purge_command_queue.metadata["url"]
        path_format_arguments = {"id": self._serialize.url("id", id, "str")}
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("PurgeMessageQueueResult", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    purge_command_queue.metadata = {"url": "/devices/{id}/commands"}

    def get_modules_on_device(self, id, custom_headers=None, raw=False, **operation_config):
        """Retrieve all the module identities on the device.

        :param id: Device ID.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~protocol.models.Module] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_modules_on_device.metadata["url"]
        path_format_arguments = {"id": self._serialize.url("id", id, "str")}
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("[Module]", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_modules_on_device.metadata = {"url": "/devices/{id}/modules"}

    def get_module(self, id, mid, custom_headers=None, raw=False, **operation_config):
        """Retrieve the specified module identity on the device.

        :param id: Device ID.
        :type id: str
        :param mid: Module ID.
        :type mid: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Module or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Module or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_module.metadata["url"]
        path_format_arguments = {
            "id": self._serialize.url("id", id, "str"),
            "mid": self._serialize.url("mid", mid, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("Module", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_module.metadata = {"url": "/devices/{id}/modules/{mid}"}

    def create_or_update_module(
        self, id, mid, module, if_match=None, custom_headers=None, raw=False, **operation_config
    ):
        """Create or update the module identity for device in IoT hub. An ETag
        must not be specified for the create operation. An ETag must be
        specified for the update operation. Note that moduleId and generation
        cannot be updated by the user.

        :param id: Device ID.
        :type id: str
        :param mid: Module ID.
        :type mid: str
        :param module:
        :type module: ~protocol.models.Module
        :param if_match:
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Module or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Module or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_or_update_module.metadata["url"]
        path_format_arguments = {
            "id": self._serialize.url("id", id, "str"),
            "mid": self._serialize.url("mid", mid, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        header_parameters["Accept"] = "application/json"
        header_parameters["Content-Type"] = "application/json; charset=utf-8"
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters["If-Match"] = self._serialize.header("if_match", if_match, "str")

        # Construct body
        body_content = self._serialize.body(module, "Module")

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("Module", response)
        if response.status_code == 201:
            deserialized = self._deserialize("Module", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    create_or_update_module.metadata = {"url": "/devices/{id}/modules/{mid}"}

    def delete_module(
        self, id, mid, if_match=None, custom_headers=None, raw=False, **operation_config
    ):
        """Delete the module identity for device of an IoT hub. This request
        requires the If-Match header. The client may specify the ETag for the
        device identity on the request in order to compare to the ETag
        maintained by the service for the purpose of optimistic concurrency.
        The delete operation is performed only if the ETag sent by the client
        matches the value maintained by the server, indicating that the device
        identity has not been modified since it was retrieved by the client. To
        force an unconditional delete, set If-Match to the wildcard character
        (*).

        :param id: Device ID.
        :type id: str
        :param mid: Module ID.
        :type mid: str
        :param if_match:
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_module.metadata["url"]
        path_format_arguments = {
            "id": self._serialize.url("id", id, "str"),
            "mid": self._serialize.url("mid", mid, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters["api-version"] = self._serialize.query(
            "self.api_version", self.api_version, "str"
        )

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters["If-Match"] = self._serialize.header("if_match", if_match, "str")

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    delete_module.metadata = {"url": "/devices/{id}/modules/{mid}"}
