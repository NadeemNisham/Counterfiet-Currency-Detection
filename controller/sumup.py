from tensorflow.keras.models import load_model

# Load the pre-trained note recognition model
model = load_model('model_weights.h5')

def sum_currency_notes():

    # Define the currency note values
    note_values = {20: 20, 50: 50, 100: 100, 500: 500, 1000: 1000, 5000: 5000}

    # Initialize a variable to keep track of the sum of note values
    sum_notes = 0.0

    # loop through the recognized notes
    for note in recognized_notes:
        if note.is_held:
            # If note is being held, add its value to the sum
            sum_notes += note_values[note.denomination]
        print(sum_notes)


