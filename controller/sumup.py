import detect_note
import identify_note as note
import utility


def calculate_sum_of_notes():
    cont = 'y'
    sum_of_notes = 0  # Variable to keep track the sum of the detected notes
    # loop until there are no more notes detected
    while detect_note.detect_note():
        if cont.capitalize() == 'Y':
            note.main()
            note_value = note.get_value()  # Get the value of the detected note
            sum_of_notes += int(note_value)  # Add the note value to the total sum
            utility.voice_out(f"Current total is {sum_of_notes}")
            utility.voice_out("Type y to sum up next note or x to exit: ")
            cont = input("Type y to sum up next note or x to exit: ")
            if cont.capitalize() == 'X':
                break
            else:
                continue
