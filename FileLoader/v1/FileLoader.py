#This script has been generated by Peach Generator 1.
#Rerunning Peach Generator on this script will lead to a loss of your added python code.

def start(c, list_file, URI):
    import ServiceUtility
    import os
    import shutil

    ServiceUtility.info(c, "Starting FileLoader")
    

    output = ""
    output_file_name = ""
    unique_output_dir = None

    if list_file is None:
        ServiceUtility.info(c, "No input archive file was given. The URI parameter value \"{}\" will be used instead.".format(URI))
        output, output_file_name = generate_file_direct(c, URI)
    else:
        ServiceUtility.info(c, "Input archive file was given... Reading out archive file...")
        unique_output_dir = generate_unique_output_dir()
        l = ""
        with open(list_file, 'r') as list_file_f:
            l = list_file_f.read().split('\n')
        output, output_file_name = generate_file_archive(c, l, unique_output_dir)
    
    
    

    #your output ports as output files


    availableFiles = ServiceUtility.make_available(c, [[output, output_file_name]])

    ServiceUtility.info(c, "Transferring file '{}' to next service".format(output_file_name))
    
    if unique_output_dir is not None:
        shutil.rmtree(unique_output_dir)

    return availableFiles

def generate_file_direct(c, URI):
    import ServiceUtility
    ServiceUtility.info(c, "Downloading contents of URI '{}'...".format(URI))
    output_file, output_file_name = ServiceUtility.from_uri(URI)
    ServiceUtility.info(c, "Saved into file '{}'".format(output_file_name))
    return output_file, output_file_name

def generate_file_archive(c, URIs, output_dir):
    import os
    s = ""
    for URI in URIs:
        s += generate_file_direct(c, URI)[0] + "\n"
    
    output_file = os.path.join(output_dir, "archive.txt")
    with open(output_file, "w") as output_file_f:
        output_file_f.write(s)

    return output_file, "archive.txt"

def generate_unique_output_dir():
    import time
    import os
    unique_relative_output_dir = "output_" + str(time.time()).replace(".", "")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    unique_output_dir = os.path.join(dir_path, unique_relative_output_dir)
    os.makedirs(unique_output_dir)
    return unique_output_dir