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

class Exposure(object):
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
        'treatment': 'list[str]',
        'contamination': 'list[str]',
        'type': 'str',
        'scenario': 'list[str]',
        'uncertainty_estimation': 'str'
    }

    attribute_map = {
        'treatment': 'treatment',
        'contamination': 'contamination',
        'type': 'type',
        'scenario': 'scenario',
        'uncertainty_estimation': 'uncertaintyEstimation'
    }

    def __init__(self, treatment=None, contamination=None, type=None, scenario=None, uncertainty_estimation=None):  # noqa: E501
        """Exposure - a model defined in Swagger"""  # noqa: E501
        self._treatment = None
        self._contamination = None
        self._type = None
        self._scenario = None
        self._uncertainty_estimation = None
        self.discriminator = None
        if treatment is not None:
            self.treatment = treatment
        if contamination is not None:
            self.contamination = contamination
        self.type = type
        if scenario is not None:
            self.scenario = scenario
        if uncertainty_estimation is not None:
            self.uncertainty_estimation = uncertainty_estimation

    @property
    def treatment(self):
        """Gets the treatment of this Exposure.  # noqa: E501

        Description of the mathematical method to replace left-censored data (recommandation of WHO (2013), distribution or others)  # noqa: E501

        :return: The treatment of this Exposure.  # noqa: E501
        :rtype: list[str]
        """
        return self._treatment

    @treatment.setter
    def treatment(self, treatment):
        """Sets the treatment of this Exposure.

        Description of the mathematical method to replace left-censored data (recommandation of WHO (2013), distribution or others)  # noqa: E501

        :param treatment: The treatment of this Exposure.  # noqa: E501
        :type: list[str]
        """

        self._treatment = treatment

    @property
    def contamination(self):
        """Gets the contamination of this Exposure.  # noqa: E501

        Description of the range of of the level of contamination after left censored data treatment  # noqa: E501

        :return: The contamination of this Exposure.  # noqa: E501
        :rtype: list[str]
        """
        return self._contamination

    @contamination.setter
    def contamination(self, contamination):
        """Sets the contamination of this Exposure.

        Description of the range of of the level of contamination after left censored data treatment  # noqa: E501

        :param contamination: The contamination of this Exposure.  # noqa: E501
        :type: list[str]
        """

        self._contamination = contamination

    @property
    def type(self):
        """Gets the type of this Exposure.  # noqa: E501

        Description of the type of exposure  # noqa: E501

        :return: The type of this Exposure.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Exposure.

        Description of the type of exposure  # noqa: E501

        :param type: The type of this Exposure.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def scenario(self):
        """Gets the scenario of this Exposure.  # noqa: E501

        Description of the different scenarii used in exposure assessment  # noqa: E501

        :return: The scenario of this Exposure.  # noqa: E501
        :rtype: list[str]
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this Exposure.

        Description of the different scenarii used in exposure assessment  # noqa: E501

        :param scenario: The scenario of this Exposure.  # noqa: E501
        :type: list[str]
        """

        self._scenario = scenario

    @property
    def uncertainty_estimation(self):
        """Gets the uncertainty_estimation of this Exposure.  # noqa: E501

        Analysis to estimate uncertainty  # noqa: E501

        :return: The uncertainty_estimation of this Exposure.  # noqa: E501
        :rtype: str
        """
        return self._uncertainty_estimation

    @uncertainty_estimation.setter
    def uncertainty_estimation(self, uncertainty_estimation):
        """Sets the uncertainty_estimation of this Exposure.

        Analysis to estimate uncertainty  # noqa: E501

        :param uncertainty_estimation: The uncertainty_estimation of this Exposure.  # noqa: E501
        :type: str
        """

        self._uncertainty_estimation = uncertainty_estimation

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
        if issubclass(Exposure, dict):
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
        if not isinstance(other, Exposure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
