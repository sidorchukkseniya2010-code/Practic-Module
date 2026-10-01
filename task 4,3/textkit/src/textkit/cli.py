from .stats import char_stats, word_count

def main():
    t = "Тест работы пакета"
    print(f"Слов: {word_count(t)} | Статистика: {char_stats(t)}")

if __name__ == "__main__":
    main()
