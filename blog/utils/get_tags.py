from posts.models import Post
import markdown
import re
from bs4 import BeautifulSoup


stopWords = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
]


def get_tags(post_content):
    word_frequency = {}
    post_content = md_to_text(post_content)
    post_content = re.sub(r"[^\w’]+|_|[0-9]+", " ", post_content.lower())
    words_to_analyse = post_content.split()
    for word in words_to_analyse:
        if word not in stopWords:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    sort_by_frequency = sorted(word_frequency, key=word_frequency.get, reverse=True)
    tags_list = sort_by_frequency[:5]
    tags = ', '.join(tags_list)
    return tags


# The following function was taken from https://stackoverflow.com/a/64575233/5722171
def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()
