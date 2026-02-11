from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail_address = models.CharField(max_length=50)
    
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.full_name()
    
    class Meta:
        verbose_name_plural = 'Authors'
    
    
    
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.caption
    
    class Meta:
        verbose_name_plural = 'Tags'
    
    

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='post')
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True, null=True)
    slug = models.SlugField(default="", blank=True,  null=False, db_index=True, unique=True) 
    content = models.TextField(default="")
    tag = models.ManyToManyField(Tag)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # Esto crea un slug a partir del title antes de que se guarde (abajo).
        super().save( *args, **kwargs) # Esto es para mantener los save methods que ya tenemos. 
    
    def __str__(self) -> str:
        return f"{self.title} ({self.date_created})"
    
    class Meta:
        verbose_name_plural = 'Posts'
        
