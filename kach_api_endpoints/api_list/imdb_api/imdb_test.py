from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from kach_api_endpoints.api_list.imdb_api.imdb_model import Content, ImdbList
from kach_api_endpoints.api_list.imdb_api.imdb_serializer import ImdbListSerializer


class ImdbTest(APITestCase):
    imdb_endpoint = reverse("imdb_lists")

    content_1 = Content(
        title="Oasis",
        imdb_id="tt0320907",
        content_type="popular_tv_shows",
        media_type="TV shows",
        release_date=2020
    )

    content_2 = Content(
        title="Wizards",
        imdb_id="tt7736558",
        content_type="trending_tv_shows",
        media_type="TV shows",
        release_date=2020
    )

    content_3 = Content(
        title="Welcome to Sudden Death",
        imdb_id="tt10804786",
        content_type="popular_movies",
        media_type="Movies",
        release_date=2020
    )

    content_4 = Content(
        title="Triggered",
        imdb_id="tt9419976",
        content_type="trending_movies",
        media_type="Movies",
        release_date=2020
    )

    imdb_list_1 = ImdbList(
        list_title="Popular Movies",
        content_type="popular_movies",
        media_type="Movies"
    )

    imdb_list_2 = ImdbList(
        list_title="Popular TV Shows",
        content_type="popular_tv_shows",
        media_type="TV shows"
    )

    imdb_list_3 = ImdbList(
        list_title="Trending Movies",
        content_type="trending_movies",
        media_type="Movies"
    )

    imdb_list_4 = ImdbList(
        list_title="Trending TV Shows",
        content_type="trending_tv_shows",
        media_type="TV shows"
    )

    expected_content = [content_1, content_2, content_3, content_4]
    expected_imdb_list = [imdb_list_1, imdb_list_2, imdb_list_3, imdb_list_4]

    def setUp(self):
        for obj in self.expected_content:
            obj.save()

        for obj in self.expected_imdb_list:
            obj.save()

    def test_get_all_lists(self):

        single_list_endpoint = reverse('single_imdb_list', args=[self.imdb_list_1.content_type])

        imdb_list = ImdbList.objects.get(content_type=self.imdb_list_1.content_type)

        serializer = ImdbListSerializer(imdb_list)

        response = self.client.get(single_list_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_getting_single_list(self):
        serializer = ImdbListSerializer(self.expected_imdb_list, many=True)

        response = self.client.get(self.imdb_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_adding_content_to_list(self):
        all_content = Content.objects.all()
        all_imdb_list = ImdbList.objects.all()

        for media in all_content:
            for imdb_list in all_imdb_list:
                if media.content_type == imdb_list.content_type:
                    correct_content_type = ImdbList.objects.get(content_type=media.content_type)
                    correct_content_type.content.add(media)

        popular_movies = ImdbList.objects.get(list_title="Popular Movies")
        popular_tv_shows = ImdbList.objects.get(list_title="Popular TV Shows")
        trending_movies = ImdbList.objects.get(list_title="Trending Movies")
        trending_tv_shows = ImdbList.objects.get(list_title="Trending TV Shows")

        assert popular_movies.content.count() == 1
        assert popular_tv_shows.content.count() == 1
        assert trending_movies.content.count() == 1
        assert trending_tv_shows.content.count() == 1
