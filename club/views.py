from dataclasses import dataclass

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import ContactMessage, Project, Resource


@dataclass
class ResourceItem:
    title: str
    url: str
    category: str


def home(request):
    query = request.GET.get('q', '').strip()
    projects = Project.objects.order_by('-created_at')
    resource_qs = Resource.objects.order_by('category', 'title')
    form = ContactForm(request.POST or None)

    default_resources = [
        ResourceItem('GitHub Education', 'https://education.github.com/', 'students'),
        ResourceItem('Harvard CS50x', 'https://cs50.harvard.edu/x/2024/', 'cs'),
        ResourceItem('Django Girls', 'https://djangogirls.org/', 'cs'),
        ResourceItem('Figma', 'https://www.figma.com/', 'tools'),
        ResourceItem('Tinkercad', 'https://www.tinkercad.com/', 'tools'),
        ResourceItem('Robotics Project Ideas', 'https://www.firstinspires.org/resource-library', 'ideas'),
    ]

    if resource_qs.exists():
        resources = list(resource_qs)
    else:
        resources = default_resources

    if query:
        projects = projects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        resources = [
            resource for resource in resources
            if query.lower() in resource.title.lower() or query.lower() in resource.category.lower()
        ]

    projects = projects[:6]

    if request.method == 'POST' and form.is_valid():
        contact = ContactMessage.objects.create(
            name=form.cleaned_data['name'],
            message=form.cleaned_data['message'],
        )
        send_mail(
            subject=f'Robotics Club Contact from {contact.name}',
            message=contact.message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['lainekrup@gmail.com'],
            fail_silently=False,
        )
        return redirect('home')

    return render(
        request,
        'club/home.html',
        {
            'projects': projects,
            'resources': resources,
            'form': form,
            'query': query,
        },
    )
