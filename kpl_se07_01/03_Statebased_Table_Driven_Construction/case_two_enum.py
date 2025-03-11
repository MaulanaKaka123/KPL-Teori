from enum import Enum
class JenisKelamin(Enum):
    Pria = 1
    Wanita = 2

patients = []

def add_patient(name : str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Harus Pria atau Wanita")
    patients.append({"name": name, "gender": gender.name})

add_patient("Andi", JenisKelamin.Pria)
add_patient("Siti", JenisKelamin.Wanita)

for patient in patients:
    print(f"{patient['name']} adalah {patient['gender']}")
