#This script has been generated by Peach Generator 1.
#Rerunning Peach Generator on this script will lead to a loss of your added python code.

def start(c, fixed_img_in, floatimg_img_in, Threshold):
    import ServiceUtility
    import os
    import time
    import shutil
    unique_relative_output_dir = "output_" + str(time.time()).replace(".", "")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    unique_output_dir = os.path.join(dir_path, unique_relative_output_dir)
    os.makedirs(unique_output_dir)

    #your output ports as output files

    xform_out_filename = "xform_out.???"
    xform_out = os.path.join(unique_output_dir, xform_out_filename)
    with open(xform_out, "w") as xform_out_f:
        xform_out_f.write("This is the output of port \"xform_out\"")

    image_out_filename = "image_out.???"
    image_out = os.path.join(unique_output_dir, image_out_filename)
    with open(image_out, "w") as image_out_f:
        image_out_f.write("This is the output of port \"image_out\"")

    print "Running RigidRegistration"
    availableFiles = ServiceUtility.make_available(c, [[xform_out, xform_out_filename], [image_out, image_out_filename]])
    shutil.rmtree(unique_output_dir)
    return availableFiles
