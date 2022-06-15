import port_sweeper
scan = True

while scan:
    correct_values = False

    ip = input("What is the ip of the server : ")
    bottom_port = input("From what port do you want to start scanning from : ")
    range = input("How many ports above {} should be scanned : ".format(bottom_port))
    threads = input("How many threads should be used : ")
    path = input("Path to the output file (don't forget the file extension) : ")

    try:
        bottom_port = int(bottom_port)
        range = int(range)
        threads = int(threads)

        correct_values = True
    except ValueError as ve:
        print("A value that needed to be numerical wasn't. Try again")
    
    if correct_values:
        sweeper = port_sweeper.Sweeper(ip, bottom_port, range, threads, path)
        sweeper.start()
        print("Done! ip and ports have been export to {}".format(path))

    again_prompt = input("Scan another ip? (y/n) : ")

    print(again_prompt.lower())
    if again_prompt.lower() != "y":
        scan = False
