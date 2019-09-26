from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateInoteForm
from .models import Inote
from django.contrib import messages


class IndexView(generic.ListView):
    model = Inote
    paginate_by = 10

    def get_queryset(self):
        return Inote.objects.order_by('-created_at')


class AddView(generic.CreateView):
    model = Inote
    # fields = '__all__'
    form_class = CreateInoteForm
    success_url = reverse_lazy('inote:index')

    def form_invalid(self, form):
        messages.warning(self.request, "Ensure this value has at least 50 characters")
        return super().form_invalid(form)


class UpdateView(generic.CreateView):
    model = Inote
    form_class = CreateInoteForm
    success_url = reverse_lazy('inote:index')


class DeleteView(generic.DeleteView):
    model = Inote
    success_url = reverse_lazy('inote:index')


class DetailView(generic.DetailView):
    model = Inote

