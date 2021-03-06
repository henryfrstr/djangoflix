from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from .models import Video, PublishedStateOptions


class VideoModelTestCase(TestCase):
    def setUp(self):
        self.obj_a = Video.objects.create(
            title='This is my title', video_id="abc")
        self.obj_b = Video.objects.create(title='This is my title',
                                          state=PublishedStateOptions.PUBLISH, video_id="abcd")

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)

    def test_valid_title(self):
        title = 'This is my title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishedStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Video.objects.filter(state=PublishedStateOptions.PUBLISH)
        published_qs = Video.objects.filter(
            state=PublishedStateOptions.PUBLISH,
            publish_timestamp__lte=timezone.now())
        self.assertTrue(published_qs.exists())

    def test_publish_manager(self):
        published_qs = Video.objects.published()
        self.assertTrue(published_qs.exists())
