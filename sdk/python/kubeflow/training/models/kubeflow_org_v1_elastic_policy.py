# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.training.configuration import Configuration


class KubeflowOrgV1ElasticPolicy(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'max_replicas': 'int',
        'max_restarts': 'int',
        'metrics': 'list[K8sIoApiAutoscalingV2MetricSpec]',
        'min_replicas': 'int',
        'n_proc_per_node': 'int',
        'rdzv_backend': 'str',
        'rdzv_conf': 'list[KubeflowOrgV1RDZVConf]',
        'rdzv_host': 'str',
        'rdzv_id': 'str',
        'rdzv_port': 'int',
        'standalone': 'bool'
    }

    attribute_map = {
        'max_replicas': 'maxReplicas',
        'max_restarts': 'maxRestarts',
        'metrics': 'metrics',
        'min_replicas': 'minReplicas',
        'n_proc_per_node': 'nProcPerNode',
        'rdzv_backend': 'rdzvBackend',
        'rdzv_conf': 'rdzvConf',
        'rdzv_host': 'rdzvHost',
        'rdzv_id': 'rdzvId',
        'rdzv_port': 'rdzvPort',
        'standalone': 'standalone'
    }

    def __init__(self, max_replicas=None, max_restarts=None, metrics=None, min_replicas=None, n_proc_per_node=None, rdzv_backend=None, rdzv_conf=None, rdzv_host=None, rdzv_id=None, rdzv_port=None, standalone=None, local_vars_configuration=None):  # noqa: E501
        """KubeflowOrgV1ElasticPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_replicas = None
        self._max_restarts = None
        self._metrics = None
        self._min_replicas = None
        self._n_proc_per_node = None
        self._rdzv_backend = None
        self._rdzv_conf = None
        self._rdzv_host = None
        self._rdzv_id = None
        self._rdzv_port = None
        self._standalone = None
        self.discriminator = None

        if max_replicas is not None:
            self.max_replicas = max_replicas
        if max_restarts is not None:
            self.max_restarts = max_restarts
        if metrics is not None:
            self.metrics = metrics
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if n_proc_per_node is not None:
            self.n_proc_per_node = n_proc_per_node
        if rdzv_backend is not None:
            self.rdzv_backend = rdzv_backend
        if rdzv_conf is not None:
            self.rdzv_conf = rdzv_conf
        if rdzv_host is not None:
            self.rdzv_host = rdzv_host
        if rdzv_id is not None:
            self.rdzv_id = rdzv_id
        if rdzv_port is not None:
            self.rdzv_port = rdzv_port
        if standalone is not None:
            self.standalone = standalone

    @property
    def max_replicas(self):
        """Gets the max_replicas of this KubeflowOrgV1ElasticPolicy.  # noqa: E501

        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas, defaults to null.  # noqa: E501

        :return: The max_replicas of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """Sets the max_replicas of this KubeflowOrgV1ElasticPolicy.

        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas, defaults to null.  # noqa: E501

        :param max_replicas: The max_replicas of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: int
        """

        self._max_replicas = max_replicas

    @property
    def max_restarts(self):
        """Gets the max_restarts of this KubeflowOrgV1ElasticPolicy.  # noqa: E501


        :return: The max_restarts of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: int
        """
        return self._max_restarts

    @max_restarts.setter
    def max_restarts(self, max_restarts):
        """Sets the max_restarts of this KubeflowOrgV1ElasticPolicy.


        :param max_restarts: The max_restarts of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: int
        """

        self._max_restarts = max_restarts

    @property
    def metrics(self):
        """Gets the metrics of this KubeflowOrgV1ElasticPolicy.  # noqa: E501

        Metrics contains the specifications which are used to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated with multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the HPA will not be created.  # noqa: E501

        :return: The metrics of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: list[K8sIoApiAutoscalingV2MetricSpec]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this KubeflowOrgV1ElasticPolicy.

        Metrics contains the specifications which are used to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated with multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the HPA will not be created.  # noqa: E501

        :param metrics: The metrics of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: list[K8sIoApiAutoscalingV2MetricSpec]
        """

        self._metrics = metrics

    @property
    def min_replicas(self):
        """Gets the min_replicas of this KubeflowOrgV1ElasticPolicy.  # noqa: E501

        minReplicas is the lower limit for the number of replicas to which the training job can scale down.  It defaults to null.  # noqa: E501

        :return: The min_replicas of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this KubeflowOrgV1ElasticPolicy.

        minReplicas is the lower limit for the number of replicas to which the training job can scale down.  It defaults to null.  # noqa: E501

        :param min_replicas: The min_replicas of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def n_proc_per_node(self):
        """Gets the n_proc_per_node of this KubeflowOrgV1ElasticPolicy.  # noqa: E501

        Number of workers per node; supported values: [auto, cpu, gpu, int]. Deprecated: This API is deprecated in v1.7+ Use .spec.nprocPerNode instead.  # noqa: E501

        :return: The n_proc_per_node of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: int
        """
        return self._n_proc_per_node

    @n_proc_per_node.setter
    def n_proc_per_node(self, n_proc_per_node):
        """Sets the n_proc_per_node of this KubeflowOrgV1ElasticPolicy.

        Number of workers per node; supported values: [auto, cpu, gpu, int]. Deprecated: This API is deprecated in v1.7+ Use .spec.nprocPerNode instead.  # noqa: E501

        :param n_proc_per_node: The n_proc_per_node of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: int
        """

        self._n_proc_per_node = n_proc_per_node

    @property
    def rdzv_backend(self):
        """Gets the rdzv_backend of this KubeflowOrgV1ElasticPolicy.  # noqa: E501


        :return: The rdzv_backend of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: str
        """
        return self._rdzv_backend

    @rdzv_backend.setter
    def rdzv_backend(self, rdzv_backend):
        """Sets the rdzv_backend of this KubeflowOrgV1ElasticPolicy.


        :param rdzv_backend: The rdzv_backend of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: str
        """

        self._rdzv_backend = rdzv_backend

    @property
    def rdzv_conf(self):
        """Gets the rdzv_conf of this KubeflowOrgV1ElasticPolicy.  # noqa: E501

        RDZVConf contains additional rendezvous configuration (<key1>=<value1>,<key2>=<value2>,...).  # noqa: E501

        :return: The rdzv_conf of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: list[KubeflowOrgV1RDZVConf]
        """
        return self._rdzv_conf

    @rdzv_conf.setter
    def rdzv_conf(self, rdzv_conf):
        """Sets the rdzv_conf of this KubeflowOrgV1ElasticPolicy.

        RDZVConf contains additional rendezvous configuration (<key1>=<value1>,<key2>=<value2>,...).  # noqa: E501

        :param rdzv_conf: The rdzv_conf of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: list[KubeflowOrgV1RDZVConf]
        """

        self._rdzv_conf = rdzv_conf

    @property
    def rdzv_host(self):
        """Gets the rdzv_host of this KubeflowOrgV1ElasticPolicy.  # noqa: E501


        :return: The rdzv_host of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: str
        """
        return self._rdzv_host

    @rdzv_host.setter
    def rdzv_host(self, rdzv_host):
        """Sets the rdzv_host of this KubeflowOrgV1ElasticPolicy.


        :param rdzv_host: The rdzv_host of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: str
        """

        self._rdzv_host = rdzv_host

    @property
    def rdzv_id(self):
        """Gets the rdzv_id of this KubeflowOrgV1ElasticPolicy.  # noqa: E501


        :return: The rdzv_id of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: str
        """
        return self._rdzv_id

    @rdzv_id.setter
    def rdzv_id(self, rdzv_id):
        """Sets the rdzv_id of this KubeflowOrgV1ElasticPolicy.


        :param rdzv_id: The rdzv_id of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: str
        """

        self._rdzv_id = rdzv_id

    @property
    def rdzv_port(self):
        """Gets the rdzv_port of this KubeflowOrgV1ElasticPolicy.  # noqa: E501


        :return: The rdzv_port of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: int
        """
        return self._rdzv_port

    @rdzv_port.setter
    def rdzv_port(self, rdzv_port):
        """Sets the rdzv_port of this KubeflowOrgV1ElasticPolicy.


        :param rdzv_port: The rdzv_port of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: int
        """

        self._rdzv_port = rdzv_port

    @property
    def standalone(self):
        """Gets the standalone of this KubeflowOrgV1ElasticPolicy.  # noqa: E501

        Start a local standalone rendezvous backend that is represented by a C10d TCP store on port 29400. Useful when launching single-node, multi-worker job. If specified --rdzv_backend, --rdzv_endpoint, --rdzv_id are auto-assigned; any explicitly set values are ignored.  # noqa: E501

        :return: The standalone of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._standalone

    @standalone.setter
    def standalone(self, standalone):
        """Sets the standalone of this KubeflowOrgV1ElasticPolicy.

        Start a local standalone rendezvous backend that is represented by a C10d TCP store on port 29400. Useful when launching single-node, multi-worker job. If specified --rdzv_backend, --rdzv_endpoint, --rdzv_id are auto-assigned; any explicitly set values are ignored.  # noqa: E501

        :param standalone: The standalone of this KubeflowOrgV1ElasticPolicy.  # noqa: E501
        :type: bool
        """

        self._standalone = standalone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KubeflowOrgV1ElasticPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeflowOrgV1ElasticPolicy):
            return True

        return self.to_dict() != other.to_dict()
