def group_by_owners(files):
    owners = {}
    for file in files.keys():
        if files[file] in owners:
            owners[files[file]].append(file)
        else:
            owners[files[file]]=[file]
    return owners

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))