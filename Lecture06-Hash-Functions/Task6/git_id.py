import hashlib

# What Git prints for this file (run on 2026-11-17 with Git 2.43):  git hash-object recipe.txt
GIT_SAYS = "e2fcdc71d93339fed5fc9b69eecf7c2b4712665c"

content = open("recipe.txt", "rb").read()

# TODO 1: the header that Git puts in front of the content: b"blob " + the length in decimal + one zero byte
#         str(len(content)).encode() turns the length into ASCII digits (like sprintf(buf, "%d", n) in C);
#         b"\0" is the zero byte that ends a C string
header = None

# TODO 2: the object id: the SHA-1 of header + content, as 40 hex digits: hashlib.sha1(...).hexdigest()
object_id = None

# TODO 3: Mallory changes "2 eggs" into "3 eggs": changed = content.replace(b"2 eggs", b"3 eggs")
#         compute the object id of changed in the same way (TODO 1 and TODO 2)
changed_id = None

# The printing is ready.
if header is None:
    print("not done yet: TODO 1")
else:
    print("header:", header, "(" + str(len(header)) + " bytes)")
if object_id is None:
    print("not done yet: TODO 2")
else:
    print("my object id: ", object_id)
    print("git says:     ", GIT_SAYS)
    print("the same:", object_id == GIT_SAYS)
if changed_id is None:
    print("not done yet: TODO 3")
else:
    print("after Mallory:", changed_id)
