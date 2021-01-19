import json
from kach_api_endpoints.api_list.instagram_api.instagram_model import Post


def create_insta_data(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for media in data["collector"]:
            if media["type"] == "GraphImage":
                display_media = media["display_url"]
                media_views = 0
            elif media["type"] == "GraphVideo":
                display_media = media["video_url"]
                media_views = media["views"]
            Post(
                media=display_media,
                user=media["owner"]["username"],
                user_id=media["owner"]["id"],
                post_link=media["shortcode"],
                caption=media["description"],
                type=media["type"],
                time_stamp=media["taken_at_timestamp"],
                thumbnail=media["thumbnail_src"],
                likes=media["likes"],
                views=media_views,
            ).save()
