# coding: utf-8

"""
    RAKIP Generic model

    TODO  # noqa: E501

    OpenAPI spec version: 1.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Study(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identifier': 'str',
        'title': 'str',
        'description': 'str',
        'design_type': 'str',
        'assay_measurement_type': 'str',
        'assay_technology_type': 'str',
        'assay_technology_platform': 'str',
        'accreditation_procedure_for_the_assay_technology': 'str',
        'protocol_name': 'str',
        'protocol_type': 'str',
        'protocol_description': 'str',
        'protocol_uri': 'str',
        'protocol_version': 'str',
        'protocol_parameters_name': 'str',
        'protocol_components_name': 'str',
        'protocol_components_type': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'title': 'title',
        'description': 'description',
        'design_type': 'designType',
        'assay_measurement_type': 'assayMeasurementType',
        'assay_technology_type': 'assayTechnologyType',
        'assay_technology_platform': 'assayTechnologyPlatform',
        'accreditation_procedure_for_the_assay_technology': 'accreditationProcedureForTheAssayTechnology',
        'protocol_name': 'protocolName',
        'protocol_type': 'protocolType',
        'protocol_description': 'protocolDescription',
        'protocol_uri': 'protocolURI',
        'protocol_version': 'protocolVersion',
        'protocol_parameters_name': 'protocolParametersName',
        'protocol_components_name': 'protocolComponentsName',
        'protocol_components_type': 'protocolComponentsType'
    }

    def __init__(self, identifier=None, title=None, description=None, design_type=None, assay_measurement_type=None, assay_technology_type=None, assay_technology_platform=None, accreditation_procedure_for_the_assay_technology=None, protocol_name=None, protocol_type=None, protocol_description=None, protocol_uri=None, protocol_version=None, protocol_parameters_name=None, protocol_components_name=None, protocol_components_type=None):  # noqa: E501
        """Study - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._title = None
        self._description = None
        self._design_type = None
        self._assay_measurement_type = None
        self._assay_technology_type = None
        self._assay_technology_platform = None
        self._accreditation_procedure_for_the_assay_technology = None
        self._protocol_name = None
        self._protocol_type = None
        self._protocol_description = None
        self._protocol_uri = None
        self._protocol_version = None
        self._protocol_parameters_name = None
        self._protocol_components_name = None
        self._protocol_components_type = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        self.title = title
        if description is not None:
            self.description = description
        if design_type is not None:
            self.design_type = design_type
        if assay_measurement_type is not None:
            self.assay_measurement_type = assay_measurement_type
        if assay_technology_type is not None:
            self.assay_technology_type = assay_technology_type
        if assay_technology_platform is not None:
            self.assay_technology_platform = assay_technology_platform
        if accreditation_procedure_for_the_assay_technology is not None:
            self.accreditation_procedure_for_the_assay_technology = accreditation_procedure_for_the_assay_technology
        if protocol_name is not None:
            self.protocol_name = protocol_name
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if protocol_description is not None:
            self.protocol_description = protocol_description
        if protocol_uri is not None:
            self.protocol_uri = protocol_uri
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if protocol_parameters_name is not None:
            self.protocol_parameters_name = protocol_parameters_name
        if protocol_components_name is not None:
            self.protocol_components_name = protocol_components_name
        if protocol_components_type is not None:
            self.protocol_components_type = protocol_components_type

    @property
    def identifier(self):
        """Gets the identifier of this Study.  # noqa: E501

        A user defined identifier for the study  # noqa: E501

        :return: The identifier of this Study.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Study.

        A user defined identifier for the study  # noqa: E501

        :param identifier: The identifier of this Study.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def title(self):
        """Gets the title of this Study.  # noqa: E501

        A title for the Study  # noqa: E501

        :return: The title of this Study.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Study.

        A title for the Study  # noqa: E501

        :param title: The title of this Study.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Study.  # noqa: E501

        A brief description of the study aims  # noqa: E501

        :return: The description of this Study.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Study.

        A brief description of the study aims  # noqa: E501

        :param description: The description of this Study.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def design_type(self):
        """Gets the design_type of this Study.  # noqa: E501

        The type of study design being employed  # noqa: E501

        :return: The design_type of this Study.  # noqa: E501
        :rtype: str
        """
        return self._design_type

    @design_type.setter
    def design_type(self, design_type):
        """Sets the design_type of this Study.

        The type of study design being employed  # noqa: E501

        :param design_type: The design_type of this Study.  # noqa: E501
        :type: str
        """

        self._design_type = design_type

    @property
    def assay_measurement_type(self):
        """Gets the assay_measurement_type of this Study.  # noqa: E501

        The measurement being observed in this assay  # noqa: E501

        :return: The assay_measurement_type of this Study.  # noqa: E501
        :rtype: str
        """
        return self._assay_measurement_type

    @assay_measurement_type.setter
    def assay_measurement_type(self, assay_measurement_type):
        """Sets the assay_measurement_type of this Study.

        The measurement being observed in this assay  # noqa: E501

        :param assay_measurement_type: The assay_measurement_type of this Study.  # noqa: E501
        :type: str
        """

        self._assay_measurement_type = assay_measurement_type

    @property
    def assay_technology_type(self):
        """Gets the assay_technology_type of this Study.  # noqa: E501

        The technology being employed to observe this measurement  # noqa: E501

        :return: The assay_technology_type of this Study.  # noqa: E501
        :rtype: str
        """
        return self._assay_technology_type

    @assay_technology_type.setter
    def assay_technology_type(self, assay_technology_type):
        """Sets the assay_technology_type of this Study.

        The technology being employed to observe this measurement  # noqa: E501

        :param assay_technology_type: The assay_technology_type of this Study.  # noqa: E501
        :type: str
        """

        self._assay_technology_type = assay_technology_type

    @property
    def assay_technology_platform(self):
        """Gets the assay_technology_platform of this Study.  # noqa: E501

        The technology platform used  # noqa: E501

        :return: The assay_technology_platform of this Study.  # noqa: E501
        :rtype: str
        """
        return self._assay_technology_platform

    @assay_technology_platform.setter
    def assay_technology_platform(self, assay_technology_platform):
        """Sets the assay_technology_platform of this Study.

        The technology platform used  # noqa: E501

        :param assay_technology_platform: The assay_technology_platform of this Study.  # noqa: E501
        :type: str
        """

        self._assay_technology_platform = assay_technology_platform

    @property
    def accreditation_procedure_for_the_assay_technology(self):
        """Gets the accreditation_procedure_for_the_assay_technology of this Study.  # noqa: E501

        Accreditation procedure for the analytical method used  # noqa: E501

        :return: The accreditation_procedure_for_the_assay_technology of this Study.  # noqa: E501
        :rtype: str
        """
        return self._accreditation_procedure_for_the_assay_technology

    @accreditation_procedure_for_the_assay_technology.setter
    def accreditation_procedure_for_the_assay_technology(self, accreditation_procedure_for_the_assay_technology):
        """Sets the accreditation_procedure_for_the_assay_technology of this Study.

        Accreditation procedure for the analytical method used  # noqa: E501

        :param accreditation_procedure_for_the_assay_technology: The accreditation_procedure_for_the_assay_technology of this Study.  # noqa: E501
        :type: str
        """

        self._accreditation_procedure_for_the_assay_technology = accreditation_procedure_for_the_assay_technology

    @property
    def protocol_name(self):
        """Gets the protocol_name of this Study.  # noqa: E501

        The name of the protocol, e.g.Extraction Protocol  # noqa: E501

        :return: The protocol_name of this Study.  # noqa: E501
        :rtype: str
        """
        return self._protocol_name

    @protocol_name.setter
    def protocol_name(self, protocol_name):
        """Sets the protocol_name of this Study.

        The name of the protocol, e.g.Extraction Protocol  # noqa: E501

        :param protocol_name: The protocol_name of this Study.  # noqa: E501
        :type: str
        """

        self._protocol_name = protocol_name

    @property
    def protocol_type(self):
        """Gets the protocol_type of this Study.  # noqa: E501

        The type of the protocol, preferably coming from an Ontology, e.g. Extraction Protocol  # noqa: E501

        :return: The protocol_type of this Study.  # noqa: E501
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this Study.

        The type of the protocol, preferably coming from an Ontology, e.g. Extraction Protocol  # noqa: E501

        :param protocol_type: The protocol_type of this Study.  # noqa: E501
        :type: str
        """

        self._protocol_type = protocol_type

    @property
    def protocol_description(self):
        """Gets the protocol_description of this Study.  # noqa: E501

        A description of the Protocol  # noqa: E501

        :return: The protocol_description of this Study.  # noqa: E501
        :rtype: str
        """
        return self._protocol_description

    @protocol_description.setter
    def protocol_description(self, protocol_description):
        """Sets the protocol_description of this Study.

        A description of the Protocol  # noqa: E501

        :param protocol_description: The protocol_description of this Study.  # noqa: E501
        :type: str
        """

        self._protocol_description = protocol_description

    @property
    def protocol_uri(self):
        """Gets the protocol_uri of this Study.  # noqa: E501

        A URI to link out to a publication, web page, etc. describing the protocol.  # noqa: E501

        :return: The protocol_uri of this Study.  # noqa: E501
        :rtype: str
        """
        return self._protocol_uri

    @protocol_uri.setter
    def protocol_uri(self, protocol_uri):
        """Sets the protocol_uri of this Study.

        A URI to link out to a publication, web page, etc. describing the protocol.  # noqa: E501

        :param protocol_uri: The protocol_uri of this Study.  # noqa: E501
        :type: str
        """

        self._protocol_uri = protocol_uri

    @property
    def protocol_version(self):
        """Gets the protocol_version of this Study.  # noqa: E501

        The version of the protocol used, where applicable  # noqa: E501

        :return: The protocol_version of this Study.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this Study.

        The version of the protocol used, where applicable  # noqa: E501

        :param protocol_version: The protocol_version of this Study.  # noqa: E501
        :type: str
        """

        self._protocol_version = protocol_version

    @property
    def protocol_parameters_name(self):
        """Gets the protocol_parameters_name of this Study.  # noqa: E501

        The parameters used when executing this protocol  # noqa: E501

        :return: The protocol_parameters_name of this Study.  # noqa: E501
        :rtype: str
        """
        return self._protocol_parameters_name

    @protocol_parameters_name.setter
    def protocol_parameters_name(self, protocol_parameters_name):
        """Sets the protocol_parameters_name of this Study.

        The parameters used when executing this protocol  # noqa: E501

        :param protocol_parameters_name: The protocol_parameters_name of this Study.  # noqa: E501
        :type: str
        """

        self._protocol_parameters_name = protocol_parameters_name

    @property
    def protocol_components_name(self):
        """Gets the protocol_components_name of this Study.  # noqa: E501

        The components used when carrying out this protocol  # noqa: E501

        :return: The protocol_components_name of this Study.  # noqa: E501
        :rtype: str
        """
        return self._protocol_components_name

    @protocol_components_name.setter
    def protocol_components_name(self, protocol_components_name):
        """Sets the protocol_components_name of this Study.

        The components used when carrying out this protocol  # noqa: E501

        :param protocol_components_name: The protocol_components_name of this Study.  # noqa: E501
        :type: str
        """

        self._protocol_components_name = protocol_components_name

    @property
    def protocol_components_type(self):
        """Gets the protocol_components_type of this Study.  # noqa: E501

        Description  # noqa: E501

        :return: The protocol_components_type of this Study.  # noqa: E501
        :rtype: str
        """
        return self._protocol_components_type

    @protocol_components_type.setter
    def protocol_components_type(self, protocol_components_type):
        """Sets the protocol_components_type of this Study.

        Description  # noqa: E501

        :param protocol_components_type: The protocol_components_type of this Study.  # noqa: E501
        :type: str
        """

        self._protocol_components_type = protocol_components_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Study, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Study):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
