import json
import xmltodict
import io
import os
import zipfile


new_name = 'ShakeFive2.metadataJSON.zip'

def tarFileIter(name):
    import tarfile
    with tarfile.open(name,mode='r:') as tarfile:
        for member in tarfile.members:
            yield member.name, tarfile.extractfile(member.name).read()


def fix_video_json(opencv_storage):
    joint_keywords = ("shoulder", 'elbow', 'wrist', 'thumb')
    for frame_key, frame in opencv_storage["opencv_storage"]['video']['frames'].items():
        if int(frame['skeletons_amount']) > 0:
            for skeleton_key, skeleton in frame['skeletons'].items():
                skeleton['joints_amount'] = int(skeleton['joints_amount'])
                if int(skeleton['joints_amount']) > 0:
                    removed_joints = 0
                    to_pop = []
                    for joint_key, joint in skeleton['joints'].items():
                        joint = json.loads(json.dumps(joint))
                        if not joint['name'].lower().startswith(joint_keywords):
                            to_pop.append(joint_key)
                            removed_joints += 1
                        else:
                            opencv_storage["opencv_storage"]['video']['frames'][frame_key]['skeletons'][skeleton_key]['joints'][joint_key]['point3Dd'] = joint[
                                'point3Dd'].split()
                            opencv_storage["opencv_storage"]['video']['frames'][frame_key]['skeletons'][skeleton_key]['joints'][joint_key]['point2Dd'] = joint[
                                'point2Dd'].split()

                    skeleton['joints_amount'] -= removed_joints

                    # Remove joints that are not related to hands
                    for popper in to_pop:
                        skeleton['joints'].pop(popper)
    return opencv_storage

mf = io.BytesIO()

with zipfile.ZipFile(mf, mode="w",compression=zipfile.ZIP_DEFLATED) as in_memory_zip:
    for index, file in enumerate(tarFileIter('ShakeFive2.metadata.tar')):
        filename, xml = file
        opencv_storage = xmltodict.parse(xml)
        opencv_storage = fix_video_json(opencv_storage)
        if filename.endswith("xml"):
            filename = filename[:-3] + 'json'
        in_memory_zip.writestr(filename, json.dumps(opencv_storage, indent=2))
        # json.dump(opencv_storage, open(filename, "w+"), indent=4)
        print(f'Done file {index}: {filename}')
zippath = os.path.join(os.getcwd(), new_name)

with open(zippath, "w+b") as f:  # use `wb` mode
    f.write(mf.getvalue())
print(f"Zip ready in {zippath}")
# zipper.writetofile(new_name)

#
#


# json.dump(xmltodict.parse(list(xml.values())[0]), open("output.json", "w+"), indent=3)