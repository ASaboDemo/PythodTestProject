from django.contrib import admin
from .models import (
    User, Language, Category, SubCategory, CategoryRelationship,
    Article, ArticleRelation, CSS, CategoryLink, LinkContent,
    Album, Photo, Carousel, CarouselPhoto, LanguageAdmin,
    BotSearch, BotSearchResult, Theme,
)

admin.site.register(User)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CategoryRelationship)
admin.site.register(Article)
admin.site.register(ArticleRelation)
admin.site.register(CSS)
admin.site.register(CategoryLink)
admin.site.register(LinkContent)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Carousel)
admin.site.register(CarouselPhoto)
admin.site.register(LanguageAdmin)
admin.site.register(BotSearch)
admin.site.register(BotSearchResult)
admin.site.register(Theme)
