import hashlib
import time

NAMES = ["md5", "sha1", "sha256", "sha512", "sha3_256"]
DATA = bytes(50 * 1000 * 1000)     # 50 MB of zero bytes (the speed does not depend on the content)

# TODO 1: for every name in NAMES: h = hashlib.new(name) makes an empty hash object of that kind;
#         h.digest_size is the size of its digest in bytes.
#         print("%-8s %4d bits" % (name, 8 * h.digest_size))
print("not done yet: TODO 1")

# TODO 2: predict first: which one is the fastest, which the slowest?
#         Then for every name: t0 = time.perf_counter(); hashlib.new(name, DATA).digest();
#         seconds = time.perf_counter() - t0; speed in MB/s = 50 / seconds
#         print("%-8s %7.0f MB/s" % (name, 50 / seconds))
print("not done yet: TODO 2")
