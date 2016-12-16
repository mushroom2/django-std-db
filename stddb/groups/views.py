from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView

from django.core.urlresolvers import reverse_lazy

from groups.models import Group
from stud.models import Student


class Groups(ListView):

    model = Group
    template_name = 'groups.html'
    context_object_name = 'groups'

    def get_queryset(self):
        return self.model.objects.order_by('pk')


class GroupAdd(CreateView):

    model = Group
    fields = '__all__'
    template_name = 'group_add.html'
    success_url = reverse_lazy('group:all')


class GroupsEdit(UpdateView):
    
    model = Group
    fields = '__all__'
    template_name = 'groups_edit.html'
    success_url = reverse_lazy('group:all')


class GroupList(ListView):

    model = Student
    fields = '__all__'
    template_name = 'students_in_group.html'
    context_object_name = 'students_list'
    
    def get_queryset(self):
        
        pk = self.kwargs.get('pk')
        return self.model.objects.filter(group__pk=pk)


class GroupDelete(DeleteView):

    model = Group
    fields = '__all__'
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('group:all')
    
    def get_context_data(self, **kwargs):
        context = super(GroupDelete, self).get_context_data(**kwargs)
        context['obj'] = 'group'
        return context
