# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class TwinOperations(object):
    """TwinOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the Api. Constant value: '2020-03-13'.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.api_version = "2020-03-13"

    def get_device_twin(self, id, custom_headers=None, raw=False, **operation_config):
        """Gets a device twin.

        Gets a device twin. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-device-twins
        for more information.

        :param id: Device ID.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Twin or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Twin or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_device_twin.metadata["url"]
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
            deserialized = self._deserialize("Twin", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_device_twin.metadata = {"url": "/twins/{id}"}

    def replace_device_twin(
        self,
        id,
        device_twin_info,
        if_match=None,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """Replaces tags and desired properties of a device twin.

        Replaces a device twin. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-device-twins
        for more information.

        :param id: Device ID.
        :type id: str
        :param device_twin_info: Device twin info
        :type device_twin_info: ~protocol.models.Twin
        :param if_match:
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Twin or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Twin or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.replace_device_twin.metadata["url"]
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
        body_content = self._serialize.body(device_twin_info, "Twin")

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("Twin", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    replace_device_twin.metadata = {"url": "/twins/{id}"}

    def update_device_twin(
        self,
        id,
        device_twin_info,
        if_match=None,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """Updates tags and desired properties of a device twin.

        Updates a device twin. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-device-twins
        for more information.

        :param id: Device ID.
        :type id: str
        :param device_twin_info: Device twin info
        :type device_twin_info: ~protocol.models.Twin
        :param if_match:
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Twin or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Twin or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_device_twin.metadata["url"]
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
        body_content = self._serialize.body(device_twin_info, "Twin")

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("Twin", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    update_device_twin.metadata = {"url": "/twins/{id}"}

    def get_module_twin(self, id, mid, custom_headers=None, raw=False, **operation_config):
        """Gets a module twin.

        Gets a module twin. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-device-twins
        for more information.

        :param id: Device ID.
        :type id: str
        :param mid: Module ID.
        :type mid: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Twin or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Twin or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_module_twin.metadata["url"]
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
            deserialized = self._deserialize("Twin", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    get_module_twin.metadata = {"url": "/twins/{id}/modules/{mid}"}

    def replace_module_twin(
        self,
        id,
        mid,
        device_twin_info,
        if_match=None,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """Replaces tags and desired properties of a module twin.

        Replaces a module twin. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-device-twins
        for more information.

        :param id: Device ID.
        :type id: str
        :param mid: Module ID.
        :type mid: str
        :param device_twin_info: Device twin info
        :type device_twin_info: ~protocol.models.Twin
        :param if_match:
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Twin or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Twin or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.replace_module_twin.metadata["url"]
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
        body_content = self._serialize.body(device_twin_info, "Twin")

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("Twin", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    replace_module_twin.metadata = {"url": "/twins/{id}/modules/{mid}"}

    def update_module_twin(
        self,
        id,
        mid,
        device_twin_info,
        if_match=None,
        custom_headers=None,
        raw=False,
        **operation_config
    ):
        """Updates tags and desired properties of a module twin.

        Updates a module twin. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-device-twins
        for more information.

        :param id: Device ID.
        :type id: str
        :param mid: Module ID.
        :type mid: str
        :param device_twin_info: Device twin information
        :type device_twin_info: ~protocol.models.Twin
        :param if_match:
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Twin or ClientRawResponse if raw=true
        :rtype: ~protocol.models.Twin or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_module_twin.metadata["url"]
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
        body_content = self._serialize.body(device_twin_info, "Twin")

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize("Twin", response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    update_module_twin.metadata = {"url": "/twins/{id}/modules/{mid}"}
