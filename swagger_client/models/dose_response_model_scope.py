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

class DoseResponseModelScope(object):
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
        'hazard': 'list[Hazard]',
        'population_group': 'list[PopulationGroup]',
        'general_comment': 'str',
        'temporal_information': 'str',
        'spatial_information': 'str'
    }

    attribute_map = {
        'hazard': 'hazard',
        'population_group': 'populationGroup',
        'general_comment': 'generalComment',
        'temporal_information': 'temporalInformation',
        'spatial_information': 'spatialInformation'
    }

    def __init__(self, hazard=None, population_group=None, general_comment=None, temporal_information=None, spatial_information=None):  # noqa: E501
        """DoseResponseModelScope - a model defined in Swagger"""  # noqa: E501
        self._hazard = None
        self._population_group = None
        self._general_comment = None
        self._temporal_information = None
        self._spatial_information = None
        self.discriminator = None
        self.hazard = hazard
        self.population_group = population_group
        if general_comment is not None:
            self.general_comment = general_comment
        if temporal_information is not None:
            self.temporal_information = temporal_information
        if spatial_information is not None:
            self.spatial_information = spatial_information

    @property
    def hazard(self):
        """Gets the hazard of this DoseResponseModelScope.  # noqa: E501


        :return: The hazard of this DoseResponseModelScope.  # noqa: E501
        :rtype: list[Hazard]
        """
        return self._hazard

    @hazard.setter
    def hazard(self, hazard):
        """Sets the hazard of this DoseResponseModelScope.


        :param hazard: The hazard of this DoseResponseModelScope.  # noqa: E501
        :type: list[Hazard]
        """
        if hazard is None:
            raise ValueError("Invalid value for `hazard`, must not be `None`")  # noqa: E501

        self._hazard = hazard

    @property
    def population_group(self):
        """Gets the population_group of this DoseResponseModelScope.  # noqa: E501


        :return: The population_group of this DoseResponseModelScope.  # noqa: E501
        :rtype: list[PopulationGroup]
        """
        return self._population_group

    @population_group.setter
    def population_group(self, population_group):
        """Sets the population_group of this DoseResponseModelScope.


        :param population_group: The population_group of this DoseResponseModelScope.  # noqa: E501
        :type: list[PopulationGroup]
        """
        if population_group is None:
            raise ValueError("Invalid value for `population_group`, must not be `None`")  # noqa: E501

        self._population_group = population_group

    @property
    def general_comment(self):
        """Gets the general_comment of this DoseResponseModelScope.  # noqa: E501


        :return: The general_comment of this DoseResponseModelScope.  # noqa: E501
        :rtype: str
        """
        return self._general_comment

    @general_comment.setter
    def general_comment(self, general_comment):
        """Sets the general_comment of this DoseResponseModelScope.


        :param general_comment: The general_comment of this DoseResponseModelScope.  # noqa: E501
        :type: str
        """

        self._general_comment = general_comment

    @property
    def temporal_information(self):
        """Gets the temporal_information of this DoseResponseModelScope.  # noqa: E501


        :return: The temporal_information of this DoseResponseModelScope.  # noqa: E501
        :rtype: str
        """
        return self._temporal_information

    @temporal_information.setter
    def temporal_information(self, temporal_information):
        """Sets the temporal_information of this DoseResponseModelScope.


        :param temporal_information: The temporal_information of this DoseResponseModelScope.  # noqa: E501
        :type: str
        """

        self._temporal_information = temporal_information

    @property
    def spatial_information(self):
        """Gets the spatial_information of this DoseResponseModelScope.  # noqa: E501


        :return: The spatial_information of this DoseResponseModelScope.  # noqa: E501
        :rtype: str
        """
        return self._spatial_information

    @spatial_information.setter
    def spatial_information(self, spatial_information):
        """Sets the spatial_information of this DoseResponseModelScope.


        :param spatial_information: The spatial_information of this DoseResponseModelScope.  # noqa: E501
        :type: str
        """

        self._spatial_information = spatial_information

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
        if issubclass(DoseResponseModelScope, dict):
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
        if not isinstance(other, DoseResponseModelScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
