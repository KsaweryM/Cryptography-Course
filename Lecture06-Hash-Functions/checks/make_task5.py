"""Makes the files of Task 5 (run from Lecture06-Hash-Functions/checks: python3 make_task5.py).
The file is 200 000 deterministic bytes, so running this again gives the same files and digests."""
import hashlib
import os

NAME = "editor-2.4.1-installer.bin"
SIZE = 200000
T5 = os.path.join("..", "Task5")

data = bytearray()
counter = 0
while len(data) < SIZE:
    data += hashlib.sha256(b"editor 2.4.1 " + counter.to_bytes(8, "big")).digest()
    counter += 1
data = bytes(data[:SIZE])

changed = bytearray(data)          # mirror-b: one byte changed (a broken copy, or Mallory)
changed[123456] ^= 0x20
mallory = bytearray(data)          # mirror-c: Mallory's version, with its own SHA256SUMS
mallory[1000:1016] = b"MALLORY WAS HERE"


def line(content):
    return hashlib.sha256(content).hexdigest() + "  " + NAME + "\n"


def write(folder, content, sums):
    os.makedirs(os.path.join(T5, folder), exist_ok=True)
    if content is not None:
        with open(os.path.join(T5, folder, NAME), "wb") as f:
            f.write(content)
    with open(os.path.join(T5, folder, "SHA256SUMS"), "w") as f:
        f.write(sums)


write("website", None, line(data))
write("mirror-a", data, line(data))
write("mirror-b", bytes(changed), line(data))
write("mirror-c", bytes(mallory), line(bytes(mallory)))
print("website:", line(data), end="")
print("mirror-b file:", line(bytes(changed)), end="")
print("mirror-c file and its SHA256SUMS:", line(bytes(mallory)), end="")
