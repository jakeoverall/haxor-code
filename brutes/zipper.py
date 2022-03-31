from zipfile import ZipFile


def start():
    filepath = input('Zipfile: ')
    extract_location = input('where would you like to extract this to?')
    # TODO get the file list and try each password in the list 


def attempt_to_unzip(filepath:str, password: str, extract_location: str):
    try:
        with ZipFile(filepath) as f:
            f.extractall(extract_location, f.filelist, bytes('password', 'utf-8'))
            f.close()
            print(f'Successfully extracted with password {password}')
            exit(1)
    except: 
        return False


start()
