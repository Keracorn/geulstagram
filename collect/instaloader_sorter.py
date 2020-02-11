import glob
import json
import shutil
import os

# using Instagram's image recognition: it is written on json file, with key of "__typename"
def discern_image_file(keyword):
    # read file list that is previously downloaded through get_it
    read_files_list = glob.glob("#" + keyword + "/*.json")
    print(read_files_list)
    write_files_list = []
    # open every json file, check image type
    # Accessibility caption "Image may contain: text" indicates there's a text inside
    # 글스타그램 image is classified as "GraphImage" through Instagram image recognition
    for json_file_name in read_files_list:
        # open json file
        with open(json_file_name, "r", encoding="UTF8") as data_file:
            # read json file
            data = json.load(data_file)
            file_name = json_file_name[:-5]
            # print(data)
            core_meta_data = data["node"]
            accessibility_caption = core_meta_data.get("accessibility_caption")
            if accessibility_caption:
                if accessibility_caption == "Image may contain: text":
                    print(file_name + " is corresponding image")
                    write_files_list.append(file_name)
                else:
                    pass
            elif core_meta_data["__typename"] == "GraphImage":
                print(file_name + " is corresponding image")
                write_files_list.append(file_name)
            else:
                print(file_name + " is uncertain")
                pass
    # print(write_files_list)
    return write_files_list


def sort_and_move_image_file(keyword):
    # change the source directory to your project directory
    # source = '/path/to/source_folder'
    source = "./"
    dest = "./" + "#" + keyword + "_sorted"
    os.mkdir(dest)

    all_image_file_list = glob.glob("#" + keyword + "/*.jpg")
    write_files_list = discern_image_file(keyword)
    print(all_image_file_list)
    print(write_files_list)
    for item in write_files_list:
        matching_list = [s for s in all_image_file_list if item in s]
        print(matching_list)
        for matching_item in matching_list:
            print(matching_item)
            shutil.move(source + matching_item, dest)


# discern image files only
# discern_image_file("글스타그램")

# discern, sort, and move image files to separate directory
sort_and_move_image_file("글스타그램")
