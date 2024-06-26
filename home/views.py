from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Company, Banner, About, Review, Service, Video, Process, Images, Instagram, Footer, Industry, \
    Blog


class Home(TemplateView):
    template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        companys = Company.objects.last()
        banner = Banner.objects.all()
        services = Service.objects.all()
        about = About.objects.last()
        reviews = Review.objects.all()
        video = Video.objects.last()
        process = Process.objects.all()
        images = Images.objects.last()
        instagram = Instagram.objects.all()
        footer = Footer.objects.last()
        industry = Industry.objects.all()
        blog = Blog.objects.all()

        context = {
            'companys': companys,
            'banner': banner,
            'services': services,
            'about': about,
            'reviews': reviews,
            'video': video,
            'process': process,
            'images': images,
            'instagram': instagram,
            'footer': footer,
            'industry': industry,
            'blog': blog,
        }
        return render(request, self.template_name, context)

class AboutPage(TemplateView):
    template_name = "home/about.html"

    def get(self, request, *args, **kwargs):
        companys = Company.objects.last()
        banner = Banner.objects.all()
        services = Service.objects.all()
        about = About.objects.last()
        reviews = Review.objects.all()
        video = Video.objects.last()
        process = Process.objects.all()
        images = Images.objects.last()
        instagram = Instagram.objects.all()
        footer = Footer.objects.last()
        industry = Industry.objects.all()
        blog = Blog.objects.all()

        context = {
            'companys': companys,
            'banner': banner,
            'services': services,
            'about': about,
            'reviews': reviews,
            'video': video,
            'process': process,
            'images': images,
            'instagram': instagram,
            'footer': footer,
            'industry': industry,
            'blog': blog,
        }
        return render(request, self.template_name, context)

class ServicePage(TemplateView):
    template_name = "home/service.html"

    def get(self, request, *args, **kwargs):
        companys = Company.objects.last()
        banner = Banner.objects.all()
        services = Service.objects.all()
        about = About.objects.last()
        reviews = Review.objects.all()
        video = Video.objects.last()
        process = Process.objects.all()
        images = Images.objects.last()
        instagram = Instagram.objects.all()
        footer = Footer.objects.last()
        industry = Industry.objects.all()
        blog = Blog.objects.all()

        context = {
            'companys': companys,
            'banner': banner,
            'services': services,
            'about': about,
            'reviews': reviews,
            'video': video,
            'process': process,
            'images': images,
            'instagram': instagram,
            'footer': footer,
            'industry': industry,
            'blog': blog,
        }
        return render(request, self.template_name, context)

class Contact(TemplateView):
    template_name = "home/contact.html"

    def get(self, request, *args, **kwargs):
        companys = Company.objects.last()
        banner = Banner.objects.all()
        services = Service.objects.all()
        about = About.objects.last()
        reviews = Review.objects.all()
        video = Video.objects.last()
        process = Process.objects.all()
        images = Images.objects.last()
        instagram = Instagram.objects.all()
        footer = Footer.objects.last()
        industry = Industry.objects.all()
        blog = Blog.objects.all()

        context = {
            'companys': companys,
            'banner': banner,
            'services': services,
            'about': about,
            'reviews': reviews,
            'video': video,
            'process': process,
            'images': images,
            'instagram': instagram,
            'footer': footer,
            'industry': industry,
            'blog': blog,
        }
        return render(request, self.template_name, context)
