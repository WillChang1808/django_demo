from django.shortcuts import render,redirect,HttpResponse  #需手动添加 redirect,HttpResponse

# Create your views here.
def ajax(request):
    if request.method == 'POST':
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        res = int(i1) + int(i2)
        return HttpResponse(res)

    return  render(request,'ajax_demo.html')
