from enum import Enum

# State
class StudentStatusState(Enum):
    Terdaftar = "Terdaftar"
    Aktif = "Aktif"
    Cuti = "Cuti"
    Lulus = "Lulus"

#Trigger Input
class TriggerInputState(Enum):
    Cetak_KSM = "Cetak KSM"
    Menyelesaikan_Cuti = "Menyelesaikan Cuti"
    Lulus = "Lulus"
    Mengajukan_Cuti = "Mengajukan Cuti"

#Transition
state_transition = {
    StudentStatusState.Terdaftar: {
        TriggerInputState.Cetak_KSM: StudentStatusState.Aktif,
        TriggerInputState.Mengajukan_Cuti: StudentStatusState.Cuti
    },
    StudentStatusState.Aktif: {
        TriggerInputState.Lulus: StudentStatusState.Lulus,
        TriggerInputState.Mengajukan_Cuti: StudentStatusState.Cuti
    },
    StudentStatusState.Cuti: {
        TriggerInputState.Menyelesaikan_Cuti: StudentStatusState.Terdaftar
    }
}

def change_state(current_state, trigger):
    cond_1 = current_state in state_transition # Return True or False
    cond_2 = trigger in state_transition[current_state] # Return True or False
    if cond_1 and cond_2:
        #Terdaftar, Aktif, Lulus, Cuti
        return state_transition[current_state][trigger]
    return "Transisi Tidak Valid"

current_state = StudentStatusState.Lulus
trigger = TriggerInputState.Mengajukan_Cuti

next_state = change_state(current_state, trigger)

print(next_state)