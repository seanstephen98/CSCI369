# written by Sean Stephen for assignment question 5

import requests

# handle error if http request ends up with an error
# DNS failure, conn refused
# returns Response object if response is 200 OK

def check_subdirectory(url):
    try:
        response = requests.get(url)

        if (response.status_code == 200):
            
            return True
        
    except requests.exceptions.ConnectionError:
        pass

    return False


# parse file of dictionary names
# returns all dictionary words in the file, as a list

def read_dictionary(filename):

    file = open(filename, "r")
    wordList = file.readlines()
    file.close()
    returnWordList = []
    for word in wordList:
        returnWordList.append(word.strip())
    return returnWordList

# uses provided dictionary file name to get dictionary list of subdirectories
# checks if subdirectories exist
# prints result and also outputs valid subdirectories to a file of the given output file name

def find_subdirectories(meta_ip, dictionary_file, output_file):

    wordList = read_dictionary(dictionary_file)

    file = open(output_file, "w")

    for word in wordList:
        target_website_subdirectory = "http://" + meta_ip + "/mutillidae/" + word

        # if the subdirectory exists and returns 200 OK response code (handled in check function)
        # then print it out and write it to a file as well
        if (check_subdirectory(target_website_subdirectory)):
            file.write(target_website_subdirectory)
            file.write(" Exists\n")
            print("\n" + target_website_subdirectory + " Exists\n")

        # any other response code is not considered alive and ignored
        else:
            pass
 

    file.close()         

# get target url, dictionary file name, output file name from user, then send through function to find subdirectories

dictionary_file_name = input("\nPlease enter the dictionary file name (e.g. list.txt) : ")

output_file_name = input("\nPlease enter the output file name (e.g. output.txt) : ")

meta_ip = input("\nPlease enter meta ip : ")

print("\nFinding subdirectories... ")

find_subdirectories(meta_ip, dictionary_file_name, output_file_name)

print("\nAll dictionary words tested against target website. Program ending now...")