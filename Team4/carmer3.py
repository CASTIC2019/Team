from mvnc import mvncapi as mvnc
import sys
import numpy as np
import cv2
import time
import os
def main():
    global gn_mean, gn_labels, actual_frame_height, actual_frame_width, TY_BOX_PROBABILITY_THRESHOLD, TY_MAX_IOU

    #print_info()

    # Set logging level and initialize/open the first NCS we find
    #mvnc.SetGlobalOption(mvnc.GlobalOption.LOG_LEVEL, 0)
    #devices = mvnc.EnumerateDevices()
    #if len(devices) < 2:
        #print('This application requires two NCS devices.')
        #return 1
    """ty_device = mvnc.Device(devices[0])
    ty_device.OpenDevice()

    gn_device = mvnc.Device(devices[1])
    gn_device.OpenDevice()


    #Load tiny yolo graph from disk and allocate graph via API
    try:
        with open(tiny_yolo_graph_file, mode='rb') as ty_file:
            ty_graph_from_disk = ty_file.read()
        ty_graph = ty_device.AllocateGraph(ty_graph_from_disk)
    except:
        print ('Error - could not load tiny yolo graph file')
        ty_device.CloseDevice()
        gn_device.CloseDevice()
        return 1

    #Load googlenet graph from disk and allocate graph via API
    try:
        with open(googlenet_graph_file, mode='rb') as gn_file:
            gn_graph_from_disk = gn_file.read()
        gn_graph = gn_device.AllocateGraph(gn_graph_from_disk)
    except:
        print ('Error - could not load googlenet graph file')
        ty_device.CloseDevice()
        gn_device.CloseDevice()
        return 1

    # GoogLenet initialization
    EXAMPLES_BASE_DIR = '../../'
    gn_mean = np.load(EXAMPLES_BASE_DIR + 'data/ilsvrc12/ilsvrc_2012_mean.npy').mean(1).mean(1)  # loading the mean file

    gn_labels_file = EXAMPLES_BASE_DIR + 'data/ilsvrc12/synset_words.txt'
    gn_labels = np.loadtxt(gn_labels_file, str, delimiter='\t')
    for label_index in range(0, len(gn_labels)):
        temp = gn_labels[label_index].split(',')[0].split(' ', 1)[1]
        gn_labels[label_index] = temp


    # get list of all the .jpg files in the image directory
    input_video_filename_list = os.listdir(input_video_path)
    input_video_filename_list = [i for i in input_video_filename_list if i.endswith('.mp4')]

    if (len(input_video_filename_list) < 1):
        # no images to show
        print('No .mp4 files found')
        return 1

    exit_app = False

    print('Starting GUI, press Q to quit')

    cv2.namedWindow(cv_window_name1)
    #cv2.namedWindow(cv_window_name2)
    #cv2.namedWindow(cv_window_name3)
    cv2.waitKey(1)

    TY_MAX_IOU = 0.15
    TY_BOX_PROBABILITY_THRESHOLD = 0.13"""

    while (True):
        while (True):
            video_device1 = cv2.VideoCapture(0)


            #actual_frame_width1 = video_device1.get(cv2.CAP_PROP_FRAME_WIDTH)
            #actual_frame_height1 = video_device1.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print ('actual video resolution: ' + str(actual_frame_width) + ' x ' + str(actual_frame_height))

            if ((video_device1 == None) or (not video_device1.isOpened())):
                print ('Could not open video device1.  Make sure file exists:')
                #print ('file name:' + input_video_file)
                print ('Also, if you installed python opencv via pip or pip3 you')
                print ('need to uninstall it and install from source with -D WITH_V4L=ON')
                print ('Use the provided script: install-opencv-from_source.sh')
            video_device2 = cv2.VideoCapture(1)

            #actual_frame_width2 = video_device2.get(cv2.CAP_PROP_FRAME_WIDTH)
            #actual_frame_height2 = video_device2.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print ('actual video resolution: ' + str(actual_frame_width) + ' x ' + str(actual_frame_height))

            if ((video_device2 == None) or (not video_device2.isOpened())):
                print ('Could not open video device2.  Make sure file exists:')
                #print ('file name:' + input_video_file)
                print ('Also, if you installed python opencv via pip or pip3 you')
                print ('need to uninstall it and install from source with -D WITH_V4L=ON')
                print ('Use the provided script: install-opencv-from_source.sh')
            video_device3 = cv2.VideoCapture(2)

            #actual_frame_width3 = video_device3.get(cv2.CAP_PROP_FRAME_WIDTH)
            #actual_frame_height3 = video_device3.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print ('actual video resolution: ' + str(actual_frame_width) + ' x ' + str(actual_frame_height))

            if ((video_device3 == None) or (not video_device3.isOpened())):
                print ('Could not open video device3.  Make sure file exists:')
                #print ('file name:' + input_video_file)
                print ('Also, if you installed python opencv via pip or pip3 you')
                print ('need to uninstall it and install from source with -D WITH_V4L=ON')
                print ('Use the provided script: install-opencv-from_source.sh')

            frame_count = 0
            start_time = time.time()

            while True :
                # Read image from video device,
                ret_val1, input_image1 = video_device1.read()
                if (not ret_val1):
                    #end_time = time.time()
                    print("No image from from video device1, exiting")
                    break
                ret_val2, input_image2 = video_device2.read()
                if (not ret_val2):
                    end_time = time.time()
                    print("No image from from video device2, exiting")
                    break
                ret_val3, input_image3 = video_device3.read()
                if (not ret_val3):
                    end_time = time.time()
                    print("No image from from video device3, exiting")
                    break


               """ # resize image to network width and height
                # then convert to float32, normalize (divide by 255),
                # and finally convert to float16 to pass to LoadTensor as input
                # for an inference
                #input_image1 = cv2.resize(input_image1, (TY_NETWORK_IMAGE_WIDTH, TY_NETWORK_IMAGE_HEIGHT), cv2.INTER_CUBIC)
                #ret1=cv2.resize(input_image1,(300,100),cv2.INTER_LINEAR)
                #ret2=cv2.resize(input_image2,(300,100),cv2.INTER_LINEAR)
                #ret3=cv2.resize(input_image3,(300,100),cv2.INTER_LINEAR)
                #input_image[0:100,0:300]=ret1[0:100,0:300]
                #input_image[100:200,0:300]=ret2[0:100,0:300]
                #input_image[200:300,0:300]=ret3[0:100,0:300]

                # save a display image as read from video device.
                display_image1 = input_image1.copy()

                # modify input_image for TinyYolo input
                input_image1 = input_image1.astype(np.float32)
                input_image1 = np.divide(input_image1, 255.0)

                # Load tensor and get result.  This executes the inference on the NCS
                ty_graph.LoadTensor(input_image1.astype(np.float16), 'user object')
                output, userobj = ty_graph.GetResult()

                # filter out all the objects/boxes that don't meet thresholds
                filtered_objs = filter_objects(output.astype(np.float32), input_image1.shape[1], input_image1.shape[0])

                get_googlenet_classifications(gn_graph, display_image1, filtered_objs)

                # check if the window is visible, this means the user hasn't closed
                # the window via the X button
                prop_val = cv2.getWindowProperty(cv_window_name1, cv2.WND_PROP_ASPECT_RATIO)
                if (prop_val < 0.0):
                    end_time = time.time()
                    exit_app = True
                    break


                overlay_on_image(display_image1, filtered_objs)

                # resize back to original size so image doesn't look squashed
                # It might be better to resize the boxes to match video dimensions
                # and overlay them directly on the video image returned from video device.
                display_image1 = cv2.resize(display_image1, (TY_NETWORK_IMAGE_WIDTH, TY_NETWORK_IMAGE_HEIGHT),cv2.INTER_CUBIC)"""

                #input_image2 = cv2.resize(input_image2, (448, 448), cv2.INTER_CUBIC)
                #ret1=cv2.resize(input_image1,(300,100),cv2.INTER_LINEAR)
                #ret2=cv2.resize(input_image2,(300,100),cv2.INTER_LINEAR)
                #ret3=cv2.resize(input_image3,(300,100),cv2.INTER_LINEAR)
                #input_image[0:100,0:300]=ret1[0:100,0:300]
                #input_image[100:200,0:300]=ret2[0:100,0:300]
                #input_image[200:300,0:300]=ret3[0:100,0:300]

                # save a display image as read from video device.
                #display_image2 = input_image2.copy()

                # modify input_image for TinyYolo input
                #input_image2 = input_image2.astype(np.float32)
                #input_image2 = np.divide(input_image2, 255.0)

                # Load tensor and get result.  This executes the inference on the NCS
                #ty_graph.LoadTensor(input_image2.astype(np.float16), 'user object')
                #output, userobj = ty_graph.GetResult()

                # filter out all the objects/boxes that don't meet thresholds
                #filtered_objs = filter_objects(output.astype(np.float32), input_image2.shape[1], input_image1.shape[0])

                #get_googlenet_classifications(gn_graph, display_image2, filtered_objs)

                # check if the window is visible, this means the user hasn't closed
                # the window via the X button
                #prop_val = cv2.getWindowProperty(cv_window_name2, cv2.WND_PROP_ASPECT_RATIO)
                #if (prop_val < 0.0):
                    #end_time = time.time()
                    #exit_app = True
                    #break


                #overlay_on_image(display_image2, filtered_objs)

                # resize back to original size so image doesn't look squashed
                # It might be better to resize the boxes to match video dimensions
                # and overlay them directly on the video image returned from video device.
                #display_image2 = cv2.resize(display_image2, (TY_NETWORK_IMAGE_WIDTH, TY_NETWORK_IMAGE_HEIGHT),cv2.INTER_CUBIC)

                #input_image3 = cv2.resize(input_image3, (448, 448), cv2.INTER_CUBIC)
                #ret1=cv2.resize(input_image1,(300,100),cv2.INTER_LINEAR)
                #ret2=cv2.resize(input_image2,(300,100),cv2.INTER_LINEAR)
                #ret3=cv2.resize(input_image3,(300,100),cv2.INTER_LINEAR)
                #input_image[0:100,0:300]=ret1[0:100,0:300]
                #input_image[100:200,0:300]=ret2[0:100,0:300]
                #input_image[200:300,0:300]=ret3[0:100,0:300]

                # save a display image as read from video device.
                #display_image3 = input_image3.copy()

                # modify input_image for TinyYolo input
                #input_image3 = input_image3.astype(np.float32)
                #input_image3 = np.divide(input_image3, 255.0)

                # Load tensor and get result.  This executes the inference on the NCS
                #ty_graph.LoadTensor(input_image3.astype(np.float16), 'user object')
                #output, userobj = ty_graph.GetResult()

                # filter out all the objects/boxes that don't meet thresholds
                #filtered_objs = filter_objects(output.astype(np.float32), input_image3.shape[1], input_image1.shape[0])

                #get_googlenet_classifications(gn_graph, display_image3, filtered_objs)

                # check if the window is visible, this means the user hasn't closed
                # the window via the X button
                #prop_val = cv2.getWindowProperty(cv_window_name3, cv2.WND_PROP_ASPECT_RATIO)
                #if (prop_val < 0.0):
                    #end_time = time.time()
                    #exit_app = True
                    #break


                #overlay_on_image(display_image3, filtered_objs)

                # resize back to original size so image doesn't look squashed
                # It might be better to resize the boxes to match video dimensions
                # and overlay them directly on the video image returned from video device.
                #display_image3 = cv2.resize(display_image3, (TY_NETWORK_IMAGE_WIDTH, TY_NETWORK_IMAGE_HEIGHT),cv2.INTER_CUBIC)
                # update the GUI window with new image
                #ret_val2, input_image2 = video_device2.read()
                #if (not ret_val2):
                    #end_time = time.time()
                    #print("No image from from video device2, exiting")
                    #break
                #ret_val3, input_image3 = video_device3.read()
                #if (not ret_val3):
                    #end_time = time.time()
                    #print("No image from from video device3, exiting")
                    #break

                cv2.imshow("kk", input_image1)
                cv2.imshow("cv_window_name2", input_image2)
                cv2.imshow("cv_window_name3", input_image3)


                raw_key = cv2.waitKey(1)
                if (raw_key != -1):
                    if (handle_keys(raw_key) == False):
                        end_time = time.time()
                        exit_app = True
                        break

                #frame_count = frame_count + 1

            #frames_per_second = frame_count / (end_time - start_time)
           # print ('Frames per Second: ' + str(frames_per_second))

            # close video device
            video_device1.release()
            video_device2.release()
            video_device3.release()
if __name__ == "__main__":
    sys.exit(main())

