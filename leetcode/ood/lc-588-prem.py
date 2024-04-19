from typing import List

"""
Question: Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path 
does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
"""

# ---- copied from user's solution from .cn
# leetcode time     cost : 112 ms
# leetcode memory   cost : 13.7 MB
# solution 1, dir struct contains sub element of dict files and dirs.
class Dir:
    def __init__(self):
        self.dirs = {}
        self.files = {}

class FileSystem_copied1:
    def __init__(self):
        self.root = Dir()
        
    #def ls(self, path: str) -> List[str]:
    def ls(self, path):
        dir_struct = self.root
        files = []
        if path is not "/":
            path_list = path.split("/")
            # loop deeper until the last dir
            for i in range(1,len(path_list)-1):
                dir_struct = dir_struct.dirs[ path_list[i] ]

            # check if the input file is file item or dir item
            if (path_list[-1] in dir_struct.files):
                files.append(path_list[-1])    
                return files
            # otherwise the item is a dir item, get the dir name
            else:
                dir_struct = dir_struct.dirs[ path_list[-1] ]
        files = list(dir_struct.dirs.keys()) + list(dir_struct.files.keys())
        files.sort()
        return files
            
    def mkdir(self, path):
        dir_struct = self.root
        path_list = path.split("/")
        for i in range(1, len(path_list)):
            if path_list[i] not in dir_struct.dirs.keys():
                dir_struct.dirs[ path_list[i] ] = Dir()
            dir_struct = dir_struct.dirs[ path_list[i] ]

    def addContentToFile(self, filePath, content):
        dir_struct = self.root
        path_list = filePath.split("/")
        for i in range(1, len(path_list)-1):
            dir_struct = dir_struct.dirs[ path_list[i] ]
        if path_list[-1] in dir_struct.files.keys():   
            dir_struct.files[ path_list[-1] ] = dir_struct.files[ path_list[-1] ] + content
        else:
            dir_struct.files[ path_list[-1] ] = "" + content
            

    def readContentFromFile(self, filePath: str) -> str:
        dir_struct = self.root
        path_list = filePath.split("/")
        for i in range(1, len(path_list)-1):
            dir_struct = dir_struct.dirs[ path_list[i] ]
        fileContent = dir_struct.files[ path_list[-1] ]
        return fileContent

# # Your FileSystem object will be instantiated and called as such:
# def main():
#     obj = FileSystem_copied1()
#     operation= ["FileSystem","ls","ls","mkdir","ls","ls","ls","ls","addContentToFile","readContentFromFile","ls"]
#     words = [[],["/"],["/"],["/rsx"],["/rsx"],["/"],["/"],["/"],["/bxjzdc","iozcpr"],["/bxjzdc"],["/rsx"]]           
#     # expect is [null,[],[],null,[],["rsx"],["rsx"],["rsx"],null,"iozcpr",[]]
#     print(None)
#     for i in range(1,len(operation)):
#         print("operation: ",operation[i],",parameter: ",words[i][0])
#         if len(words[i])>1:
#             cmd = 'obj.'+operation[i]+"(%r,%r)" % (words[i][0],words[i][1])
#         else:
#             cmd = 'obj.'+operation[i]+"(%r)" % words[i][0]
#         result = eval(cmd)
#         print("result: ",result)
    
# if __name__ =='__main__':
#     main()


# write after reading official solution 1, using the same idea
# start to AC - 30:52
# AC
class Dir:
    def __init__(self):
        self.dirs = {}
        self.files = {}

class FileSystem:
    def __init__(self):
        self.root = Dir()

    def ls(self, path: str) -> List[str]:
        plist = path.split('/')
        cur = self.root
        rtn = []
        # process all but the last elements
        for i in range(1, len(plist) - 1):
            # detail and accuracy !!!
            # // cur = cur[plist[i]].dirs
            cur = cur.dirs[plist[i]]

        # process the last element
        pfinal = plist[-1]

        # the empty string case is very tricky, indicating that the input path is only "/"
        # you initially did not handle the empty string case properly # *
        # lesson: understanding the question and solution deeper # *
        if pfinal in cur.dirs or pfinal == "":
            if pfinal in cur.dirs:
                cur = cur.dirs[pfinal]
            # you intended to iterate over all dirs and files, but this is the wrong way
            # lesson: be very detail-oriented of the data structure you used
            # // for itm in cur:
            # //    rtn.append(itm)
            for itm in cur.files:
                rtn.append(itm)
            for itm in cur.dirs:
                rtn.append(itm)
            for itm in cur.files:
                rtn.append(itm)
            rtn.sort()
        else:
            rtn.append(pfinal)
        
        return rtn

    def mkdir(self, path: str) -> None:
        plist = path.split('/')
        cur = self.root
        for i in range(1, len(plist)):
            if cur.dirs.get(plist[i]) == None:
                cur.dirs[plist[i]] = Dir()
            cur = cur.dirs[plist[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        plist = filePath.split('/')
        cur = self.root
        # process all but last element
        for i in range(1, len(plist) - 1):
            if cur.dirs.get(plist[i]) == None:
                cur.dirs[plist[i]] = Dir()
            cur = cur.dirs[plist[i]]
        
        pfinal = plist[-1]
        if cur.files.get(pfinal) == None:
            cur.files[pfinal] = content
        else:
            cur.files[pfinal] += content

    def readContentFromFile(self, filePath: str) -> str:
        plist = filePath.split('/')
        cur = self.root
        # process all but last element
        for i in range(1, len(plist) - 1):
            if cur.dirs.get(plist[i]) == None:
                cur.dirs[plist[i]] = Dir()
            cur = cur.dirs[plist[i]]
        
        pfinal = plist[-1]
        return cur.files[pfinal]
