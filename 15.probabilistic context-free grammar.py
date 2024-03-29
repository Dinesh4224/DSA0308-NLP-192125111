import nltk
from nltk import PCFG, ViterbiParser

def main():
    # Define a simple PCFG
    grammar = PCFG.fromstring("""
        S -> NP VP [1.0]
        NP -> Det N [0.5] | NP PP [0.25] | 'I' [0.25]
        VP -> V NP [0.7] | VP PP [0.3]
        PP -> P NP [1.0]
        Det -> 'the' [0.7] | 'my' [0.3]
        N -> 'dog' [0.5] | 'cat' [0.5]
        V -> 'chased' [1.0]
        P -> 'with' [0.61] | 'in' [0.39]
    """)

    # Create a Viterbi parser
    parser = ViterbiParser(grammar)

    # Get input sentence from user
    input_sentence = input("Enter a sentence: ").strip().split()

    # Parse the input sentence using the Viterbi parser
    trees = list(parser.parse(input_sentence))

    if len(trees) > 0:
        print("Parse tree:")
        print(trees[0])
        print("Probability:", trees[0].prob())
    else:
        print("No parse found for the sentence.")

if __name__ == "__main__":
    main()
