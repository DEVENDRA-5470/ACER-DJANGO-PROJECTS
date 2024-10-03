from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Stats
from django.contrib.auth.signals import user_logged_in

# Create profile when user is created, excluding superusers
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:  # Exclude superusers
        profile = Profile.objects.create(user=instance)
        Stats.objects.create(profile=profile)  # Create stats for the profile

# Save the profile and stats when user is updated, excluding superusers
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_superuser:  # Exclude superusers
        instance.profile.save()
        instance.profile.stats.save()  # Save the associated stats as well


@receiver(user_logged_in)
def update_login_count(sender, request, user, **kwargs):
    if not user.is_superuser:  # Exclude superusers
        user_profile = Profile.objects.get(user=user)
        stats, created = Stats.objects.get_or_create(profile=user_profile)
        
        # Increment total logins
        if stats.total_logins is None:
            stats.total_logins = 0
        stats.total_logins += 1
        stats.save()