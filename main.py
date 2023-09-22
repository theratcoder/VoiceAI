import torch
from instruct_pipeline import InstructionTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-3b", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-3b", device_map="auto", torch_dtype=torch.bfloat16, offload_folder="./offload")

gt_pipe = InstructionTextGenerationPipeline(model=model, tokenizer=tokenizer)

def gen_text(prompt):
    res = gt_pipe(prompt)
    return res[0]["generated_text"]

###################################

r = sr.Recognizer()
mic = sr.Microphone()

print("Press enter to start...")
input()

while 1:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        prompt = r.recognize_google(audio)
    except sr.UnknownValueError:
        sorry = "Sorry, I couldn't understand that."
        print(sorry)

        speech = gTTS(sorry, slow=False)
        speech.save("sorry.mp3")
        playsound("sorry.mp3")

        continue
    
    print(prompt)

    if prompt == "exit":
        bye = "Bye!"
        print(bye)

        speech = gTTS(bye, slow=False)
        speech.save("bye.mp3")
        playsound("bye.mp3")

        break

    res = gen_text(prompt)
    print(res)

    speech = gTTS(res, slow=False)
    speech.save("mp3.mp3")
    playsound("mp3.mp3")