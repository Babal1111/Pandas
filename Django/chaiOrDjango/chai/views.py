from django.shortcuts import render
from .models import ChaiVarity
# Create your views here.
from django.shortcuts import get_object_or_404

# from .forms import ChaiVarityForm

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk = chai_id)
    return render(request, '/chai_detail.html', {'chai': chai})

def chai_store_view(request):

    # if(request.method== 'POST'):
    #     form = ChaiVarityForm(request.POST)
    #     if form.is_valid():
    #         chai_varity = form.cleaned_data['chai_varity']
    return render(request,'chai/chai_stores.html',{stores:'stores'})