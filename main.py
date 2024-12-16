from textblob import TextBlob

def correct_grammer(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

text = input("Enter your Sentence: ")
correct_text = correct_grammer(text)
print(f"Corrected: {correct_text}")