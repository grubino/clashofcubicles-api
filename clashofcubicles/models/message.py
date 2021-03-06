# coding: utf-8

from __future__ import absolute_import
from clashofcubicles.models.message import Message
from clashofcubicles.models.task import Task
from clashofcubicles.models.worker import Worker
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Message(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, recipients=None, sender=None, text=None, attachments=None):
        """
        Message - a model defined in Swagger

        :param id: The id of this Message.
        :type id: int
        :param recipients: The recipients of this Message.
        :type recipients: List[Worker]
        :param sender: The sender of this Message.
        :type sender: Message
        :param text: The text of this Message.
        :type text: str
        :param attachments: The attachments of this Message.
        :type attachments: List[Task]
        """
        self.swagger_types = {
            'id': int,
            'recipients': List[Worker],
            'sender': Message,
            'text': str,
            'attachments': List[Task]
        }

        self.attribute_map = {
            'id': 'id',
            'recipients': 'recipients',
            'sender': 'sender',
            'text': 'text',
            'attachments': 'attachments'
        }

        self._id = id
        self._recipients = recipients
        self._sender = sender
        self._text = text
        self._attachments = attachments

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Message of this Message.
        :rtype: Message
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self):
        """
        Gets the id of this Message.

        :return: The id of this Message.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Message.

        :param id: The id of this Message.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def recipients(self):
        """
        Gets the recipients of this Message.

        :return: The recipients of this Message.
        :rtype: List[Worker]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this Message.

        :param recipients: The recipients of this Message.
        :type recipients: List[Worker]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")

        self._recipients = recipients

    @property
    def sender(self):
        """
        Gets the sender of this Message.

        :return: The sender of this Message.
        :rtype: Message
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this Message.

        :param sender: The sender of this Message.
        :type sender: Message
        """

        self._sender = sender

    @property
    def text(self):
        """
        Gets the text of this Message.

        :return: The text of this Message.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Message.

        :param text: The text of this Message.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

    @property
    def attachments(self):
        """
        Gets the attachments of this Message.

        :return: The attachments of this Message.
        :rtype: List[Task]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this Message.

        :param attachments: The attachments of this Message.
        :type attachments: List[Task]
        """

        self._attachments = attachments

