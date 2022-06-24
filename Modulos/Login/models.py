from django.contrib.auth.models import AbstractUser
from django.db import models

from Farmacia.settings import MEDIA_URL, STATIC_URL

class User(AbstractUser):
	image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

	def get_image(self):
		if self.image:
			return '{}{}'.format(MEDIA_URL, self.image)
		return '{}{}'.format(STATIC_URL, 'img/empty.png')

	def toJSON(self):
		item = model_to_dict(self, exclude['password', 'groups', 'user_permissions'])
		item['last_login'] = self.last_login.strftime('%Y-%m-%d')
		item['date_joined'] = self.last_login.strftime('%Y-%m-%d')
		item['imagen'] = self.get_image()
		return item
