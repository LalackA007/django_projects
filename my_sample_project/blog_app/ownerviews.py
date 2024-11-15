from django.views.generic import DetailView, DeleteView, UpdateView, CreateView
from django.utils.text import slugify

class OwnerDeleteView(DeleteView):
    def get_queryset(self, **kwargs):
        qset = super().get_queryset(**kwargs)
        qset = qset.filter(owner = self.request.user)
        return qset

class OwnerUpdateView(UpdateView):
    def get_queryset(self, **kwargs):
        qset = super().get_queryset(**kwargs)
        qset = qset.filter(owner = self.request.user)
        return qset

class OwnerCreateView(CreateView):
    def form_valid(self, form):
       print('form_valid called')
       object = form.save(commit=False)
       object.owner = self.request.user
       object.slug = slugify(object.title)
       object.save()
       return super(CreateView, self).form_valid(form)

