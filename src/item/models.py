from django.db import models

class ItemGroup(models.Model):
    name = models.TextField(null=False, blank=False)
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

    def save(self, *args, **kwargs): # Override save function
        # If saving for the first time, call slugify() to set slug
        if not self.slug:
            self.slug = itemHash(self)
        super(ItemGroup, self).save(*args, **kwargs)

s = 0

def itemHash(itmgrp):
    # hashing function here
    # example:
    global s 
    s += 1
    return s