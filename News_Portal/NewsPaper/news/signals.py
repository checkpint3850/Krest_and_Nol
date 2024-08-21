from django.conf import settings
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import mail_managers, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import PostCategory
from .tasks import notify_about_new_post


@receiver(m2m_changed, sender=PostCategory, )
def notify_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        notify_about_new_post.delay(instance.pk)
