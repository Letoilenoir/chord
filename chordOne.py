#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import midiutil
import os

# Global variables
error_label = None
midi_file = None
track = 0
channel = 0
time = 0

# Define a dictionary of chord types
chord_types = {
    "Major": [0, 4, 7],
    "Minor": [0, 3, 7],
    "Diminished": [0, 3, 6],
    "Augmented": [0, 4, 8],
    "Seventh": [0, 4, 7, 10],
    "Major 7th": [0, 3, 7, 11],
    "Minor 7th": [0, 3, 7, 10],
    "Diminished 7th": [0, 3, 6, 9],
    "Aug 7th": [0, 4, 8, 10],
    "Aug 9th": [0, 4, 7, 10, 14],
    "Aug 11th": [0, 4, 8, 10, 18],
    "Aug 13th": [0, 4, 8, 10, 14, 18],
    "Maj 9th": [0, 4, 7, 11, 14],
    "Min 9th": [0, 3, 7, 10, 14],
    "Dom 9th": [0, 4, 7, 10, 14],
    "Min 11th": [0, 3, 7, 10, 14, 17],
    "Dom 11th": [0, 4, 7, 10, 14, 17],
    "Maj 13th": [0, 4, 7, 11, 14, 21],
    "Min 13th": [0, 3, 7, 10, 14, 21],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7],
}

# Define a dictionary to map note names to MIDI note numbers
note_map = {
    "C": 60,
    "C#": 61,
    "Db": 61,
    "D": 62,
    "D#": 63,
    "Eb": 63,
    "E": 64,
    "F": 65,
    "F#": 66,
    "Gb": 66,
    "G": 67,
    "G#": 68,
    "Ab": 68,
    "A": 69,
    "A#": 70,
    "Bb": 70,
    "B": 71
}

# Function to handle button click
def generate_chord():
    global midi_file, track, channel, time

    root_note = root_note_entry.get().capitalize()  # Convert the first letter to uppercase
    if root_note not in note_map:
        # Display an error message for invalid input
        error_label.config(text="Invalid root note")
        return
    root_note_num = note_map[root_note]
    chord_type = chord_type_var.get()

    # Get the duration from the Entry widget
    try:
        duration = float(duration_entry.get())
    except ValueError:
        # Display an error message for invalid duration input
        error_label.config(text="Invalid duration")
        return

    # Generate MIDI events for each note in the chord
    for note in chord_types[chord_type]:
        # Add note-on event
        midi_file.addNote(
            track,
            channel,
            note + root_note_num,
            time,
            duration=duration,
            volume=100
        )

    # Add a rest between chords
    time += duration

    # Ask the user if they want to add another chord
    response = messagebox.askyesno("Add Chord", "Do you want to add another chord?")
    if response:
        # Clear the entry fields for the next chord
        root_note_entry.delete(0, tk.END)
        chord_type_var.set("Major")  # Set default value for chord type
        duration_entry.delete(0, tk.END)
    else:
        # Save the MIDI file and close the application
        save_and_exit()

def save_and_exit():
    global midi_file

    # Find a non-existing file name with an incremental suffix
    base_name = "progression"
    suffix = 1
    while os.path.exists(f"{base_name}_{suffix}.mid"):
        suffix += 1
    
    # Save the MIDI file
    file_name = f"{base_name}_{suffix}.mid"
    with open(file_name, "wb") as file:
        midi_file.writeFile(file)
    
    # Close the GUI
    root.destroy()

# Create MIDI file
midi_file = midiutil.MIDIFile(1)  # 1 track
track = 0
channel = 0
time = 0

# Create GUI
root = tk.Tk()
root.title("Chord Structure Generator")

# Root Note Label and Entry
root_note_label = tk.Label(root, text="Root Note")
root_note_label.grid(row=0, column=0)
root_note_entry = tk.Entry(root)
root_note_entry.grid(row=0, column=1)

# Chord Type Label and Dropdown
chord_type_label = tk.Label(root, text="Chord Type")
chord_type_label.grid(row=1, column=0)
chord_type_var = tk.StringVar(root)
chord_type_var.set("Major")  # Set default value
chord_type_dropdown = tk.OptionMenu(root, chord_type_var, *chord_types.keys())
chord_type_dropdown.grid(row=1, column=1)

# Duration Label and Entry
duration_label = tk.Label(root, text="Duration (beats)")
duration_label.grid(row=2, column=0)
duration_entry = tk.Entry(root)
duration_entry.grid(row=2, column=1)

# Error Label
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=2)

# Generate Chord Button
generate_button = tk.Button(root, text="Generate Chord", command=generate_chord)
generate_button.grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
