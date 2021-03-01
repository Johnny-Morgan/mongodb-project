import os
import pymongo
if os.path.exists('env.py'):
    import env


MONGO_URI = os.environ.get('MONGO_URI')
DATABASE = 'myFirstDB'
COLLECTION = 'celebrities'


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print(f'Could not connect to MongoDB: {e}')


def show_menu():
    print('')
    print('1. Add a record')
    print('2. Find a record by name')
    print('3. Edit a record')
    print('4. Delete a record')
    print('5. Exit')

    option = input('Enter option: ')
    return option


def get_record():
    print('')
    first = input('Enter first name: ')
    last = input('Enter last name: ')

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print('Error accessing database')

    if not doc:
        print('\nError! No results found.')

    return doc


def add_record():
    print('')
    first = input('Enter first name: ')
    last = input('Enter last name: ')
    dob = input('Enter dob: ')
    gender = input('Enter gender: ')
    hair_color = input('Enter hair color: ')
    occupation = input('Enter occupation: ')
    nationality = input('Enter nationality: ')

    new_doc = {
        'first': first.lower(),
        'last': last.lower(),
        'dob': dob,
        'gender': gender,
        'hair_color': hair_color,
        'occupation': occupation,
        'nationality': nationality
    }

    try:
        coll.insert(new_doc)
        print('\nDocument Inserted')
    except:
        print('Error accessing database')


def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            print('You have chosen option 2')
        elif option == '3':
            print('You have chosen option 3')
        elif option == '4':
            print('You have chosen option 4')
        elif option == '5':
            print('Exiting...')
            conn.close()
            break
        else:
            print('Invalid option')
        print('')


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]

main_loop()
