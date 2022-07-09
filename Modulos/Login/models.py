from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict

from Modulos.Productos.models import Sucursal
from Farmacia.settings import MEDIA_URL, STATIC_URL

class User(AbstractUser):
	image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
	sucursales = models.ManyToManyField(Sucursal)

	def get_image(self):
		if self.image:
			return '{}{}'.format(MEDIA_URL, self.image)
		return '{}{}'.format(STATIC_URL, 'images/empty.png')

	def toJSON(self):
		item = model_to_dict(self, exclude=['user_permissions', 'last_login', 'sucursales'])
		if self.last_login:
			item['last_login'] = self.last_login.strftime('%Y-%m-%d')
		item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
		item['full_name'] = self.get_full_name()
		item['image'] = self.get_image()
		item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
		return item

	def get_group_session(self):
		try:
			request = get_current_request()
			groups = self.groups.all()
			if groups.exists():
				if 'group' not in request.session:
					request.session['group'] = groups[0]
		except:
			pass

