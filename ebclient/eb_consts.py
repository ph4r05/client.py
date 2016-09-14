import logging

__author__ = 'dusanklinec'


logger = logging.getLogger(__name__)


class UOTypes(object):
    """
    UO types constants
    """

    HMAC = 0x1
    SCRAMBLE = 0x2
    ENSCRAMBLE = 0x3
    PLAINAES = 0x4
    RSA1024DECRYPT_NOPAD = 0x5
    RSA2048DECRYPT_NOPAD = 0x6
    EC_FP192SIGN = 0x7
    AUTH_HOTP = 0x8
    AUTH_NEW_USER_CTX = 0x9
    AUTH_PASSWORD = 0xa
    AUTH_UPDATE_USER_CTX = 0xb
    TOKENIZE = 0xc
    DETOKENIZE = 0xd
    TOKENIZEWRAP = 0xe
    PLAINAESDECRYPT = 0xf
    RANDOMDATA = 0x10
    CREATENEWUO = 0x11
    RSA1024ENCRYPT_NOPAD = 0x12
    RSA2048ENCRYPT_NOPAD = 0x13


class EBConsts(object):
    """
    Constants
    """
    INVALID_KEY_HANDLE = -1
    INVALID_KEY_TYPE = -1
    FRESHNESS_NONCE_LEN = 8

    STATUS_OK = 0x9000

    METHOD_REST = 'REST'
    METHOD_SOCKET = 'SOCKET'

    HTTP_METHOD_GET = 'GET'
    HTTP_METHOD_POST = 'POST'

    REQUEST_TYPES = {
        UOTypes.HMAC: 'HMAC',
        UOTypes.SCRAMBLE: 'SCRAMBLE',
        UOTypes.ENSCRAMBLE: 'ENSCRAMBLE',
        UOTypes.PLAINAES: 'PLAINAES',
        UOTypes.RSA1024DECRYPT_NOPAD: 'RSA1024DECRYPT_NOPAD',
        UOTypes.RSA2048DECRYPT_NOPAD: 'RSA2048DECRYPT_NOPAD',
        UOTypes.EC_FP192SIGN: 'EC_FP192SIGN',
        UOTypes.AUTH_HOTP: 'AUTH_HOTP',
        UOTypes.AUTH_NEW_USER_CTX: 'AUTH_NEW_USER_CTX',
        UOTypes.AUTH_PASSWORD: 'AUTH_PASSWORD',
        UOTypes.AUTH_UPDATE_USER_CTX: 'AUTH_UPDATE_USER_CTX',
        UOTypes.TOKENIZE: 'TOKENIZE',
        UOTypes.DETOKENIZE: 'DETOKENIZE',
        UOTypes.TOKENIZEWRAP: 'TOKENIZEWRAP',
        UOTypes.PLAINAESDECRYPT: 'PLAINAESDECRYPT',
        UOTypes.RANDOMDATA: 'RANDOMDATA',
        UOTypes.CREATENEWUO: 'CREATENEWUO',
        UOTypes.RSA1024ENCRYPT_NOPAD: 'RSA1024ENCRYPT_NOPAD',
        UOTypes.RSA2048ENCRYPT_NOPAD: 'RSA2048ENCRYPT_NOPAD'
    }



