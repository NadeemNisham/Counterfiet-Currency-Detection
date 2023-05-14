import time

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
                  "\n3. Identify Counterfeit note\n4. Sum up currency\n5. Settings\n6. Exit\n\n->"))
    except Exception as e:
        print(e)

    if option == 1:
        if dn.detect_note():
            note.main()
            utility.voice_out(note.value)
    elif option == 2:
        if dn.detect_note():
            coin.main()
            utility.voice_out(coin.value)
    elif option == 3:
        if dn.detect_note():
            note.main()
            time.sleep(4)
            utility.voice_out(f.fake_classifier(note.get_value()))
    elif option == 4:
        sumup.calculate_sum_of_notes()
    elif option == 5:
        sub_option = 1
        while 0 < sub_option < 4:
            sub_option = int(input("-Output settings-\n1. Change volume\n2. Change speed\n3. Change voice\n\n->"))
            if sub_option == 1:
                utility.change_volume()
            elif sub_option == 2:
                utility.change_speed()
            elif sub_option == 3:
                utility.change_voice()
            else:
                print("Settings saved")
                pass
    elif option == 6:
        utility.voice_out("Have a nice day!")
