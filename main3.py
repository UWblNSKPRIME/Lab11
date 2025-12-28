import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string


print("Завантаження необхідних пакетів NLTK...")
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')


print("\nЗавантаження тексту 'Emma' Джейн Остін...")
emma_words = gutenberg.words('austen-emma.txt')


total_words = len(emma_words)
print(f"Загальна кількість слів (токенів) у тексті: {total_words}")


fdist_raw = FreqDist(emma_words)
top_10_raw = fdist_raw.most_common(10)

print("\n10 найбільш вживаних слів (до очищення):")
for word, frequency in top_10_raw:
    print(f"{word}: {frequency}")

# Побудова діаграми 1
plt.figure(figsize=(10, 5))
fdist_raw.plot(10, title="10 найбільш вживаних слів (без очищення)")


print("\nВидалення стоп-слів та пунктуації...")

stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)


filtered_words = [
    word.lower() for word in emma_words 
    if word.isalpha() and word.lower() not in stop_words
]


fdist_clean = FreqDist(filtered_words)
top_10_clean = fdist_clean.most_common(10)

print("\n10 найбільш вживаних слів (після очищення):")
for word, frequency in top_10_clean:
    print(f"{word}: {frequency}")

# Побудова діаграми 2
plt.figure(figsize=(10, 5))
fdist_clean.plot(10, title="10 найбільш вживаних слів (після видалення стоп-слів)")

plt.show()