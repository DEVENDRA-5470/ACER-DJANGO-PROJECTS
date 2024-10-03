from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about-us/', views.about_us, name='about_us'),  # About Us page
    path('newsletter/', views.newsletter, name='newsletter'),  # Newsletter page
    path('send-email/', views.send_email, name='send_email'),  # Send email page
    path('admin/', views.admin_url, name='admin-panel'),  # Admin panel
    path('admin-add-blog/', views.admin_add_blog, name='admin-add-blog'),  # Add blog
    path('edit-blog/', views.edit_blog, name='edit-blog'),  # Edit blog by ID
    path('update-post/<int:id>/', views.updatepost, name='updatepost'),  # Update post by ID
    path('delete-post/<int:id>/', views.delete_post, name='delete-post'),  # Delete post by ID
    path('blog/<slug:slug>/', views.show_blog_detail, name='blog_detail'),  # Blog detail by slug
    path('category/<str:name>/', views.all_category, name='all_category'),  # All posts in a category
    path('add-category/', views.admin_add_category, name='admin-add-category'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
