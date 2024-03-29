import spacy

def main():
    # Load the SpaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Get input text from user
    input_text = input("Enter a text: ")

    # Perform NER on the input text
    doc = nlp(input_text)

    # Print named entities and their labels
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")

if __name__ == "__main__":
    main()
