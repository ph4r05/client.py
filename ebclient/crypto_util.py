__author__ = 'dusanklinec'
"""
Provides basic cryptographic utilities for the Python EnigmaBridge client, e.g.,
generating random numbers, encryption, decryption, padding, etc...

For now we use PyCrypto, later we may use pure python implementations to minimize dependency count.
"""

import abc
import logging
import os
import base64

from Crypto import Random
from Crypto.Cipher import AES

# Logging if needed
logger = logging.getLogger(__name__)

#
# Utils
#


def toBytes(x):
    """
    Converts input to a byte string.
    Typically used in PyCrypto as an argument (e.g., key, iv)

    :param x: string (does nothing), bytearray, array with numbers
    :return:
    """
    if isinstance(x, bytearray):
        return x.decode('ascii')
    elif isinstance(x, basestring):
        return x
    elif isinstance(x, (list, tuple)):
        return bytearray(x).decode('ascii')
    else:
        raise ValueError('Unknown input argument type')


def toByteArr(x):
    """
    Converts input to byte array.
    If already a byte array, return directly.

    :param x:
    :return:
    """
    if isinstance(x, bytearray):
        return x
    else:
        return bytearray(x)


def toHex(x):
    """
    Converts input to the hex string
    :param x:
    :return:
    """
    if isinstance(x, bytearray):
        return x.decode('hex')
    elif isinstance(x, basestring):
        return base64.b16encode(x)
    elif isinstance(x, (list, tuple)):
        return bytearray(x).decode('hex')
    else:
        raise ValueError('Unknown input argument type')


def getZeroVector(numBytes):
    """
    Generates a zero vector of a given size

    :param numBytes:
    :return:
    """
    return bytearray([0] * numBytes).decode('ascii')

#
# Randomness
#


def getRandomVector(numBytes):
    #return Random.get_random_bytes(numBytes)
    return os.urandom(numBytes)

#
# Padding
#


class Padding(object):
    """
    Basic Padding methods
    """
    @abc.abstractmethod
    def pad(self, data, *args, **kwargs):  # pragma: no cover
        """Pads data with given padding.

        :returns: Padded data.
        :rtype: list

        """
        raise NotImplementedError()

    def unpad(self, data, *args, **kwargs):  # pragma: no cover
        """UnPads data with given padding.

        :returns: unpaded data
        :rtype: list

        """
        raise NotImplementedError()


class PKCS7(Padding):
    def unpad(self, data, *args, **kwargs):
        return data[:-ord(data[len(data)-1:])]

    def pad(self, data, *args, **kwargs):
        bs = kwargs.get('bs', 16)
        return data + (bs - len(data) % bs) * chr(bs - len(data) % bs)


class PKCS15(Padding):
    def unpad(self, data, *args, **kwargs):
        #TODO: implement
        pass

    def pad(self, data, *args, **kwargs):
        #TODO: implement
        pass


#
# Encryption
#





