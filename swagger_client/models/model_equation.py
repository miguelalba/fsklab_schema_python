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

class ModelEquation(object):
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
        'name': 'str',
        'model_equation_class': 'str',
        'reference': 'list[Reference]',
        'model_equation': 'str',
        'model_hypothesis': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'model_equation_class': 'modelEquationClass',
        'reference': 'reference',
        'model_equation': 'modelEquation',
        'model_hypothesis': 'modelHypothesis'
    }

    def __init__(self, name=None, model_equation_class=None, reference=None, model_equation=None, model_hypothesis=None):  # noqa: E501
        """ModelEquation - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._model_equation_class = None
        self._reference = None
        self._model_equation = None
        self._model_hypothesis = None
        self.discriminator = None
        self.name = name
        if model_equation_class is not None:
            self.model_equation_class = model_equation_class
        if reference is not None:
            self.reference = reference
        self.model_equation = model_equation
        if model_hypothesis is not None:
            self.model_hypothesis = model_hypothesis

    @property
    def name(self):
        """Gets the name of this ModelEquation.  # noqa: E501

        A name given to the model equation  # noqa: E501

        :return: The name of this ModelEquation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelEquation.

        A name given to the model equation  # noqa: E501

        :param name: The name of this ModelEquation.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def model_equation_class(self):
        """Gets the model_equation_class of this ModelEquation.  # noqa: E501

        Information on that helps to categorize model equations  # noqa: E501

        :return: The model_equation_class of this ModelEquation.  # noqa: E501
        :rtype: str
        """
        return self._model_equation_class

    @model_equation_class.setter
    def model_equation_class(self, model_equation_class):
        """Sets the model_equation_class of this ModelEquation.

        Information on that helps to categorize model equations  # noqa: E501

        :param model_equation_class: The model_equation_class of this ModelEquation.  # noqa: E501
        :type: str
        """

        self._model_equation_class = model_equation_class

    @property
    def reference(self):
        """Gets the reference of this ModelEquation.  # noqa: E501


        :return: The reference of this ModelEquation.  # noqa: E501
        :rtype: list[Reference]
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ModelEquation.


        :param reference: The reference of this ModelEquation.  # noqa: E501
        :type: list[Reference]
        """

        self._reference = reference

    @property
    def model_equation(self):
        """Gets the model_equation of this ModelEquation.  # noqa: E501

        The pointer to the file that holds the software code (e.g. R-script)  # noqa: E501

        :return: The model_equation of this ModelEquation.  # noqa: E501
        :rtype: str
        """
        return self._model_equation

    @model_equation.setter
    def model_equation(self, model_equation):
        """Sets the model_equation of this ModelEquation.

        The pointer to the file that holds the software code (e.g. R-script)  # noqa: E501

        :param model_equation: The model_equation of this ModelEquation.  # noqa: E501
        :type: str
        """
        if model_equation is None:
            raise ValueError("Invalid value for `model_equation`, must not be `None`")  # noqa: E501

        self._model_equation = model_equation

    @property
    def model_hypothesis(self):
        """Gets the model_hypothesis of this ModelEquation.  # noqa: E501


        :return: The model_hypothesis of this ModelEquation.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_hypothesis

    @model_hypothesis.setter
    def model_hypothesis(self, model_hypothesis):
        """Sets the model_hypothesis of this ModelEquation.


        :param model_hypothesis: The model_hypothesis of this ModelEquation.  # noqa: E501
        :type: list[str]
        """

        self._model_hypothesis = model_hypothesis

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
        if issubclass(ModelEquation, dict):
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
        if not isinstance(other, ModelEquation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
