from machine import Pin, PWM
import time

octave_4_frequencies = {"C4": 261.63, # do
                "C#4/Db4": 277.18, 
                "D4": 293.66, # RE
                "D#4/Eb4": 311.13,
                "E4": 329.63, # MI
                "F4": 349.23,#FA 
                "F#4/Gb4": 369.99,
                "G4": 392.00,# SO
                "G#4/Ab4": 415.30,
                "A4": 440.00,# LA
                "A#4/Bb4": 466.16,
                "B4": 493.88} # TI


buz = PWM(Pin(0, Pin.OUT))
buz.duty_u16(int(30000))

def play_notes(note_string):
    notes_array = note_string.split(" ")
    print(notes_array)
    
    for note in notes_array:
        if note != "S":
            buz.freq(int(octave_4_frequencies[note]))
            time.sleep(0.5)
        else:
            buz.duty_u16(0)
            time.sleep(0.5)
            buz.duty_u16(int(30000))
        
        buz.duty_u16(0)
        time.sleep(0.025)
        buz.duty_u16(int(30000))

mary_had_a_little_lamb_notes_octave_4 = "E4 D4 C4 D4 E4 E4 E4 S D4 D4 D4 S E4 G4 G4 S E4 D4 C4 D4 E4 E4 E4 S E4 D4 D4 E4 D4 C4 S S S"
twinkle_twinkle_notes_octave_4 = "C4 C4 G4 G4 A4 A4 G4 S F4 F4 E4 E4 D4 D4 C4 S G4 G4 F4 F4 E4 E4 D4 S G4 G4 F4 F4 E4 E4 D4 S C4 C4 G4 G4 A4 A4 G4 S F4 F4 E4 E4 D4 D4 C4 S S"

while True:
    play_notes(twinkle_twinkle_notes_octave_4)
    #time.sleep(2)