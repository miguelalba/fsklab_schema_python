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

class GenericModelDataBackground(object):
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
        'study': 'Study',
        'study_sample': 'list[StudySample]',
        'dietary_assessment_method': 'list[DietaryAssessmentMethod]',
        'laboratory': 'list[Laboratory]',
        'assay': 'list[Assay]'
    }

    attribute_map = {
        'study': 'study',
        'study_sample': 'studySample',
        'dietary_assessment_method': 'dietaryAssessmentMethod',
        'laboratory': 'laboratory',
        'assay': 'assay'
    }

    def __init__(self, study=None, study_sample=None, dietary_assessment_method=None, laboratory=None, assay=None):  # noqa: E501
        """GenericModelDataBackground - a model defined in Swagger"""  # noqa: E501
        self._study = None
        self._study_sample = None
        self._dietary_assessment_method = None
        self._laboratory = None
        self._assay = None
        self.discriminator = None
        self.study = study
        if study_sample is not None:
            self.study_sample = study_sample
        if dietary_assessment_method is not None:
            self.dietary_assessment_method = dietary_assessment_method
        if laboratory is not None:
            self.laboratory = laboratory
        if assay is not None:
            self.assay = assay

    @property
    def study(self):
        """Gets the study of this GenericModelDataBackground.  # noqa: E501


        :return: The study of this GenericModelDataBackground.  # noqa: E501
        :rtype: Study
        """
        return self._study

    @study.setter
    def study(self, study):
        """Sets the study of this GenericModelDataBackground.


        :param study: The study of this GenericModelDataBackground.  # noqa: E501
        :type: Study
        """
        if study is None:
            raise ValueError("Invalid value for `study`, must not be `None`")  # noqa: E501

        self._study = study

    @property
    def study_sample(self):
        """Gets the study_sample of this GenericModelDataBackground.  # noqa: E501


        :return: The study_sample of this GenericModelDataBackground.  # noqa: E501
        :rtype: list[StudySample]
        """
        return self._study_sample

    @study_sample.setter
    def study_sample(self, study_sample):
        """Sets the study_sample of this GenericModelDataBackground.


        :param study_sample: The study_sample of this GenericModelDataBackground.  # noqa: E501
        :type: list[StudySample]
        """

        self._study_sample = study_sample

    @property
    def dietary_assessment_method(self):
        """Gets the dietary_assessment_method of this GenericModelDataBackground.  # noqa: E501


        :return: The dietary_assessment_method of this GenericModelDataBackground.  # noqa: E501
        :rtype: list[DietaryAssessmentMethod]
        """
        return self._dietary_assessment_method

    @dietary_assessment_method.setter
    def dietary_assessment_method(self, dietary_assessment_method):
        """Sets the dietary_assessment_method of this GenericModelDataBackground.


        :param dietary_assessment_method: The dietary_assessment_method of this GenericModelDataBackground.  # noqa: E501
        :type: list[DietaryAssessmentMethod]
        """

        self._dietary_assessment_method = dietary_assessment_method

    @property
    def laboratory(self):
        """Gets the laboratory of this GenericModelDataBackground.  # noqa: E501


        :return: The laboratory of this GenericModelDataBackground.  # noqa: E501
        :rtype: list[Laboratory]
        """
        return self._laboratory

    @laboratory.setter
    def laboratory(self, laboratory):
        """Sets the laboratory of this GenericModelDataBackground.


        :param laboratory: The laboratory of this GenericModelDataBackground.  # noqa: E501
        :type: list[Laboratory]
        """

        self._laboratory = laboratory

    @property
    def assay(self):
        """Gets the assay of this GenericModelDataBackground.  # noqa: E501


        :return: The assay of this GenericModelDataBackground.  # noqa: E501
        :rtype: list[Assay]
        """
        return self._assay

    @assay.setter
    def assay(self, assay):
        """Sets the assay of this GenericModelDataBackground.


        :param assay: The assay of this GenericModelDataBackground.  # noqa: E501
        :type: list[Assay]
        """

        self._assay = assay

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
        if issubclass(GenericModelDataBackground, dict):
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
        if not isinstance(other, GenericModelDataBackground):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other