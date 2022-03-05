# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

MOVIES = 'movies'
IMAGES = 'images'
MUSIC = 'music'


def get_type_by_extention(extention):
    file_type_dict = {
        'mp3': MUSIC, 'aac': MUSIC, 'flac': MUSIC,
        'jpg': IMAGES, 'bmp': IMAGES, 'gif': IMAGES,
        'mp4': MOVIES, 'avi': MOVIES, 'mkv': MOVIES
    }
    if extention in file_type_dict:
        return file_type_dict[extention]
    return 'other'


def get_extention_by_filename(file_name):
    file_name_list = file_name.split(".")
    return file_name_list[-1]


def get_size(file_size):
    return int(file_size.replace("b", ""))


def make_str_file_size(file_size):
    return "".join([str(file_size), 'b'])


def make_str_result(file_type, file_size_str):
    return " ".join([str(file_type), file_size_str])


def solution(S):
    # write your code in Python 3.6

    music_total_size = 0
    images_total_size = 0
    movies_total_size = 0
    other_total_size = 0

    for line in S.split("\n"):
        file_name, file_size = line.split(" ")
        file_type = get_type_by_extention(get_extention_by_filename(file_name))

        if file_type == MUSIC:
            music_total_size += get_size(file_size)
        elif file_type == MOVIES:
            movies_total_size += get_size(file_size)
        elif file_type == IMAGES:
            images_total_size += get_size(file_size)
        else:
            other_total_size += get_size(file_size)

    return "\n".join([
        make_str_result(MUSIC, make_str_file_size(music_total_size)),
        make_str_result(IMAGES, make_str_file_size(images_total_size)),
        make_str_result(MOVIES, make_str_file_size(movies_total_size)),
        make_str_result('other', make_str_file_size(other_total_size))
    ])

