from sys import argv

script, filename = argv

write_file = True
while write_file == True:
    print "You entered {!r} as the file we will work with. If we continue, it will be erased.".format(filename)

    with open(filename) as f:
        print "The file currently contains the following:"
        print f.read()

    resume = raw_input("Do you want to continue? (y/n)")

    if resume.lower() == 'y':
        pass
    elif resume.lower() == 'n':
        write_file = False
        continue
    else:
        print "That wasn't one of the options. Let's start over."
        continue

    print "Opening the file..."
    with open(filename, 'w+') as f:
        print "Enter the text you would like to write:"
        text = ''
        for line in iter(raw_input, ''):
            text = '\n'.join([text, line])

        print "I'm going to write these to the file."

        f.write(text)

    with open(filename) as f:
        print "Now let's read it to make sure you input what you intended to."
        print f.read()

    try_again = raw_input("Do you want to try again? (y/n)")

    if try_again.lower() == 'y':
        continue
    elif try_again.lower() == 'n':
        write_file = False
    else:
        print "That wasn't one of the options. Let's start over."
        continue
