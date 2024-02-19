import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from collections import defaultdict
import string

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=5):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Filter out stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Calculate frequency distribution of words
    word_frequencies = FreqDist(filtered_words)
    max_frequency = max(word_frequencies.values())

    # Normalize word frequencies
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / max_frequency)

    # Scoring sentences
    sentence_scores = defaultdict(int)
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                sentence_scores[sent] += word_frequencies[word]

    # Sorting sentences by score
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    # Joining the selected sentences
    summary = ' '.join(summary_sentences)
    return summary


