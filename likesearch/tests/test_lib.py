from unittest import TestCase

from ..lib import Like, search_likes, get_oldest_like


class LikeTests(TestCase):
    def test_url(self):
        # Given
        like = Like(id=5, text="", user_handle="me_twitter")

        # When
        url = like.url

        # Then
        self.assertEqual(url, "https://twitter.com/me_twitter/status/5")

    def test_str(self):
        # Given
        like = Like(id=5, text="hello from tests", user_handle="me_twitter")

        # When
        string = str(like)

        # Then
        self.assertEqual(
            string,
            '"hello from tests" by me_twitter at https://twitter.com/me_twitter/status/5',
        )


class SearchLikesTests(TestCase):
    def test_SearchLikes_NoLikes_ReturnEmptyList(self):
        # Given
        likes = []

        # When
        matching_likes = search_likes(likes, "query")

        # Then
        self.assertEqual(0, len(matching_likes))

    def test_SearchLikes_MatchExists_ReturnMatch(self):
        # Given
        likes = [Like(id=2, text="one about hockey", user_handle="")]

        # When
        matching_likes = search_likes(likes, "hockey")

        # Then
        self.assertEqual(1, len(matching_likes))

    def test_SearchLikes_CaseInsentitiveMatch_ReturnMatch(self):
        # Make sure case doesn't matter
        # Given
        likes = [
            Like(id=1, text="one about HOCKEY", user_handle=""),
            Like(id=2, text="one about hockey", user_handle=""),
        ]

        # When
        matching_likes = search_likes(likes, "hockey")

        # Then
        self.assertEqual(2, len(matching_likes))

    def test_SearchLikes_NoMatches_ReturnEmptyList(self):
        # Given
        likes = [
            Like(id=1, text="one about hockey", user_handle=""),
            Like(id=2, text="one about baseball", user_handle=""),
            Like(id=3, text="one about basketball", user_handle=""),
        ]

        # When
        matching_likes = search_likes(likes, "football")

        # Then
        self.assertEqual(0, len(matching_likes))


class GetOldestLikeTests(TestCase):
    def test_GetOldestLike__ReturnLikeWithSmallestId(self):
        # Given
        likes = [
            Like(id=1, text="one about hockey", user_handle=""),
            Like(id=2, text="one about baseball", user_handle=""),
            Like(id=3, text="one about basketball", user_handle=""),
        ]

        # When
        oldest = get_oldest_like(likes)

        # Then
        self.assertEqual(1, oldest.id)

    def test_GetOldestLike_NoLikes_ReturnNone(self):
        # Given
        likes = []

        # When
        oldest = get_oldest_like(likes)

        # Then
        self.assertIsNone(oldest)
