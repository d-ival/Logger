from logger import log_proc_call
from hashlib import md5

@log_proc_call('log.txt')
def file_line_md5(file_path : str):

    with open(file_path, encoding='utf8') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break

            yield md5(line.encode())
                #yield md5(file.readline())

if __name__ == '__main__':
    for hash_obj in file_line_md5('countries_wiki.txt'):
        print(hash_obj.hexdigest())
