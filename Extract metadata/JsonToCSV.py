import io
import os
import json
import zipfile


new_name = 'ShakeFive2.metadata.csv'

def zipFileIter(filename):
    import zipfile
    with zipfile.ZipFile(filename) as zipfile:
        for zippedfilename in zipfile.namelist():
            print(zippedfilename)
            yield zippedfilename, zipfile.open(name=zippedfilename).read()



def get_csv_from_video(opencv_storage):
    total = ""
    for frame_index, frame_data in enumerate(opencv_storage["opencv_storage"]['video']['frames'].items()):
        frame_key, frame = frame_data
        if int(frame['skeletons_amount']) > 0:
            line = ['None' for i in range(87)]
            line[0] = opencv_storage["opencv_storage"]['video']['id']
            line[1] = frame_index
            line[2] = frame['id']
            line[3] = frame['timestamp']
            line[4] = opencv_storage["opencv_storage"]['video']['image_data']['path']
            offset = 5
            for skeleton_index, skeleton in enumerate(frame['skeletons'].items()):
                skeleton_key, skeleton = skeleton
                skeleton['joints_amount'] = int(skeleton['joints_amount'])
                # if int(skeleton['joints_amount']) > 0:
                for joint_key, joint in skeleton['joints'].items():
                    p1, p2, p3 = joint['point3Dd']
                    o1, o2 = joint['point2Dd']
                    line[offset] = p1
                    line[offset+1] = p2
                    line[offset+2] = p3
                    line[offset+3] = o1
                    line[offset+4] = o2
                    offset += 5

                if skeleton_index == 0:
                    line[45] = skeleton['action_name']
                    offset += 1
                else:
                    line[-1] = skeleton['action_name']

            line = [str(i) for i in line]
            total += ",".join(line[:]) + "\n"
    return total

mf = io.BytesIO()
final_csv = "VideoID,FameNumber,FrameID,timestamp,VideoName,S0ShoulderLeft3Dx,S0ShoulderLeft3Dy,S0ShoulderLeft3Dz,S0ShoulderLeft2Dx,S0ShoulderLeft2Dz,S0ElbowLeft3Dx," \
            "S0ElbowLeft3Dy,S0ElbowLeft3Dz,S0ElbowLeft2Dx,S0ElbowLeft2Dz,S0WristLeft3Dx,S0WristLeft3Dy,S0WristLeft3Dz,S0WristLeft2Dx,S0WristLeft2Dz,S0ShoulderRight3Dx,S0ShoulderRight3Dy,S0ShoulderRight3Dz,S0ShoulderRight2Dx,S0ShoulderRight2Dz,S0ElbowRight3Dx,S0ElbowRight3Dy,S0ElbowRight3Dz,S0ElbowRight2Dx,S0ElbowRight2Dz,S0WristRight3Dx,S0WristRight3Dy,S0WristRight3Dz,S0WristRight2Dx,S0WristRight2Dz,S0ThumbLeft3Dx,S0ThumbLeft3Dy,S0ThumbLeft3Dz,S0ThumbLeft2Dx,S0ThumbLeft2Dz,S0ThumbRight3Dx,S0ThumbRight3Dy,S0ThumbRight3Dz,S0ThumbRight2Dx,S0ThumbRight2Dz,S0ActionName,S1ShoulderLeft3Dx,S1ShoulderLeft3Dy,S1ShoulderLeft3Dz,S1ShoulderLeft2Dx,S1ShoulderLeft2Dz,S1ElbowLeft3Dx,S1ElbowLeft3Dy,S1ElbowLeft3Dz,S1ElbowLeft2Dx,S1ElbowLeft2Dz,S1WristLeft3Dx,S1WristLeft3Dy,S1WristLeft3Dz,S1WristLeft2Dx,S1WristLeft2Dz,S1ShoulderRight3Dx,S1ShoulderRight3Dy,S1ShoulderRight3Dz,S1ShoulderRight2Dx,S1ShoulderRight2Dz,S1ElbowRight3Dx,S1ElbowRight3Dy,S1ElbowRight3Dz,S1ElbowRight2Dx,S1ElbowRight2Dz,S1WristRight3Dx,S1WristRight3Dy,S1WristRight3Dz,S1WristRight2Dx,S1WristRight2Dz,S1ThumbLeft3Dx,S1ThumbLeft3Dy,S1ThumbLeft3Dz,S1ThumbLeft2Dx,S1ThumbLeft2Dz,S1ThumbRight3Dx,S1ThumbRight3Dy,S1ThumbRight3Dz,S1ThumbRight2Dx,S1ThumbRight2Dz,S1ActionName\n"



if __name__ == '__main__'
	for index, file in enumerate(zipFileIter('ShakeFive2.metadataJSON.zip')):
	    filename, text = file
	    opencv_storage = json.loads(text)
	    opencv_storage = get_csv_from_video(opencv_storage)
	    final_csv += opencv_storage
	print("Done!\nStarting to write file...",end="")
	with open(new_name, "w+") as output:
	    output.write(final_csv)
	print("done")