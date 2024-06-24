import re
import os

# This is the map where dictionary terms will be stored as keys and value will be posting list with position in the file
dictionary = {}


class Index:
    def __init__(self, path):
        self.path = path

    def buildIndex(self):
        fileList = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

        for eachFile in fileList:
            with open(os.path.join(self.path, eachFile), 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    wordList = re.findall(r'\b\w+\b', line.lower())  # Using regex to extract words

                    for position, word in enumerate(wordList, start=1):
                        if word in dictionary:
                            postingList = dictionary[word]
                            if eachFile in postingList:
                                postingList[eachFile].append((line_number, position))
                            else:
                                postingList[eachFile] = [(line_number, position)]
                        else:
                            dictionary[word] = {eachFile: [(line_number, position)]}

    def print_dict(self):
        fileobj = open("invertedIndex.txt", 'w')
        for key in dictionary:
            print(key + " --> " + str(dictionary[key]))
            fileobj.write(key + " --> " + str(dictionary[key]))
            fileobj.write("\n")
        fileobj.close()


def main():
    doc_collection_path = input("Enter path of text file collection: ")
    index_object = Index(doc_collection_path)
    index_object.buildIndex()

    print("")
    print("Inverted Index :")
    index_object.print_dict()


if __name__ == '__main__':
    main()
