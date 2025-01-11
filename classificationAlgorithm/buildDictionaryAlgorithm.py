import os
from collections import defaultdict
import math



def build_dictionary(train_folder):
    dictionary = defaultdict(int)
    for class_folder in os.listdir(train_folder):
        class_folder_path = os.path.join(train_folder, class_folder)
        if os.path.isdir(class_folder_path):
            for filename in os.listdir(class_folder_path):
                file_path = os.path.join(class_folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        words = line.split()
                        for word in words:
                            dictionary[word] += 1
    return dictionary



# # Get the directory of the current script 
# current_dir = os.path.dirname(os.path.abspath(__file__)) 
# # Construct the path to the "classification-traint and test" directory 
# train_folder_path = os.path.join(current_dir, 'Classification-Data') 





# dictionary = build_dictionary(train_folder_path)
# print(len(dictionary))
# print(dictionary["that"])

# print("folder path : "+ train_folder_path)



def calculate_class_probabilities(train_folder):
    
    class_counts = defaultdict(int)

    class_counts['Comp.graphics'] = 1 / 5
    class_counts['rec.autos'] = 1 % 5
    class_counts['talk.politics.mideast'] = 1 / 5
    class_counts['soc.religion.christian'] = 1 / 5
    class_counts['sci.electronics'] = 1 / 5

    return class_counts


# class_probabilities = calculate_class_probabilities(train_folder_path)
# print("\n______________")
# print(len(class_probabilities))
# print(class_probabilities['Comp.graphics'])
import os
from collections import defaultdict

def calculate_conditional_probabilities(train_folder, dictionary):
    word_counts = defaultdict(lambda: defaultdict(int))
    class_counts = defaultdict(int)
    
    for class_folder in os.listdir(train_folder):
        class_folder_path = os.path.join(train_folder, class_folder)
        if os.path.isdir(class_folder_path):
            for filename in os.listdir(class_folder_path):
                file_path = os.path.join(class_folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        words = line.split()
                        for word in words:
                            word_counts[class_folder][word] += 1
                            class_counts[class_folder] += 1
    
    conditional_probabilities = {}
    for cls, words in word_counts.items():
        conditional_probabilities[cls] = {word: (count + 1) / (class_counts[cls] + len(dictionary)) for word, count in words.items()}
        
        # Ensure all words in the dictionary have an entry in the probabilities dictionary
        for word in dictionary:
            if word not in conditional_probabilities[cls]:
                conditional_probabilities[cls][word] = 1 / (class_counts[cls] + len(dictionary))
    
    return conditional_probabilities





def classify_test_document(document, class_probabilities, conditional_probabilities, dictionary):
    words = document.split()
    class_scores = {}
    for cls in class_probabilities:
        class_scores[cls] = math.log(class_probabilities[cls])
        for word in words:
            if word in dictionary:
                class_scores[cls] += math.log(conditional_probabilities[cls].get(word, 1 / (sum(dictionary.values()) + len(dictionary))))
    return max(class_scores, key=class_scores.get)


