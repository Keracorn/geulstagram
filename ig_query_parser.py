from urllib.parse import urlparse

key_url = "https://www.instagram.com/p/B2X3I0InR6C/"

def get_ig_key(key_url):
    if key_url:
        query_list = urlparse(key_url)
        print(query_list)
        key_query = query_list.path
        print(key_query)
        id_list = query_list.path.split('/')
        print(id_list)
        ig_id = id_list[2]
        print(ig_id)
        return ig_id
    else:
        raise ValueError

get_ig_key(key_url)
