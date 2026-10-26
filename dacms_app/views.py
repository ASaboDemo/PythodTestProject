from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import AlbumForm, ArticleForm, CarouselForm, CategoryForm, CategoryLinkForm, SubCategoryForm, ThemeForm
from .models import Album, Article, CSS, Carousel, Category, CategoryLink, Photo, SubCategory, Theme


def home(request):
    categories = Category.objects.filter(display=True).order_by('menu_order')
    articles = Article.objects.filter(display=True).order_by('-id')[:10]
    featured = Article.objects.filter(display=True, first_page=True).first()
    carousels = Carousel.objects.filter(display=True).order_by('id')
    theme = Theme.objects.order_by('id').first()
    site_css = CSS.objects.order_by('id').first()
    return render(
        request,
        'home/index.html',
        {
            'categories': categories,
            'articles': articles,
            'featured_article': featured,
            'carousels': carousels,
            'theme': theme,
            'site_css': site_css,
        },
    )


def category_index(request):
    categories = Category.objects.filter(display=True).order_by('menu_order')
    return render(request, 'categories/index.html', {'categories': categories})


def category_detail(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    subcategories = category.subcategories.filter(display=True).order_by('menu_order')
    category_links = CategoryLink.objects.filter(category=category).order_by('id')
    articles = Article.objects.filter(display=True).order_by('-id')
    return render(request, 'categories/detail.html', {'category': category, 'subcategories': subcategories, 'category_links': category_links, 'articles': articles})


def article_detail(request, article_slug=None):
    article = get_object_or_404(Article, slug=article_slug)
    return render(request, 'articles/detail.html', {'article': article})


def gallery(request):
    albums = Album.objects.filter(display=True)
    return render(request, 'gallery/index.html', {'albums': albums})


def album_detail(request, album_id=None):
    album = get_object_or_404(Album, id=album_id)
    photos = album.photos.filter(display=True).order_by('id')
    return render(request, 'gallery/detail.html', {'album': album, 'photos': photos})


@login_required
def admin_dashboard(request):
    categories_count = Category.objects.count()
    subcategories_count = SubCategory.objects.count()
    articles_count = Article.objects.count()
    albums_count = Album.objects.count()
    carousels_count = Carousel.objects.count()
    themes_count = Theme.objects.count()
    return render(
        request,
        'admin/dashboard.html',
        {
            'categories_count': categories_count,
            'subcategories_count': subcategories_count,
            'articles_count': articles_count,
            'albums_count': albums_count,
            'carousels_count': carousels_count,
            'themes_count': themes_count,
        },
    )


@login_required
def admin_category_list(request):
    categories = Category.objects.all().order_by('menu_order')
    return render(request, 'admin/categories_list.html', {'categories': categories})


@login_required
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_category_list')
    else:
        form = CategoryForm()
    return render(request, 'admin/categories_form.html', {'form': form, 'title': 'Create category'})


@login_required
def admin_category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'admin/categories_form.html', {'form': form, 'title': 'Edit category'})


@login_required
def admin_subcategory_list(request):
    subcategories = SubCategory.objects.all().order_by('menu_order')
    return render(request, 'admin/subcategories_list.html', {'subcategories': subcategories})


@login_required
def admin_subcategory_create(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_subcategory_list')
    else:
        form = SubCategoryForm()
    return render(request, 'admin/subcategories_form.html', {'form': form, 'title': 'Create subcategory'})


@login_required
def admin_subcategory_edit(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('admin_subcategory_list')
    else:
        form = SubCategoryForm(instance=subcategory)
    return render(request, 'admin/subcategories_form.html', {'form': form, 'title': 'Edit subcategory'})


@login_required
def admin_category_link_list(request):
    category_links = CategoryLink.objects.all().order_by('id')
    return render(request, 'admin/category_links_list.html', {'category_links': category_links})


@login_required
def admin_category_link_create(request):
    if request.method == 'POST':
        form = CategoryLinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_category_link_list')
    else:
        form = CategoryLinkForm()
    return render(request, 'admin/category_links_form.html', {'form': form, 'title': 'Create category link'})


@login_required
def admin_category_link_edit(request, category_link_id):
    category_link = get_object_or_404(CategoryLink, id=category_link_id)
    if request.method == 'POST':
        form = CategoryLinkForm(request.POST, instance=category_link)
        if form.is_valid():
            form.save()
            return redirect('admin_category_link_list')
    else:
        form = CategoryLinkForm(instance=category_link)
    return render(request, 'admin/category_links_form.html', {'form': form, 'title': 'Edit category link'})


@login_required
def admin_album_list(request):
    albums = Album.objects.all().order_by('id')
    return render(request, 'admin/albums_list.html', {'albums': albums})


@login_required
def admin_album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_album_list')
    else:
        form = AlbumForm()
    return render(request, 'admin/albums_form.html', {'form': form, 'title': 'Create album'})


@login_required
def admin_album_edit(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('admin_album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'admin/albums_form.html', {'form': form, 'title': 'Edit album'})


@login_required
def admin_carousel_list(request):
    carousels = Carousel.objects.all().order_by('id')
    return render(request, 'admin/carousels_list.html', {'carousels': carousels})


@login_required
def admin_carousel_create(request):
    if request.method == 'POST':
        form = CarouselForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_carousel_list')
    else:
        form = CarouselForm()
    return render(request, 'admin/carousels_form.html', {'form': form, 'title': 'Create carousel'})


@login_required
def admin_carousel_edit(request, carousel_id):
    carousel = get_object_or_404(Carousel, id=carousel_id)
    if request.method == 'POST':
        form = CarouselForm(request.POST, instance=carousel)
        if form.is_valid():
            form.save()
            return redirect('admin_carousel_list')
    else:
        form = CarouselForm(instance=carousel)
    return render(request, 'admin/carousels_form.html', {'form': form, 'title': 'Edit carousel'})


@login_required
def admin_theme_list(request):
    themes = Theme.objects.all().order_by('id')
    return render(request, 'admin/themes_list.html', {'themes': themes})


@login_required
def admin_theme_create(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_theme_list')
    else:
        form = ThemeForm()
    return render(request, 'admin/themes_form.html', {'form': form, 'title': 'Create theme'})


@login_required
def admin_theme_edit(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    if request.method == 'POST':
        form = ThemeForm(request.POST, instance=theme)
        if form.is_valid():
            form.save()
            return redirect('admin_theme_list')
    else:
        form = ThemeForm(instance=theme)
    return render(request, 'admin/themes_form.html', {'form': form, 'title': 'Edit theme'})


@login_required
def admin_article_list(request):
    articles = Article.objects.all().order_by('-id')
    return render(request, 'admin/articles_list.html', {'articles': articles})


@login_required
def admin_article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_article_list')
    else:
        form = ArticleForm()
    return render(request, 'admin/articles_form.html', {'form': form, 'title': 'Create article'})


@login_required
def admin_article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('admin_article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'admin/articles_form.html', {'form': form, 'title': 'Edit article'})
