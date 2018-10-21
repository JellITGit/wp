from django.db import models

# Create your models here.
class walmart_products(models.Model):
    itemid = models.IntegerField(max_length=11, primary_key=True)
    name = models.TextField(max_length=200, null = True)
    upc = models.TextField(max_length=20, null = True)
    longDescription = models.TextField(max_length=2000, null = True)
    enabled = models.IntegerField(max_length=1, null = True)
    parentItemId = models.IntegerField(max_length=11, null = True)
    salePrice = models.DecimalField((max_digits=10, decimal_places=2 null = True)
    categoryPath = models.TextField(max_length=2000, null = True)
    shortDescription = models.TextField(max_length=2000, null = True)
    thumbnailImage = models.TextField(max_length=2000, null = True)
    mediumImage = models.TextField(max_length=2000, null = True)                
    largeImage = models.TextField(max_length=2000, null = True)
    productTrackingUrl = models.TextField(max_length=2000, null = True)
    standardShipRate = models.DecimalField((max_digits=10, decimal_places=2 null = True)
    marketplace = models.TextField(max_length=200, null = True)
    modelNumber = models.TextField(max_length=200, null = True)
    productUrl = models.TextField(max_length=2000, null = True)
    customerRating = models.TextField(max_length=3, null = True)
    numReviews = models.TextField(max_length=4, null = True)
    image_urls_json = models.TextField 
    updated_date = models.DateTimeField(auto_now_add=True))
    class Meta:
         db_table = "walmart_products"
    

    
    
    def __str__(self):
        return '%s %s' % (self.itemid, self.enabled)
