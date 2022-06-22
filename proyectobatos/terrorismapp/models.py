
from django.db import models

class gName(models.Model):
    eventid =models.BigIntegerField()
    gname = models.CharField(max_length=450)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['eventid', 'gname'], name='unique_eventid_gname_combination'
            )]
    def __str__(self):
        return 'El evento es %s el nombre de grupo es %s' %(self.eventid, self.gname)
