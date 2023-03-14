import detect_note
import identify_note as note

# # Load the pre-trained note recognition model
# model = load_model('model_weights.h5')

notes = []  # List to store the detected notes
sum_of_notes = 0.0  # Variable to keep track the sum of the detected notes


def calculate_sum_of_notes():
    global sum_of_notes

    # loop untill there are no more notes detected
    while detect_note.detect_note():
        note.main()
        note_value = note.get_value()  # Get the value of the detected note
        notes.append(note_value)  # Add the note value to the list of notes
        sum_of_notes += float(note_value)  # Add the note value to the total sum
        print(sum_of_notes)
    return sum_of_notes, notes


def get_sum_of_notes():
    return sum_of_notes


def get_notes():
    return notes
