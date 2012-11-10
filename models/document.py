from django.db import models
from os import path

class Document(models.Model):
	class Meta:
		app_label = 'gedgo'
	
	title = models.CharField(max_length=40, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	
	docfile = models.FileField(upload_to='uploaded')
	thumb = models.FileField(upload_to='uploaded/thumbs', null=True, blank=True)
	
	kind = models.CharField(max_length=5, 
		choices=(('DOCUM', 'Document'), ('VIDEO', 'Video'), ('DOCUV', 'Documentary'),
			('PHOTO', 'Image')))
	
	tagged_people = models.ManyToManyField('Person', 
		related_name='media_tagged_people', null=True, blank=True)
	
	tagged_families = models.ManyToManyField('Family', 
		related_name='media_tagged_families', null=True, blank=True)
	
	last_updated = models.DateTimeField(auto_now_add=True)
	
	gedcom = models.ForeignKey('Gedcom', null=True, blank=True)
	
	def key_person_tag(self):
		if self.tagged_people.all():
			return self.tagged_people.all()[0]
	
	def file_base_name(self):
		return docfile.path.basename()
	
	def __unicode__(self):
		return path.basename(self.docfile.path)