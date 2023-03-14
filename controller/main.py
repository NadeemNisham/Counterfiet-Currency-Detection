import identify_note as note
import fake_classifier as f
import detect_note as dn
import identify_coin as coin
import utility
import sumup

while True:
    option = 0
    try:
        option = int(
            input("Enter one of the below options: \n1. Identify note \n2. Identify coin"
                  "\n3. Identify Counterfeit note\n4. Sum up currency\n5. Exit\n\n->"))
    except Exception as e:
        print(e)

    if option == 1:
        if dn.detect_note():
            print("Image found")
            note.main()
            print(note.get_value())
    elif option == 2:
        if dn.detect_note():
            print("Image found")
            coin.main()
            print(coin.get_value())
    elif option == 3:
        print("Image found")
        if dn.detect_note():
            note.main()
            utility.voice_out(f.fake_classifier(note.get_value()))
    elif option == 4:
        while dn.detect_note():
            note.main()
            sumup.calculate_sum_of_notes()
            utility.voice_out("Identified notes:"+sumup.get_notes())
            utility.voice_out("the sum of the note is"+sumup.get_sum_of_notes())
    elif option == 5:
        utility.voice_out("Have a nice day!")
