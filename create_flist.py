#!/usr/bin/python

import argparse
import os
from random import shuffle
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', default='/vgldb1/LightStageFaceDB/Datasets/FaceEncoding/AlbedoAugmentation', type=str,
                    help='The folder path')
parser.add_argument('--train_filename', default='/mount/Users/zli/gen_inpainting_data/data_flist/lightstage_train_shuffled.flist', type=str,
                    help='The output filename.')
#parser.add_argument('--validation_filename', default='/mount/Users/zli/gen_inpainting_data/data_flist/validation_shuffled.flist', type=str,
#                    help='The output filename.')
parser.add_argument('--is_shuffled', default='1', type=int,
                    help='Needed to shuffle')

if __name__ == "__main__":

    args = parser.parse_args()

    # get the list of directories
    flist = os.listdir(args.folder_path)
    flist = glob.glob(os.path.join(args.folder_path, '*.exr'))
    #dirs_name_list = []

    # make 2 lists to save file paths
    training_file_names = []
    #validation_file_names = []

    # print all directory names
    for img_fname in flist:
        
        training_item = os.path.join(args.folder_path, img_fname)
        
        training_file_names.append(training_item)

    for i in training_file_names:
        print(i)
#    for i in validation_file_names:
#        print(i)

    # This would print all the files and directories

    # shuffle file names if set
    if args.is_shuffled == 1:
        shuffle(training_file_names)
        #shuffle(validation_file_names)

    # make output file if not existed
    if not os.path.exists(args.train_filename):
        os.mknod(args.train_filename)

#    if not os.path.exists(args.validation_filename):
#        os.mknod(args.validation_filename)

    # write to file
    fo = open(args.train_filename, "w")
    fo.write("\n".join(training_file_names))
    fo.close()

#    fo = open(args.validation_filename, "w")
#    fo.write("\n".join(validation_file_names))
#    fo.close()

    # print process
    print("Written file is: ", args.train_filename, ", is_shuffle: ", args.is_shuffled)