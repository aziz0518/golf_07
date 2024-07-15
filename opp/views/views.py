from django.urls import reverse_lazy
from django.views.generic import View,  CreateView
from django.shortcuts import redirect, render
from golf.forms import MemberForm, PersonForm, EventForm
from golf.models import Events, Person
# Create your views here.


def index(request):
    events = Events.objects.all()
    persons = Person.objects.all()
    # paginator = Paginator(person, 1)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'events': events,
        'persons': persons
    }
    return render(request, 'golf/index.html', context)


# def person(request):
#         persons = Person.objects.all()
#         return render(request, 'golf/index.html', {'persons': persons})

# def event_detail(request, pk):
#     events = Events.objects.get(id=pk)
#     context = {
#         'events': events
#     }
#     return render(request, 'event-detail.html', context)


def detail_event(request):
    event = Events.objects.all()
    context = {
        'event': event
    }
    return render(request, 'golf/event-detail.html', context)

def listing(request):
    return render(request, 'golf/event-listing.html')



class MemberAdd(View):
    def get(self, request):
        form = MemberForm()
        return render(request, 'golf/member.html', {'form': form})

    def post(self, request):
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'gold/member.html', {'form': form})



# def members(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = MemberForm()
    
#     return render(request, 'golf/member.html', {'form': form})





# class PersonAddTemplateView(TemplateView):
#     template_name = 'golf/add-person.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = PersonForm()
#         return context
    
#     def post(self, request, *args, **kwargs):
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             tepm = form.save(commit=False)
#             return redirect('index', {'tepm': tepm})






class PersonAddView(CreateView):
    model = Person
    template_name = 'golf/add-person.html'
    form_class = PersonForm
    success_url = reverse_lazy('index')







# def add_person(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = PersonForm()
    
#     return render(request, 'golf/add-person.html', {'form': form})



def add_events(request):
    event = Events.objects.all()
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()

    context = {
        'add_event': event,
        'form': form
    }
    return render(request, 'golf/add-event.html', context)