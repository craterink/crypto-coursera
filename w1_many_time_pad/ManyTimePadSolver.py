from UnknownPTW1 import UnknownPTW1
from util.mesh_map import mesh_map


class ManyTimePadSolver:

    # key
    _key_size = 0
    _key_guess = 1

    # (cipher, msg)
    _cipher_msg_guesses = None

    def __init__(self, ciphers):
        # TODO: key size??
        self._cipher_msgs = [(cipher, UnknownPTW1(cipher)) for cipher in ciphers]

    def ascii_analyze(self):
        cipher_msg_mesh = mesh_map(self._analyze_cipher_duo, self._cipher_msgs)
        pass

    def _analyze_cipher_duo(self, ((ciph1, unk_msg1),(ciph2, unk_msg2))):
        xor = ciph1 ^ ciph2
        return xor

    def guess_msg(self, cipher):
        return self._key_guess ^ cipher;