from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from knoteserver.apps.profiles.models import Profile


@receiver(post_save, sender=get_user_model())
def create_related_profile(sender, instance, created, *args, **kwargs):
    """Signal for creating Profile after User creation."""
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)
