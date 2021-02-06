from django.db import models
class Patient(models.Model):
    name=models.CharField(max_length=20,blank=false)
    proxy_id=models.IntegerField（default=0）
    relation=models.CharField（max_length=30,verbose_name='与患者关系'）
    
    def getRelations（self）:
        model.Patient.object.all（peoxy_id=self.id）
