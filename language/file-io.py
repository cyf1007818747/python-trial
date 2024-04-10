

def basic_text_file_ops():
    # // append_txt()
    import random

    def read_txt():
        with open('../resources/test-text.txt', 'r') as myfile:
            file_read = myfile.read() # a string of whole file
            lines = myfile.readlines()  # a list of lines in myfile
            print('file.closed:', myfile.closed)
        
    def overwrite_txt():
        # write to a new file # ! in reality try to use 'a' if possible to prevent overwriting
        # note that the directory must exist. cannot create new directory
        with open('../resources/w_files/random_ints.txt', 'w') as myfile:
            for i in range(10):
                rand_int = random.randrange(100)
                # // myfile.write(rand_int)
                myfile.write(str(rand_int) + '\n')

    def append_txt():
        with open('../resources/w_files/random_ints.txt', 'a') as myfile:
            for i in range(20):
                rand_int = random.randrange(100, 200)
                # // myfile.write(rand_int)
                myfile.write(str(rand_int) + '\n') # this will not overwrite contents under current opening
    
    append_txt()


def basic_json_ops():
    import json
    from pprint import pprint

    json_path = '../resources/package.json'

    def read_json():
        with open(json_path, 'r') as jsonfile:
            myjson_r = json.load(jsonfile) # add _r to the name make it clearer # *
            # print('myjson:', myjson)
            # // pprint('myjson:', myjson) # pprint api is different
            pprint(myjson_r) # print in structured format # *
            print('myjson type:', type(myjson_r)) # type is dict
            print('myjson["scripts"] type:', type(myjson_r['scripts']))

    # only suitable for very small files
    def write_json(): # *
        with open(json_path, 'r') as jsonfile:
            myjson_r = json.load(jsonfile)

        # make it to be int is fine for general json, but package.json should onlt contains str values
        myjson_r['scripts']['lint'] = '123456'

        with open(json_path, 'w') as jsonfile:
            # json.dump(myjson_r, jsonfile) # the written json file is unformatted (in one line)
            # json.dump(myjson_r, jsonfile, indent=4) # this will make the file formatted
            json.dump(myjson_r, jsonfile, indent=4, sort_keys=True) # this will sort the key in reverse order

    read_json()


def basic_yaml_ops():
    from pprint import pprint
    try:
        import yaml
    except ImportError:
        print('You should install pyyaml in your env before calling basic_yaml_ops().')

    yaml_path = '../resources/docker-compose.yml'

    def read_yaml():
        with open(yaml_path, 'r') as yamlfile:
            myyaml_r = yaml.safe_load(yamlfile) # skip comments
            pprint(myyaml_r)
            print('type myyaml_r:', type(myyaml_r)) # dict type

    # only suitable for very small files
    def write_yaml():
        with open(yaml_path, 'r') as yamlfile:
            myyaml_r = yaml.safe_load(yamlfile) # skip comments

        print('------', myyaml_r['services']['adminer']['ports'])
        myyaml_r['services']['adminer']['ports'] = ['123456:654321', 1, 2, 3]

        with open(yaml_path, 'w') as yamlfile:
            yaml.dump(myyaml_r, yamlfile, indent=4)

    write_yaml()


def large_file_ops():
    r_path = '../resources/test-text.txt'
    w_path = '../resources/modified-text.txt'
    with open(r_path, 'r') as source_file, open(w_path, 'w') as modified_file:
        # this iteration approach will open only one line of the file
        for line in source_file:
            line = line[:-1] # since originally, each line ends with \n
            line += ' -- modified by Chris on 4.10\n'
            modified_file.write(line)


large_file_ops()
