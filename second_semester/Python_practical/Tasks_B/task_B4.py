"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

def wiki_function(filename):
    # Read the file line by line and add non-empty lines to a list
    print ('>>Read the file line by line and add non-empty lines to a list')
    with open(filename, "r") as f:
        for line in f:
            print (line)
    print ("\n\n")
    # print ('Select what to do with the text: \n1-> Add non-empty lines into a list\n->Remove everything except latins characters\n->')
    
    print ('>>adding non-empty lines to a list:')
    lines = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)
    print (lines)
    
    
    print ("->Removing other characters except latins: \n")
    latins = ''
    with open(filename, "r") as f:
      for line in f: 
        
        for lat in line: 
          if lat.isalpha() or lat.isspace():
            latins+= lat
    print (latins)
    print ('\n\n->Joining all characters from list using join method with comman as separator: ')
    string = " ".join(lines)
    print (string)
    print("\n\n-> Creating a dic which contains the words as key and value as quantity: ") 
    word_count = {}
    for word in string.split():
        word = word.lower()
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    print (word_count)
    print ("->10 most used words in txt: \n")
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i, (word, count) in enumerate(sorted_words[:10]):
        print(f"{i+1} place --- {word} --- {count} times")
    print ("->changing them to python: \n")
    top_words = [word for word, count in sorted_words[:10]]
    python = ' '
    for i in range(len(top_words)):
      top_words[i] = "PYTHON"
      python += top_words[i] + " "
    print (python)
    
    #!to write a new file with nomore than 100 chars in a line 
    
    print ("->writing the string to a new file: \n\n")
    with open("output.txt", "w") as f:
        while len(string) > 100:
            index = string.rfind(" ", 0, 100)
            if index == -1:
                index = 100
            f.write(string[:index] + "\n")
            string = string[index+1:]
        f.write(string)
    # translator = str.maketrans("", "", filename.digits + filename.punctuation)
    # cleaned_lines = [line.translate(translator) for line in lines]
    # # Combine all the lines into one string using space as the separator
    # text = " ".join(cleaned_lines)
    # # # Create a dictionary to count the occurrences of different words
    # word_count = {}
    # for word in text.split():
    #     word = word.lower()
    #     if word not in word_count:
    #         word_count[word] = 0
    #     word_count[word] += 1
    # # Print the 10 most popular words in descending order using formatting
    # sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # for i, (word, count) in enumerate(sorted_words[:10]):
    #     print(f"{i+1} place --- {word} --- {count} times")
    # # Replace the 10 most popular words in the string with the word "PYTHON"
    # top_words = [word for word, count in sorted_words[:10]]
    # for word in top_words:
    #     text = text.replace(word, "PYTHON")
    # # Write the modified text to a new file
    # with open("output.txt", "w") as f:
    #     while len(text) > 100:
    #         index = text.rfind(" ", 0, 100)
    #         if index == -1:
    #             index = 100
    #         f.write(text[:index] + "\n")
    #         text = text[index+1:]
    #     f.write(text)
    return 1
# Вызов функции
wiki_function("python.txt")


