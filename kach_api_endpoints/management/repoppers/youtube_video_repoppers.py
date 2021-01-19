import json
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo


def create_new_youtube_videos(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for item in data["items"]:
            clip = item["snippet"]

            description_crop = clip["description"].split("\n\n")[0]

            clip_words = clip["title"].split(" ")

            for word in clip_words:
                if word == "vs" or word == "v":
                    x = range(-2, 3)
                    my_title = []
                    for n in x:
                        my_title.append(clip_words[clip_words.index(word) + n])

                    my_title.pop(2)
                    my_title.insert(2, "vs")
                    display_title = " ".join(my_title)

            YoutubeVideo(
                video_title=display_title,
                video_id=clip["resourceId"]["videoId"],
                video_description=description_crop,
                upload_date=clip["publishedAt"],
                video_thumbnail=clip["thumbnails"]["maxres"]["url"],
                playlist_id=clip["playlistId"],
                channel_id=clip["channelId"]
            ).save()
