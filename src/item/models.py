from django.db import models

class ItemGroup(models.Model):
    name = models.TextField(null=False, blank=False)
    location = models.TextField(null=False, blank=True)
    num_items = models.IntegerField(default=0)
    item_count = models.IntegerField(default=0)
    AVAIL = "AVAIL"
    UNAVAIL = "UNAVAIL"
    status = models.TextField(null=False, blank=False, 
                              choices=[(AVAIL, "available"), (UNAVAIL, "unavailable")], 
                              default=UNAVAIL)
    description = models.TextField(null=False, blank=True)