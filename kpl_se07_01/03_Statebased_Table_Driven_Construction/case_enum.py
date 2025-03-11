from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2

print(JenisKelamin.LAKI_LAKI) # Value of Enum
print(JenisKelamin.LAKI_LAKI.value) # Value dari Laki-laki = 1
print(JenisKelamin.LAKI_LAKI.name) # Nama Enum

# Dart Programming
# enum Status {ONLINE, OFFLINE, BUSY}

