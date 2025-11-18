DELIMITER = ','

def collectWords():
    Cwords = []
    while True:
        Cword = input("Insert word(empty stops): ")
        if Cword == "":
            break
        Cwords.append(Cword)
    return DELIMITER.join(Cwords)

def analyseWords(Pwords):
    if not words_string:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return
    words_list = words_string.split(DELIMITER) 
    total_words = len(words_list)
    total_characters = sum(len(word) for word in words_list)
    avg_length = total_characters / total_words if total_words > 0 else 0
    
    print(f"- {total_words} Words")
    print(f"- {total_characters} Characters")
    print("- {:.2f} Average word length".format(avg_length))

def main():
    print("Program starting.")
    collected_words = collectWords()
    analyseWords(collected_words)
    print("Program ending.")

if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()
