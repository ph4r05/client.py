"""
Constants
"""

from ebclient.eb_consts import UOTypes


INVALID_KEY_HANDLE = -1
INVALID_KEY_TYPE = -1
FRESHNESS_NONCE_LEN = 8

STATUS_OK = 0x9000

METHOD_REST = 'REST'
METHOD_SOCKET = 'SOCKET'

HTTP_METHOD_GET = 'GET'
HTTP_METHOD_POST = 'POST'

REQUEST_PROCESS_DATA = 'ProcessData'
REQUEST_GET_AUTH = 'getauth'
REQUEST_INIT_AUTH = 'initauth'
REQUEST_CREATE = 'create'
REQUEST_ADD_API = 'addapi'
REQUEST_SHOW_API = 'showapi'
REQUEST_LIST_OPERATIONS = 'listops'
REQUEST_ENROL_DOMAIN = 'enroldomain'
REQUEST_GET_DOMAIN_CHALLENGE = 'getdomainchallenge'
REQUEST_UPDATE_DOMAIN = 'updatedomain'
REQUEST_INSTALL_STATUS = 'installstatus'
REQUEST_UNLOCK_DOMAIN = 'unlockdomain'

COMM_ENC_KEY_LENGTH = 32
COMM_MAC_KEY_LENGTH = 32

TPL_ENC_KEY_LENGTH = 32
TPL_MAC_KEY_LENGTH = 32

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
