# Checks the pure-Python bcrypt (bcrypt_ready.py of Task 7 and Task 8) against published vectors.
# Source of the vectors: pyca/bcrypt, tests/test_bcrypt.py (https://github.com/pyca/bcrypt), copied 2026-11-17.
# Also compares random passwords and salts with the bcrypt of the system C library (libxcrypt, via crypt).
# Run: python3 checks/check_bcrypt.py  (from Lecture7/)
import os
import sys
import time
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", sys.argv[1] if len(sys.argv) > 1 else "Task7"))
import bcrypt_ready as B

VECTORS = [
    (b"Kk4DQuMMfZL9o", "$2b$04$cVWp4XaNU8a4v1uMRum2SO026BWLIoQMD/TXg5uZV.0P.uO8m3YEm"),
    (b"9IeRXmnGxMYbs", "$2b$04$pQ7gRO7e6wx/936oXhNjrOUNOHL1D0h1N2IDbJZYs.1ppzSof6SPy"),
    (b"xVQVbwa1S0M8r", "$2b$04$SQe9knOzepOVKoYXo9xTteNYr6MBwVz4tpriJVe3PNgYufGIsgKcW"),
    (b"Zfgr26LWd22Za", "$2b$04$eH8zX.q5Q.j2hO1NkVYJQOM6KxntS/ow3.YzVmFrE4t//CoF4fvne"),
    (b"Tg4daC27epFBE", "$2b$04$ahiTdwRXpUG2JLRcIznxc.s1.ydaPGD372bsGs8NqyYjLY1inG5n2"),
    (b"xhQPMmwh5ALzW", "$2b$04$nQn78dV0hGHf5wUBe0zOFu8n07ZbWWOKoGasZKRspZxtt.vBRNMIy"),
    (b"59je8h5Gj71tg", "$2b$04$cvXudZ5ugTg95W.rOjMITuM1jC0piCl3zF5cmGhzCibHZrNHkmckG"),
    (b"wT4fHJa2N9WSW", "$2b$04$YYjtiq4Uh88yUsExO0RNTuEJ.tZlsONac16A8OcLHleWFjVawfGvO"),
    (b"uSgFRnQdOgm4S", "$2b$04$WLTjgY/pZSyqX/fbMbJzf.qxCeTMQOzgL.CimRjMHtMxd/VGKojMu"),
    (b"tEPtJZXur16Vg", "$2b$04$2moPs/x/wnCfeQ5pCheMcuSJQ/KYjOZG780UjA/SiR.KsYWNrC7SG"),
    (b"vvho8C6nlVf9K", "$2b$04$HrEYC/AQ2HS77G78cQDZQ.r44WGcruKw03KHlnp71yVQEwpsi3xl2"),
    (b"5auCCY9by0Ruf", "$2b$04$vVYgSTfB8KVbmhbZE/k3R.ux9A0lJUM4CZwCkHI9fifke2.rTF7MG"),
    (b"GtTkR6qn2QOZW", "$2b$04$JfoNrR8.doieoI8..F.C1OQgwE3uTeuardy6lw0AjALUzOARoyf2m"),
    (b"zKo8vdFSnjX0f", "$2b$04$HP3I0PUs7KBEzMBNFw7o3O7f/uxaZU7aaDot1quHMgB2yrwBXsgyy"),
    (b"I9VfYlacJiwiK", "$2b$04$xnFVhJsTzsFBTeP3PpgbMeMREb6rdKV9faW54Sx.yg9plf4jY8qT6"),
    (b"VFPO7YXnHQbQO", "$2b$04$WQp9.igoLqVr6Qk70mz6xuRxE0RttVXXdukpR9N54x17ecad34ZF6"),
    (b"VDx5BdxfxstYk", "$2b$04$xgZtlonpAHSU/njOCdKztOPuPFzCNVpB4LGicO4/OGgHv.uKHkwsS"),
    (b"dEe6XfVGrrfSH", "$2b$04$2Siw3Nv3Q/gTOIPetAyPr.GNj3aO0lb1E5E9UumYGKjP9BYqlNWJe"),
    (b"cTT0EAFdwJiLn", "$2b$04$7/Qj7Kd8BcSahPO4khB8me4ssDJCW3r4OGYqPF87jxtrSyPj5cS5m"),
    (b"J8eHUDuxBB520", "$2b$04$VvlCUKbTMjaxaYJ.k5juoecpG/7IzcH1AkmqKi.lIZMVIOLClWAk."),
    (b"U*U", "$2a$05$CCCCCCCCCCCCCCCCCCCCC.E5YPO9kmyuRGyh0XouQYb4YMJKvyOeW"),
    (b"U*U*", "$2a$05$CCCCCCCCCCCCCCCCCCCCC.VGOzA784oUp/Z0DY336zx7pLYAy0lwK"),
    (b"U*U*U", "$2a$05$XXXXXXXXXXXXXXXXXXXXXOAcXxm9kjPGEMsLznoKqmqw7tc8WCx4a"),
    (b"\xa3", "$2a$05$/OK.fbVrR/bpIqNJ5ianF.Sa7shbm4.OzKpvFnX1pQLmQW96oUlCq"),
    (b"}>\xb3\xfe\xf1\x8b\xa0\xe6(\xa2Lzq\xc3P\x7f\xcc\xc8b{\xf9\x14\xf6"
     b"\xf6`\x81G5\xec\x1d\x87\x10\xbf\xa7\xe1}I7 \x96\xdfc\xf2\xbf\xb3Vh"
     b"\xdfM\x88q\xf7\xff\x1b\x82~z\x13\xdd\xe9\x84\x00\xdd4",
     "$2b$10$keO.ZZs22YtygVF6BLfhGOI/JjshJYPp8DZsUtym6mJV2Eha2Hdd."),
    (b"g7\r\x01\xf3\xd4\xd0\xa9JB^\x18\x007P\xb2N\xc7\x1c\xee\x87&\x83C"
     b"\x8b\xe8\x18\xc5>\x86\x14/\xd6\xcc\x1cJ\xde\xd7ix\xeb\xdeO\xef"
     b"\xe1i\xac\xcb\x03\x96v1' \xd6@.m\xa5!\xa0\xef\xc0(",
     "$2a$04$tecY.9ylRInW/rAAzXCXPOOlyYeCNzmNTzPDNSIFztFMKbvs/s5XG"),
    # OpenBSD / jBCrypt classic vector (empty password, cost 6)
    (b"", "$2a$06$DCq7YPn5Rq63x1Lad4cll.TV4S6ytwfsfvkgY8jIucDrjc8deX1s."),
]

bad = 0
for i in range(len(VECTORS)):
    pw = VECTORS[i][0]
    want = VECTORS[i][1]
    t = time.perf_counter()
    got = B.bcrypt_with_salt(pw, int(want[4:6]), want[7:29], want[1:3])
    ok = got == want and B.check_password(pw, want)
    if not ok:
        bad = bad + 1
    print("%-4s %s  %.2f s" % ("ok" if ok else "BAD", want, time.perf_counter() - t))

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        import crypt
    except ImportError:
        crypt = None
if crypt is not None:
    for i in range(10):
        pw = os.urandom(1 + i * 7).hex()[: 1 + i * 8]
        h = B.hash_password(pw, 4)
        libc = crypt.crypt(pw, h)
        ok = libc == h
        if not ok:
            bad = bad + 1
        print("%-4s libxcrypt %s" % ("ok" if ok else "BAD", h))
print("ALL OK" if bad == 0 else "%d FAILED" % bad)
