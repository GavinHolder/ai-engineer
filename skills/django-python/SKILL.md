---
name: django-python
description: Comprehensive Django and Python development reference. Covers project structure, models, views, URLs, forms, DRF APIs, Celery tasks, HTMX SPA patterns, testing, security, Docker deployment, and service layer architecture. Auto-updated by update-django-skill.py for latest package versions and API changes.
---

# Django & Python — Complete Development Reference

**Tracked Versions** (auto-updated by `update-django-skill.py`):

| Package | Version | Role |
|---------|---------|------|
| Python | 3.13 | Runtime |
| Django | 6.0.2 | Web framework |
| djangorestframework | 3.16.1 | REST APIs |
| celery | 5.6.2 | Task queue |
| redis | 7.1.0 | Cache / broker |
| psycopg | 3.3.2 | PostgreSQL adapter |
| gunicorn | 25.0.3 | WSGI server |
| whitenoise | 6.11.0 | Static files |
| django-cors-headers | 4.9.0 | CORS middleware |
| django-filter | 25.2 | Queryset filtering |
| django-extensions | 4.1 | Dev utilities |
| django-htmx | 1.27.0 | HTMX integration |
| django-environ | 0.12.0 | Environment config |
| django-debug-toolbar | 6.2.0 | Debug panel |
| pytest-django | 4.11.1 | Testing |
| Pillow | 12.1.0 | Image processing |

> Versions are checked and updated by running `python update-django-skill.py`

---

## Project Structure (Modular)

```
project/
├── apps/
│   └── myapp/
│       ├── models/              # One model per file
│       │   ├── __init__.py      # Import all models for Django discovery
│       │   ├── user_profile.py
│       │   └── order.py
│       ├── services/            # Business logic (NOT in views)
│       │   ├── order_service.py
│       │   └── payment_service.py
│       ├── tasks/               # Celery tasks (modularized)
│       │   ├── __init__.py
│       │   ├── order_tasks.py
│       │   └── notification_tasks.py
│       ├── views/               # Thin controllers
│       │   ├── __init__.py
│       │   ├── order_views.py
│       │   └── api_views.py
│       ├── admin/               # Admin classes (modularized)
│       │   ├── __init__.py
│       │   └── order_admin.py
│       ├── forms/
│       ├── serializers/         # DRF serializers
│       ├── urls.py
│       ├── tests/
│       │   ├── unit/
│       │   ├── integration/
│       │   └── adversarial/     # Edge cases, failure modes
│       └── templatetags/
├── templates/
│   ├── base.html                # Master layout
│   ├── components/              # Reusable atoms ({% include %})
│   ├── pages/                   # Full pages extending base
│   └── partials/                # HTMX swap targets
├── static/
│   ├── css/
│   ├── js/
│   └── img/
├── config/                      # Project settings
│   ├── settings/
│   │   ├── base.py              # Shared settings
│   │   ├── development.py       # Dev overrides
│   │   └── production.py        # Prod overrides
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── celery.py
├── deployment/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── nginx.conf
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── manage.py
├── .env.example
├── .gitignore
└── CLAUDE.md
```

### Modular __init__.py Pattern

```python
# apps/myapp/models/__init__.py
from .user_profile import UserProfile
from .order import Order, OrderItem

__all__ = ['UserProfile', 'Order', 'OrderItem']
```

**Rule:** One model/service/admin per file. Max 500 lines per file, aim for 200-400.

---

## Models

### Field Reference

```python
from django.db import models
from django.conf import settings
from decimal import Decimal

class Order(models.Model):
    # --- Relationships ---
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='orders')
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE)

    # --- Text ---
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, default='')
    email = models.EmailField()
    url = models.URLField(blank=True)

    # --- Numbers ---
    price = models.DecimalField(max_digits=10, decimal_places=2)  # ALWAYS Decimal for money
    quantity = models.PositiveIntegerField(default=1)
    rating = models.FloatField(null=True, blank=True)             # Float OK for non-financial

    # --- Boolean ---
    is_active = models.BooleanField(default=True)

    # --- Date/Time ---
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateField(null=True, blank=True)

    # --- Files ---
    image = models.ImageField(upload_to='orders/%Y/%m/', blank=True)
    document = models.FileField(upload_to='docs/', blank=True)

    # --- JSON ---
    metadata = models.JSONField(default=dict, blank=True)

    # --- Choices ---
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        PENDING = 'PENDING', 'Pending'
        ACTIVE = 'ACTIVE', 'Active'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    # --- UUID primary key (optional) ---
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['user', 'status']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'], name='unique_user_order_title'),
            models.CheckConstraint(check=models.Q(price__gte=0), name='order_price_non_negative'),
        ]

    def __str__(self):
        return self.title
```

### on_delete Options

| Option | Behaviour |
|--------|-----------|
| `CASCADE` | Delete related objects (use for owned children) |
| `PROTECT` | Prevent deletion if related objects exist |
| `SET_NULL` | Set FK to NULL (requires `null=True`) |
| `SET_DEFAULT` | Set FK to default value |
| `SET(func)` | Set FK to return value of func |
| `DO_NOTHING` | Do nothing (handle in DB or signals) |

### QuerySet Patterns

```python
# Filtering
Order.objects.filter(status='ACTIVE', user=user)
Order.objects.exclude(status='CANCELLED')
Order.objects.filter(price__gte=100, price__lte=500)       # Range
Order.objects.filter(title__icontains='widget')              # Case-insensitive search
Order.objects.filter(created_at__date=date.today())          # Date lookup
Order.objects.filter(tags__name__in=['urgent', 'priority'])  # M2M lookup

# Chaining
Order.objects.filter(status='ACTIVE').select_related('user').prefetch_related('tags')

# Aggregation
from django.db.models import Count, Sum, Avg, F, Q
Order.objects.aggregate(total=Sum('price'), avg=Avg('price'), count=Count('id'))
Order.objects.values('status').annotate(count=Count('id'))

# F expressions (database-level operations)
Order.objects.filter(quantity__gt=F('min_quantity'))
Order.objects.update(price=F('price') * Decimal('1.10'))  # 10% increase

# Q objects (complex queries)
Order.objects.filter(Q(status='ACTIVE') | Q(status='PENDING'))
Order.objects.filter(Q(price__gt=100) & ~Q(status='CANCELLED'))

# Exists / subqueries
from django.db.models import Exists, Subquery
active_orders = Order.objects.filter(user=models.OuterRef('pk'), status='ACTIVE')
User.objects.annotate(has_active=Exists(active_orders))

# Bulk operations
Order.objects.bulk_create([Order(title=f'Order {i}') for i in range(100)])
Order.objects.bulk_update(orders, ['status', 'updated_at'])
Order.objects.filter(status='DRAFT').update(status='CANCELLED')
Order.objects.filter(status='CANCELLED').delete()

# Performance: select_related (FK/OneToOne) vs prefetch_related (M2M/reverse FK)
Order.objects.select_related('user', 'category')          # JOIN in SQL
Order.objects.prefetch_related('tags', 'orderitem_set')    # Separate query
```

### Custom Manager

```python
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Order(models.Model):
    objects = models.Manager()   # Default
    active = ActiveManager()     # Order.active.all()
```

---

## Service Layer Pattern (Critical)

**Business logic lives in `services/`, NOT views.**

```python
# apps/myapp/services/order_service.py
from decimal import Decimal
from django.db import transaction
from apps.myapp.models import Order, OrderItem

class OrderService:
    """Handles all order business logic."""

    @staticmethod
    @transaction.atomic
    def create_order(user, items_data: list[dict]) -> Order:
        """Create order with items. Validates stock and calculates totals."""
        order = Order.objects.create(user=user, status=Order.Status.PENDING)

        total = Decimal('0')
        for item_data in items_data:
            item = OrderItem.objects.create(
                order=order,
                product=item_data['product'],
                quantity=item_data['quantity'],
                price=item_data['product'].price,
            )
            total += item.price * item.quantity

        order.total = total
        order.save(update_fields=['total'])
        return order

    @staticmethod
    def cancel_order(order: Order) -> tuple[bool, str]:
        """Cancel order. Returns (success, reason)."""
        if order.status == Order.Status.COMPLETED:
            return False, "Cannot cancel completed order"
        if order.status == Order.Status.CANCELLED:
            return False, "Order already cancelled"

        order.status = Order.Status.CANCELLED
        order.save(update_fields=['status'])
        return True, "Order cancelled"
```

**View calls service:**
```python
# apps/myapp/views/order_views.py
def create_order_view(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = OrderService.create_order(request.user, form.cleaned_data['items'])
        return redirect('order_detail', pk=order.pk)
    return render(request, 'pages/order_form.html', {'form': form})
```

---

## Views

### Function-Based Views

```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).select_related('category')
    return render(request, 'pages/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'pages/order_detail.html', {'order': order})
```

### Class-Based Views

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'pages/order_list.html'
    context_object_name = 'orders'
    paginate_by = 25

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'pages/order_form.html'
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
```

---

## URLs

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.myapp.urls')),
    path('api/', include('apps.myapp.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

# apps/myapp/urls.py
from django.urls import path
from apps.myapp.views import order_views

urlpatterns = [
    path('', order_views.order_list, name='order_list'),
    path('orders/<int:pk>/', order_views.order_detail, name='order_detail'),
    path('orders/create/', order_views.order_create, name='order_create'),
    path('orders/<int:pk>/edit/', order_views.order_edit, name='order_edit'),
    path('orders/<int:pk>/delete/', order_views.order_delete, name='order_delete'),
]
```

---

## HTMX SPA Pattern

**Single-page feel with Django templates + HTMX. No full page reloads.**

### Setup

```html
<!-- base.html -->
<script src="https://unpkg.com/htmx.org@2.0.4"></script>
<script src="https://unpkg.com/htmx-ext-response-targets@2.0.2/response-targets.js"></script>
```

```python
# pip install django-htmx
INSTALLED_APPS = ['django_htmx', ...]
MIDDLEWARE = ['django_htmx.middleware.HtmxMiddleware', ...]
```

### View returns partial for HTMX, full page for normal

```python
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    template = 'partials/order_list.html' if request.htmx else 'pages/order_list.html'
    return render(request, template, {'orders': orders})
```

### HTMX Patterns

```html
<!-- Click to load content into target -->
<button hx-get="{% url 'order_detail' order.pk %}"
        hx-target="#content"
        hx-swap="innerHTML"
        hx-push-url="true">
    View Order
</button>

<!-- Form submission without page reload -->
<form hx-post="{% url 'order_create' %}"
      hx-target="#order-list"
      hx-swap="afterbegin">
    {% csrf_token %}
    {{ form.as_div }}
    <button type="submit">Create</button>
</form>

<!-- Inline edit -->
<div id="order-{{ order.pk }}">
    <span hx-get="{% url 'order_edit' order.pk %}"
          hx-target="#order-{{ order.pk }}"
          hx-swap="outerHTML">
        {{ order.title }}
    </span>
</div>

<!-- Delete with confirmation -->
<button hx-delete="{% url 'order_delete' order.pk %}"
        hx-target="#order-{{ order.pk }}"
        hx-swap="outerHTML"
        hx-confirm="Delete this order?">
    Delete
</button>

<!-- Infinite scroll -->
<div hx-get="{% url 'order_list' %}?page={{ page.next_page_number }}"
     hx-trigger="revealed"
     hx-swap="afterend">
</div>

<!-- Search with debounce -->
<input type="search"
       hx-get="{% url 'order_search' %}"
       hx-target="#results"
       hx-trigger="keyup changed delay:300ms"
       name="q">

<!-- Polling (live updates) -->
<div hx-get="{% url 'order_status' order.pk %}"
     hx-trigger="every 5s"
     hx-swap="innerHTML">
    {{ order.status }}
</div>
```

### HTMX Response Headers

```python
from django_htmx.http import HttpResponseClientRedirect, trigger_client_event

def order_create(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = OrderService.create_order(request.user, form.cleaned_data)
        if request.htmx:
            response = render(request, 'partials/order_card.html', {'order': order})
            trigger_client_event(response, 'orderCreated', {})
            return response
        return redirect('order_detail', pk=order.pk)
    return render(request, 'partials/order_form.html', {'form': form})
```

---

## Django REST Framework (DRF)

### Serializers

```python
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'title', 'status', 'total', 'created_at']
        read_only_fields = ['id', 'user', 'total', 'created_at']

class OrderCreateSerializer(serializers.Serializer):
    """Separate serializer for creation (different fields than read)."""
    title = serializers.CharField(max_length=200)
    items = serializers.ListField(child=serializers.DictField())

    def create(self, validated_data):
        user = self.context['request'].user
        return OrderService.create_order(user, validated_data['items'])
```

### ViewSets

```python
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()
        success, reason = OrderService.cancel_order(order)
        if success:
            return Response({'status': 'cancelled'})
        return Response({'error': reason}, status=status.HTTP_400_BAD_REQUEST)
```

### API URLs

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='order')

urlpatterns = router.urls
```

### Pagination, Filtering, Throttling

```python
# config/settings/base.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour',
    },
}
```

---

## Celery (Async Tasks)

### Setup

```python
# config/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# config/settings/base.py
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Celery Beat schedule
CELERY_BEAT_SCHEDULE = {
    'cleanup-expired-orders': {
        'task': 'apps.myapp.tasks.order_tasks.cleanup_expired_orders',
        'schedule': 300.0,  # Every 5 minutes
    },
}
```

### Task Patterns

```python
# apps/myapp/tasks/order_tasks.py
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def process_order(self, order_id: int) -> dict:
    """Process an order asynchronously."""
    try:
        order = Order.objects.get(id=order_id)
        result = OrderService.process(order)
        return {'success': True, 'order_id': order_id, 'result': result}
    except Order.DoesNotExist:
        logger.error(f"Order {order_id} not found")
        return {'success': False, 'error': 'Order not found'}
    except Exception as exc:
        logger.exception(f"Error processing order {order_id}")
        raise self.retry(exc=exc)

@shared_task
def cleanup_expired_orders():
    """Periodic task: cancel orders older than 24h in PENDING status."""
    from django.utils import timezone
    cutoff = timezone.now() - timezone.timedelta(hours=24)
    expired = Order.objects.filter(status='PENDING', created_at__lt=cutoff)
    count = expired.update(status='CANCELLED')
    logger.info(f"Cancelled {count} expired orders")
    return {'cancelled': count}
```

### Calling Tasks

```python
# Fire and forget
process_order.delay(order.pk)

# With options
process_order.apply_async(args=[order.pk], countdown=30, queue='high')

# Get result
result = process_order.delay(order.pk)
result.get(timeout=10)  # Blocks until done
```

---

## Forms

```python
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'description', 'category', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be positive")
        return price
```

---

## Templates (Bootstrap + HTMX)

### base.html

```html
<!doctype html>
<html lang="en" data-bs-theme="light">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    {% block extra_css %}{% endblock %}
    <title>{% block title %}{{ project_name }}{% endblock %}</title>
</head>
<body class="d-flex flex-column min-vh-100" hx-ext="response-targets">

    {% include 'components/navbar.html' %}

    <main class="container py-4 flex-grow-1" id="main-content">
        {% include 'components/messages.html' %}
        {% block content %}{% endblock %}
    </main>

    {% include 'components/footer.html' %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/htmx.org@2.0.4"></script>
    <script src="https://unpkg.com/htmx-ext-response-targets@2.0.2/response-targets.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Template Tags

```django
{% load static %}              {# Static files #}
{% csrf_token %}               {# CSRF in forms #}
{% url 'view_name' pk=obj.pk %} {# URL reverse #}
{% include 'comp.html' with obj=item %} {# Partial include #}

{% if condition %}...{% elif %}...{% else %}...{% endif %}
{% for item in items %}...{% empty %}No items{% endfor %}
{{ value|default:"N/A" }}      {# Default filter #}
{{ date|date:"Y-m-d" }}        {# Date format #}
{{ text|truncatewords:30 }}     {# Truncate #}
{{ amount|floatformat:2 }}      {# Number format #}
{{ html|safe }}                 {# Mark as safe (careful!) #}
```

---

## Settings (Split Configuration)

```python
# config/settings/base.py
import environ
from pathlib import Path

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'rest_framework',
    'django_filters',
    'corsheaders',
    'django_htmx',
    # Local
    'apps.myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3'),
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    'staticfiles': {'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'},
}
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# config/settings/development.py
from .base import *
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS += ['debug_toolbar', 'django_extensions']
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = ['127.0.0.1']

# config/settings/production.py
from .base import *
DEBUG = False
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## Authentication

```python
# Custom user model (do this FIRST, before any migrations)
# apps/accounts/models/user.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass  # Extend later without migration headaches

# config/settings/base.py
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### Login/Logout Views

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

---

## Testing

### pytest-django Setup

```ini
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings.development
python_files = tests.py test_*.py *_tests.py
```

### Test Patterns

```python
import pytest
from django.test import TestCase, Client
from apps.myapp.models import Order
from apps.myapp.services.order_service import OrderService

@pytest.mark.django_db
class TestOrderService:
    def test_create_order(self, user):
        order = OrderService.create_order(user, [{'product': product, 'quantity': 1}])
        assert order.status == Order.Status.PENDING
        assert order.user == user

    def test_cancel_completed_order_fails(self, completed_order):
        success, reason = OrderService.cancel_order(completed_order)
        assert success is False
        assert "Cannot cancel completed" in reason

# Fixtures
@pytest.fixture
def user(db):
    from django.contrib.auth import get_user_model
    return get_user_model().objects.create_user(username='test', password='testpass123')

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
```

### API Testing

```python
@pytest.mark.django_db
class TestOrderAPI:
    def test_list_orders(self, api_client, user):
        api_client.force_authenticate(user=user)
        response = api_client.get('/api/orders/')
        assert response.status_code == 200

    def test_create_order(self, api_client, user):
        api_client.force_authenticate(user=user)
        response = api_client.post('/api/orders/', {'title': 'Test'})
        assert response.status_code == 201
```

### Running Tests

```bash
pytest                                      # All tests
pytest apps/myapp/tests/ -v                 # Specific app
pytest -k "test_create" -v                  # By name pattern
pytest --cov=apps --cov-report=term-missing # With coverage
pytest -x                                   # Stop on first failure
```

---

## Security Checklist

- [ ] `SECRET_KEY` in environment variable, never in code
- [ ] `DEBUG = False` in production
- [ ] `ALLOWED_HOSTS` set explicitly
- [ ] `SECURE_SSL_REDIRECT = True`
- [ ] `SESSION_COOKIE_SECURE = True`
- [ ] `CSRF_COOKIE_SECURE = True`
- [ ] `SECURE_HSTS_SECONDS` set (31536000 = 1 year)
- [ ] `.env` in `.gitignore`
- [ ] `CORS_ALLOWED_ORIGINS` set explicitly (not `CORS_ALLOW_ALL_ORIGINS`)
- [ ] Custom `AUTH_USER_MODEL` defined before first migration
- [ ] All user input validated (forms or serializers)
- [ ] No raw SQL (use ORM, or parameterized queries only)
- [ ] `{% csrf_token %}` in all POST forms
- [ ] File uploads validated (type, size)
- [ ] `@login_required` / `IsAuthenticated` on all protected views

---

## Docker Deployment (Portainer + Traefik)

### Dockerfile

```dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/prod.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
```

### docker-compose.yml (Portainer manual build)

```yaml
version: '3.8'

services:
  web:
    image: myapp:latest
    build:
      context: .
      dockerfile: Dockerfile
    env_file: .env
    volumes:
      - media_data:/app/media
      - static_data:/app/staticfiles
    networks:
      - traefik_proxy
      - internal
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.myapp.rule=Host(`myapp.example.com`)"
      - "traefik.http.routers.myapp.entrypoints=websecure"
      - "traefik.http.routers.myapp.tls.certresolver=letsencrypt"
      - "traefik.http.services.myapp.loadbalancer.server.port=8000"
    depends_on:
      - db
      - redis

  db:
    image: postgres:16-alpine
    env_file: .env
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - internal

  redis:
    image: redis:7-alpine
    networks:
      - internal

  worker:
    image: myapp:latest
    command: celery -A config worker -l info
    env_file: .env
    volumes:
      - media_data:/app/media
    networks:
      - internal
    depends_on:
      - db
      - redis

  beat:
    image: myapp:latest
    command: celery -A config beat -l info
    env_file: .env
    networks:
      - internal
    depends_on:
      - db
      - redis

volumes:
  postgres_data:
  media_data:
  static_data:

networks:
  traefik_proxy:
    external: true
  internal:
```

---

## Django Management Commands

```bash
# Project
django-admin startproject config .
python manage.py startapp myapp

# Database
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
python manage.py sqlmigrate myapp 0001

# Development
python manage.py runserver
python manage.py shell
python manage.py createsuperuser
python manage.py collectstatic

# Data
python manage.py dumpdata myapp --indent 2 > data.json
python manage.py loaddata data.json
python manage.py flush  # Delete all data (dangerous!)

# Custom command
# apps/myapp/management/commands/seed_data.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10)

    def handle(self, *args, **options):
        count = options['count']
        # Create objects...
        self.stdout.write(self.style.SUCCESS(f'Created {count} records'))
```

---

## Rules for Django Development

1. **ALWAYS use the service layer** - Views are thin, services hold logic
2. **ALWAYS use Decimal for money** - Never float for financial calculations
3. **ALWAYS use select_related/prefetch_related** - Prevent N+1 queries
4. **ALWAYS define a custom User model** before first migration
5. **ALWAYS use environment variables** for secrets (django-environ)
6. **ALWAYS write tests** before implementation (TDD)
7. **ALWAYS use transactions** for multi-step write operations
8. **ALWAYS validate at boundaries** - Forms for HTML, Serializers for API
9. **Modularize** - One model/service/admin per file, max 500 lines
10. **HTMX for SPA feel** - Return partials for HTMX requests, full pages otherwise
