from django.db import models

class ItemGroup(models.Model):
    name = models.TextField(null=False, blank=False)

    # TODO obfuscation of slugs
    slug = models.SlugField(null=False, blank=True, unique=True)    # blank=True (or we can use default=?) so the item 
                                                                    # can be created first before its slug is filled
    location = models.TextField(null=False, blank=True)
    num_items = models.IntegerField(default=1)
    item_count = models.IntegerField(default=1)
    AVAIL = "AVAIL"
    UNAVAIL = "UNAVAIL"
    status = models.TextField(null=False, blank=False, 
                              choices=[(AVAIL, "available"), (UNAVAIL, "unavailable")], 
                              default=AVAIL)
    description = models.TextField(null=False, blank=True)