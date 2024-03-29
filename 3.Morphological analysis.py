import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('wordnet')

def perform_morphological_analysis(text):
    words = word_tokenize(text)

 
    porter = PorterStemmer()
    lancaster = LancasterStemmer()
    snowball = SnowballStemmer('english')
    lemmatizer = WordNetLemmatizer()

    stemmed_words = [porter.stem(word) for word in words]
    lancaster_words = [lancaster.stem(word) for word in words]
    snowball_words = [snowball.stem(word) for word in words]
    lemmatized_words = [lemmatizer.lemmatize(word, wordnet.VERB) for word in words]

    return stemmed_words, lancaster_words, snowball_words, lemmatized_words

def main():
    text = input("Enter a sentence for morphological analysis: ")
    stemmed_words, lancaster_words, snowball_words, lemmatized_words = perform_morphological_analysis(text)

    print("\nStemmed words (Porter Stemmer):")
    print(stemmed_words)

    print("\nStemmed words (Lancaster Stemmer):")
    print(lancaster_words)

    print("\nStemmed words (Snowball Stemmer):")
    print(snowball_words)

    print("\nLemmatized words:")
    print(lemmatized_words)

if __name__ == "__main__":
    main()
