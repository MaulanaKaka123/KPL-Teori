from enum import Enum
import time

#Automata => State
class TrafficLight(Enum):
    Merah = "Merah"
    Hijau = "Hijau"
    Kuning = "Kuning"

#Automata => State atau Perubahan atau Transisi
# Map< Key, Value>
# Key => State Awal
# Value => State Tujuan
state_transition = {
    TrafficLight.Merah: TrafficLight.Hijau,
    TrafficLight.Hijau: TrafficLight.Kuning,
    TrafficLight.Kuning: TrafficLight.Merah
}

state_duration = {
    TrafficLight.Merah: 7,
    TrafficLight.Hijau: 5,
    TrafficLight.Kuning: 2
}

def traffic_light():
    current_state = TrafficLight.Merah
    while True:
        print(f"Lampu: {current_state.value}")
        time.sleep(state_duration[current_state])
        current_state = state_transition[current_state]
traffic_light()

# current_state = TrafficLight.Merah
# next_state = state_transition[current_state] #Hijau, Kuning atau Merah
# print(next_state)





