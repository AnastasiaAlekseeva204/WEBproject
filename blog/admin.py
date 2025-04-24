from django.contrib import admin
from .models import Post 
from .models import Book
from .models import Author
from .models import Rubric
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Category
from .models import New

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
# Register your models here.
admin.site.register(Post)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(New)
#admin.site.register(Rubric,MPTTModelAdmin)