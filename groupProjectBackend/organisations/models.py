from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
# from PIL import Image
import uuid


def upload_image_to(self, filename):
        print(filename)
        filename_base, filename_ext = os.path.splitext(filename)
        print(os.path.splitext(filename))
        u = uuid.uuid4()
        return 'posts/%s/%s' % (
            now().strftime("%Y%m%d"),
            u.hex
        )
class Organisation(models.Model):

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_organisation'
    )
    logo = models.ImageField(default=None, upload_to=upload_image_to, blank=True, null=True)
    # logo = models.ImageField(default='default.jpg', upload_to='logo_pics', blank=True, null=True)
    # logo = models.URLField()
    organisation = models.TextField(max_length=150, blank=True)
    description = models.TextField(max_length=300, blank=True)
    website = models.URLField()

    def __str__(self):
        return self.organisation

    def save(self, *args, **kwargs):
        super(Organisation, self).save(*args, **kwargs)

        # img = Image.open(self.logo.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300,  300)
        #     img.thumbnail(output_size)
        #     img.save(self.logo.path)
