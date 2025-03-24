from django.db import models
class Patient(models.Model):
    name=models.CharField(max_length=20,blank=false)
    nick_name=models.CharField(max_length=20,blank=True)
    gender=models.CharField(verbose_name='性别’，choices=[（'男','男'）,('女','女')])
    dob=model.DateTimeField(verbose_name='出生日期',null=True)
    nation=models.CharField(verbose_name='民族',max_length=3,default='汉')
    telephone=models.CharField(verbose_name='电话号码',max_length=15,null=True)
    
    proxy_id=models.IntegerField（default=0）
    relation=models.CharField（max_length=30,verbose_name='与患者关系'）
    
    def getRelations（self）:
        model.Patient.object.get（id=peoxy_id）
