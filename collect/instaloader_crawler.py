import instaloader
import glob

# download pictures, download json file, but don't compress json file.
L = instaloader.Instaloader(
    download_pictures=True,
    download_video_thumbnails=False,
    download_videos=False,
    download_geotags=True,
    download_comments=False,
    save_metadata=True,
    compress_json=False,
)

# two arguments: keyword and number of files
def get_it(keyword, numbers_of_files):
    # Get instance
    while numbers_of_files > 0:
        for post in L.get_hashtag_posts(keyword):
            # post is an instance of instaloader.Post
            L.download_post(post, target="#" + keyword)
            numbers_of_files -= 1
            # print(numbers_of_files)
            if numbers_of_files == 0:
                break
        print("loop ended for " + keyword)


def combine_txt_file(exercise_name):
    read_files = glob.glob("#" + exercise_name + "/*.txt")

    with open("#" + exercise_name + "_sum.txt", "w", encoding="utf-8") as outfile:
        for f in read_files:
            with open(f, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())


# sample function
get_it("글스타그램", 50)
