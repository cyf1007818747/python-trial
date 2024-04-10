import os

def path_trial():
    cur_dir = os.getcwd()
    print('cur_dir:', cur_dir)
    
    cur_dir_splitted = os.path.split(cur_dir) # returns a tuple of dirname and basename
    print('cur_dir_splitted:', cur_dir_splitted)

    cur_dir_basename = os.path.basename(cur_dir)
    print('cur_dir_basename:', cur_dir_basename)

    cur_dir_dirname = os.path.dirname(cur_dir)
    print('cur_dir_dirname:', cur_dir_dirname)

    while os.path.basename(cur_dir):
        cur_dir = os.path.dirname(cur_dir)
        print('cur_dir:', cur_dir)




path_trial()