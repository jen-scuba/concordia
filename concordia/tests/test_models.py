from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from concordia.models import Campaign, Transcription, UserProfileActivity
from concordia.utils import get_anonymous_user

from .utils import CreateTestUsers, create_asset, create_transcription


class AssetTestCase(CreateTestUsers, TestCase):
    def setUp(self):
        self.asset = create_asset()
        anon = get_anonymous_user()
        create_transcription(asset=self.asset, user=anon)
        create_transcription(
            asset=self.asset,
            user=self.create_test_user(username="tester"),
            reviewed_by=anon,
        )

    def test_get_contributor_count(self):
        self.assertEqual(self.asset.get_contributor_count(), 2)


class TranscriptionManagerTestCase(CreateTestUsers, TestCase):
    def test_recent_review_actions(self):
        transcription1 = create_transcription(
            user=self.create_user(username="tester1"),
            rejected=timezone.now() - timedelta(days=2),
        )
        transcription2 = create_transcription(
            asset=transcription1.asset, user=get_anonymous_user()
        )
        transcriptions = Transcription.objects
        self.assertEqual(transcriptions.recent_review_actions().count(), 0)
        transcription1.accepted = timezone.now()
        transcription1.save()
        self.assertEqual(transcriptions.recent_review_actions().count(), 1)
        transcription2.rejected = timezone.now()
        transcription2.save()
        self.assertEqual(transcriptions.recent_review_actions().count(), 2)


class UserProfileActivityTestCase(TestCase):
    def setUp(self):
        self.user_profile_activity = UserProfileActivity(
            campaign=Campaign(), transcribe_count=135, review_count=204
        )

    def test_get_status(self):
        self.user_profile_activity.campaign.status = Campaign.Status.ACTIVE
        self.assertEqual(self.user_profile_activity.get_status(), "Active")
        self.user_profile_activity.campaign.status = Campaign.Status.COMPLETED
        self.assertEqual(self.user_profile_activity.get_status(), "Completed")
        self.user_profile_activity.campaign.status = Campaign.Status.RETIRED
        self.assertEqual(self.user_profile_activity.get_status(), "Retired")

    def test_total_actions(self):
        self.assertEqual(self.user_profile_activity.total_actions(), 339)
