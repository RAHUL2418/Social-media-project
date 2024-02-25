class BlogPost(models.Model): 
      id = models.IntegerField(primary_key=True) 
      likes = models.IntegerField(default=0) 
      post = models.TextField() 