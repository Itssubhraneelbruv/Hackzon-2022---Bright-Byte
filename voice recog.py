
import speech_recognition as sr
r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("say something")
        input_voice = r.listen(source, timeout=1)
        print("Please wait a moment...")
        text = r.recognize_google(input_voice)
        a = text
        if a == "true":
            print("Name=Subhraneel \n Department = CSE \n Number = 8432453954")
        elif a=="why":
            print("Name = Yagya Raj Bhatt \n Department = CSE \n Number = 8923485438")
        elif a == "hello":
            print("Name = Vighnesh Nair \n Department = CSE \n Number = 8241535832")
        elif a == "floor":
            print("Name = Jithin J Nair \n Department = CSE \n Number = 9423445423")
        print("word said = ",text)
except:
    print("Please try again")
