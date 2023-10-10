my_file_system = {
    "penut/": {
        "sub-dir/": {
            
        },
        "sub-dir2/": {
            "hello.txt":""
        }
    },
}
project_file_system = {
    "penut/": {
        "sub-dir/": {
            "hello.txt":""
        },
        "sub-dir2/": {
        }
    },
    "second_dir/": {
        "what/": {
            "who/": {
                
            }
        }
    },
    "yell/": {
        "use/": {
            "in/": {
                "on/": {
                    "helloin2on3.txt": ""
                },
                "on2/": {
                    "hello2.txt": ""
                }
            },
            "in2/": {
                "on3/": {
                    "hello.txt": ""
                }
            }
        }
    },
    "a_file.txt":''
    #any dicts that are added start here
    #always make sub_dict which reference the dict behind it for cd..
}
def isDirectory(name):
    return name[-1] == "/"

def locate(find_name, cur_dir):
    list_of_paths = []
    for key in cur_dir.keys():
        if isDirectory(key):
            path = locate(find_name, cur_dir[key])
            for file in path:
                list_of_paths.append(key+file)
        else:
            if find_name == key:
                list_of_paths.append(find_name)

    return list_of_paths

"""
first run:
find_name = "hello.txt"
cur_dir = {
        "what/": {
            "who/": {
                
            }
        }
    }

list_of_paths = []

for key in [what]:
    ## loop 1
    if isDirectory(what) ## True
        path = locate("hello.txt", --sub call-- {
            "who/": {
                
            }
        })
        
        

    first run iteration one:
        find 





"""



# First run
# find_name = hello.tct
# cur_dir = {
    #     "sub-dir/": {
            
    #     },
    #     "sub-dir2/": {
    #         "hello.txt":""
    #     }
    # },
# Loop 1
# . Key = sub_dir/
# isDir = True
# path = locate("hello.txt", {})

# Sub run
    # cur_dir = {}
    # for key in []:
    #     pass

def main():
    find_file = locate("hello.txt", project_file_system)
    if find_file:
        for i in find_file:
            print(i)
    else:
        print("No files were found.")

if __name__ == "__main__":
    main()
