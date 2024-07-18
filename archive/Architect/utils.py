import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

def delete_file_on_delete(instance, **kwargs):
    """
    Deletes file from filesystem when corresponding model object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

def delete_file_on_change(instance, sender, **kwargs):
    """
    Deletes old file from filesystem when corresponding model object is updated with new file.
    """
    if not instance.pk:
        return

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

def connect_image_deletion_signals(model):
    """
    Connects post_delete and pre_save signals to the given model for image deletion.
    """
    post_delete.connect(delete_file_on_delete, sender=model)
    pre_save.connect(delete_file_on_change, sender=model)

