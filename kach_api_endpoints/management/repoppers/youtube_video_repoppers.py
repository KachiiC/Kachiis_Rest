import json
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo


def create_new_youtube_videos(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)
        for item in data["items"]:
            YoutubeVideo(
                video_title=item["snippet"]["title"],
                video_id=item["snippet"]["resourceId"]["videoId"],
                video_description=item["snippet"]["description"],
                upload_date=item["snippet"]["publishedAt"],
                video_thumbnail=item["snippet"]["thumbnails"]["maxres"]["url"],
                playlist_id=item["snippet"]["playlistId"],
                channel_id=item["snippet"]["channelId"]
            ).save()
