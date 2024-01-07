07/01/2024 Tested for Midi file output via new VS install
"Flat" Root notes eg "Ab" not currently recognised as valid user input, Sharp root notes(eg A#) & natural (eg A) working.

Chord Structure Generator

This is a simple Python script that generates MIDI files for different chord types based on user input. It provides a graphical user interface (GUI) using the Tkinter library for easy interaction.

Dependencies

    Python 3
    Tkinter library
    midiutil library

Usage

    Make sure you have Python 3 installed on your system.
    Install the required dependencies by running the following command:

pip install midiutil

Run the script using the following command:

    python chord.py

    The GUI window titled "Chord Structure Generator" will open.
    Select the root note of the chord from the "Root Note" entry field.
    Choose the chord type from the dropdown menu labeled "Chord Type".
    Click the "Generate Chord" button to generate the MIDI file.
    The MIDI file will be saved with the name <root_note>_<chord_type>.mid in the current directory.
    If a MIDI file with the same name already exists, it will be overwritten.

Chord Types

The script supports the following chord types:

    Major
    Minor
    Diminished
    Augmented
    Seventh

Note Mapping

The script includes a dictionary called note_map, which maps note names to their corresponding MIDI note numbers. This mapping is used to determine the MIDI note number for the root note of the chord. If you need to add or modify note mappings, you can update the note_map dictionary accordingly.
GUI Interface

The GUI provides the following elements for user interaction:

    Root Note Label and Entry: Enter the root note of the chord in this field.
    Chord Type Label and Dropdown: Select the desired chord type from the dropdown menu.
    Error Label: Displays error messages, such as invalid root note.
    Generate Chord Button: Click this button to generate the MIDI file based on the provided inputs.

Notes

    The generated MIDI files use a single track with a duration of 1 and a volume of 100 for each note in the chord.
    The GUI event loop is started using the mainloop() method, which allows the GUI to respond to user interactions.

Feel free to modify and enhance this script as per your needs. Happy chord generating!
