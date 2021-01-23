import json
from kach_api_endpoints.api_list.instagram_api.instagram_model import Post


def create_insta_data(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for item in data["edges"]:
            media = item["node"]

            if media["__typename"] == "GraphImage":
                display_media = media["display_url"]
            elif media["__typename"] == "GraphVideo":
                display_media = media["video_url"]

            Post(
                media=display_media,
                user=media["owner"]["username"],
                user_id=media["owner"]["id"],
                post_link=media["shortcode"],
                caption=media["edge_media_to_caption"]["edges"][0]["node"]["text"],
                type=media["__typename"],
                time_stamp=media["taken_at_timestamp"],
                thumbnail=media["thumbnail_src"],
                likes=media["edge_media_preview_like"]["count"],
            ).save()
