from sys import argv, exit
from os.path import exists


script, original_file, new_file = argv

print "Copying from {original} to {new}".format(original=original_file, new=new_file)

with open(original_file) as of:
    print "The original file contains the following:"
    data = of.read()
    print data

    existence = "exists" if exists(new_file) else "doesn't exist."
    print "The file you are copying to {existence}.".format(existence=existence)

    if exists(new_file):
        with open(new_file) as nf:
            print "The file you would overwrite currently contains the following:"
            print nf.read()

    resume = raw_input("Do you want to continue? (y/n)")

    if resume.lower() == 'y':
        pass
    elif resume.lower() == 'n':
        exit()
    else:
        print "That wasn't one of the options. Going to stop just in case."
        exit()

    with open(new_file, 'w') as nf:
        nf.write(data)

    with open(new_file) as nf:
        print "The file you overwrote now contains the following:"
        print nf.read()

print "Alright, all done."
