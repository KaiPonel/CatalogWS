from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import ugettext as _
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

"""
      This Website was designed for a very special use case.
      If you want to implement own/other Categories Change the content below respectively.
  """


class Item(models.Model):
    def get_img_upload_path(self, instance, name):
        return f'{instance.name}/img/{self.id}'

    # Meta
    item_Image = models.ImageField(upload_to="images/", default="images/default/default.png",
                                   verbose_name="Bild des Objekts", blank=True)

    # Other
    name = models.CharField(max_length=100, default=" ", name="name", verbose_name="Objektname", blank=False)
    artist = models.CharField(max_length=100, default=" ", verbose_name="Künstler", blank=True)
    quantity = models.IntegerField(default=1, blank=True, null=False, verbose_name="Anzahl")
    year = models.IntegerField(blank=True, null=True, verbose_name="Jahr")
    kindOf = models.CharField(default=" ", max_length=100, verbose_name="Art", blank=True)
    description = models.CharField(max_length=8000, default=" ", verbose_name="Beschreibung", blank=True)
    glashuette = models.CharField(max_length=100, default=" ", verbose_name="Glashütte", blank=True)
    color = models.CharField(max_length=120, default=" ", verbose_name="Farbe", blank=True)

    # image = models.FileField()
    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"my_id": self.id})

    def get_model_fields(self):
        return Item._meta.fields

    def addField(self, name, field):
        setattr(self, name, field)

    def getID(self):
        return int(Item._meta.fields[0].value_to_string(obj=self))

    def save(self, *args, **kwargs):
        if not self.id and not self.item_Image == "images/default/default.png":
            self.item_Image = self.compressImage(self.item_Image)
        super(Item, self).save(*args, **kwargs)

    def compressImage(self, uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        imageTemproary = imageTemproary.convert("RGB")
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize((1020, 573))
        imageTemproary.save(outputIoStream, format='JPEG', optimize=True)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0],
                                             'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage
