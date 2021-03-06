from django import forms
from django.contrib import admin

from mrben.main.models import Entry, Category, Link


class EntryAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntryAdminForm, self).__init__(*args, **kwargs)

    body = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'tinymce vLargeTextField'}))

    class Meta:
        model = Entry


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
    list_display = ('title', 'slug', 'status', 'publish',)
    list_filter = ('status', 'publish', 'categories',)
    search_fields = ('title', 'body')
    fields = (
        'title', 'slug', 'author', 'body', 'publish', 'status', 'categories',
    )

    class Media:
        js = (
            'js/jquery/jquery-1.4.1.min.js',
            'js/tiny_mce/jquery.tinymce.js',
            'js/admin/entry.js',
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Link)
