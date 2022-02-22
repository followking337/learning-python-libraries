from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'currency', 'rating_status']
    # to view more other fields in admin
    # __str__ is not working after setting list_display
    # first field is link to that one specific register, so it can´t be editable
    list_editable = ['rating', 'year', 'currency', 'budget']  # make fields editable from admin
    ordering = ['-rating', 'name']  # rating_status can't be used here because is not attribute
    list_per_page = 3
    actions = ['set_dollars', 'set_euro']  # register of the method

    @admin.display(ordering='rating', description='status')  # after decorating this field can be ordered
    def rating_status(self, movie: Movie):  # by default this field is can´t be ordered
        if movie.rating < 50:
            return 'Зачем это смотреть?'
        if movie.rating < 70:
            return 'Разок можно посмотреть'
        if movie.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(request, f'Было обновлено {count_updated} записей', messages.ERROR)

# admin.site.register(Movie, MovieAdmin)  # same as decorator above
