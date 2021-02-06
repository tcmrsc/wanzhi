def profile（request）:
    id=request.Get['id']
    pts=Patient.objects.filter(id=id)
     并且找出proxy id 为此ID
    然后显示出来
    选择挂号、治疗
