from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateInoteForm
from .models import Inote


def index(request):
    context = {
        'inote_list': Inote.objects.all()
    }
    return render(request, 'inote/inote_list.html', context)


def add(request):
    # 送信内容(request.POST)を元にフォームを作る、POSTではなければからのフォーム.（イディオムとして覚える）
    form = CreateInoteForm(request.POST or None)
    # request.methodにはGET or POSTが入っている.method==POST,送信ボタン押下時、入力内容に誤りがなければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('inote:index')
    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': form
    }
    return render(request, 'inote/inote_form.html', context)


def update(request, pk):
    inote = get_object_or_404(Inote, pk=pk)
    form = CreateInoteForm(request.POST or None, instance=inote)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('inote:index')
    context ={
        'form': form
    }
    return render(request, 'inote/inote_form.html', context)


def delete(request, pk):
    inote = get_object_or_404(Inote, pk=pk)
    if request.method == 'POST':
        inote.delete()
        return redirect('inote:index')
    context ={
        'inote': inote
    }
    return render(request, 'inote/inote_confirm_delete.html', context)


def detail(request, pk):
    inote = get_object_or_404(Inote, pk=pk)
    context ={
        'inote': inote
    }
    return render(request, 'inote/inote_detail.html', context)
