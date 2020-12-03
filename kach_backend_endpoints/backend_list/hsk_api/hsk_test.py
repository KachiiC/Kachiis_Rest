from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from kach_backend_endpoints.backend_list.hsk_api.hsk_model import Word, HSKLevel
from kach_backend_endpoints.backend_list.hsk_api.hsk_serializers import WordSerializer, HSKLevelSerializer


class HskTest(APITestCase):
    hsk_words_endpoint = reverse("hsk_words")

    word_1 = Word(
        chinese_characters="大",
        pinyin="dà",
        definition="big, large",
        type="adjective",
        hsk_level=1
    )

    word_2 = Word(
        chinese_characters="真",
        pinyin="zhēn",
        definition="really",
        type="adverb",
        hsk_level=2
    )

    word_3 = Word(
        chinese_characters="蓝",
        pinyin="lán",
        definition="blue",
        type="adjective",
        hsk_level=3
    )

    hsk_1 = HSKLevel(
        level=1
    )

    hsk_2 = HSKLevel(
        level=2
    )

    hsk_3 = HSKLevel(
        level=3
    )

    expected_words = [word_1, word_2, word_3]
    expected_hsk = [hsk_1, hsk_2, hsk_3]

    def setUp(self):
        for obj in self.expected_words:
            obj.save()
        for obj in self.expected_hsk:
            obj.save()

    def test_add_word_to_hsk_level(self):
        """test words to levels"""
        words = Word.objects.all()
        all_levels = HSKLevel.objects.all()

        for word in words:
            for hsk_level in all_levels:
                if word.hsk_level == hsk_level.level:
                    correct_level = HSKLevel.objects.get(level=word.hsk_level)
                    correct_level.words.add(word)

        level_1 = HSKLevel.objects.get(level=1)
        level_2 = HSKLevel.objects.get(level=2)
        level_3 = HSKLevel.objects.get(level=3)

        assert level_1.words.count() == 1
        assert level_2.words.count() == 1
        assert level_3.words.count() == 1

    def test_get_all_words(self):
        """test getting all words"""
        serializer = WordSerializer(self.expected_words, many=True)

        response = self.client.get(self.hsk_words_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_get_single_word(self):
        """ Retrieve an existing words"""
        word_endpoint = reverse('hsk_single_word', args=[self.word_2.chinese_characters])

        word = Word.objects.get(chinese_characters=self.word_2.chinese_characters)

        serializer = WordSerializer(word)

        response = self.client.get(word_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data
