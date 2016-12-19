from django.views.generic import TemplateView
from . import models
<<<<<<< HEAD
from . import forms
import locale
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
=======
import locale
>>>>>>> Premier affichage des vidéos avec titre. Modification du lien enregistrer pour qu'il puisse s'afficher sans avoir à modifier le lien manuellement
locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")


class HomePage(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(HomePage, self).get_context_data(*args, **kwargs)
        ctx['videos'] = models.Video.objects.all()
        self.selection_liens_videos(ctx['videos'])

        ctx['video_first'] = models.Video.objects.filter(first=True)

        result = models.Video.objects.filter(first=False).values()
        ctx['videos_bas'] = self.recuperer_3_dernieres_videos(result)

        return ctx

    def transforme_le_lien(self, link):
        return link.replace('watch?', '').replace('=', '/')

    def selection_liens_videos(self, videos):
        for video in videos:
            video.link = self.transforme_le_lien(video.link)
            video.save()

    def recuperer_3_dernieres_videos(self, video):
        list_result = list_result = [entry for entry in video]
        list_result = list(list_result)
        return list_result[-3:]


class ContactPage(TemplateView):

    template_name = 'contact.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ContactPage, self).get_context_data(*args, **kwargs)

        ctx['contact_form'] = forms.ContactForm()
        return ctx

    def post(self, request, *args, **kwargs):
        sujet = request.POST.get('sujet', '')
        nom = request.POST.get('nom', '')
        prenom = request.POST.get('prenom', '')
        pseudo = request.POST.get('pseudo', '')
        mail = request.POST.get('mail', '')
        temp = 'Mail : ' + mail + ' Nom : ' + nom + ' Prenom : ' + prenom + ' Pseudo : ' + pseudo + ' Message :'
        message = temp + request.POST.get('message', '')
        if sujet and message and mail:
            try:
                send_mail(sujet, message, mail, ['camillealram@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Formulaire invalide')
            return HttpResponseRedirect('/')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Tous les champs ne sont pas valide.')
