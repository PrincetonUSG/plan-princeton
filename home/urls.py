from django.urls import path
from . import views
from django.conf.urls import url
import django_cas_ng.views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('scheduler/', views.scheduler, name='scheduler'),
    url(r'^ajax/choose_conc/$', views.choose_conc, name='choose_conc'),
    url(r'^ajax/choose_deg/$', views.choose_deg, name='choose_deg'),
    url(r'^ajax/choose_season/$', views.choose_season, name='choose_season'),
    url(r'^ajax/dropped_course/$', views.dropped_course, name='dropped_course'),
    url(r'^ajax/remove_course/$', views.remove_course, name='remove_course'),
    url(r'^ajax/load/$', views.on_load, name='on_load'),
    path('sampleschedules/', views.sampleschedules, name='sampleschedules'),
    path('sampleschedules/aas/', views.aas, name='aas'),
    path('sampleschedules/ant/', views.ant, name='ant'),
    path('sampleschedules/arc/', views.arc, name='arc'),
    path('sampleschedules/art/', views.art, name='art'),
    path('sampleschedules/ast/', views.ast, name='ast'),
    path('sampleschedules/cbe/', views.cbe, name='cbe'),
    path('sampleschedules/cee/', views.cee, name='cee'),
    path('sampleschedules/chm/', views.chm, name='chm'),
    path('sampleschedules/cla/', views.cla, name='cla'),
    path('sampleschedules/com/', views.com, name='com'),
    path('sampleschedules/cos/', views.cos, name='cos'),
    path('sampleschedules/eas/', views.eas, name='eas'),
    path('sampleschedules/eco/', views.eco, name='eco'),
    path('sampleschedules/eeb/', views.eeb, name='eeb'),
    path('sampleschedules/ele/', views.ele, name='ele'),
    path('sampleschedules/eng/', views.eng, name='eng'),
    path('sampleschedules/fit/', views.fit, name='fit'),
    path('sampleschedules/geo/', views.geo, name='geo'),
    path('sampleschedules/ger/', views.ger, name='ger'),
    path('sampleschedules/his/', views.his, name='his'),
    path('sampleschedules/mae/', views.mae, name='mae'),
    path('sampleschedules/mat/', views.mat, name='mat'),
    path('sampleschedules/mol/', views.mol, name='mol'),
    path('sampleschedules/mus/', views.mus, name='mus'),
    path('sampleschedules/nes/', views.nes, name='nes'),
    path('sampleschedules/neu/', views.neu, name='neu'),
    path('sampleschedules/orf/', views.orf, name='orf'),
    path('sampleschedules/phi/', views.phi, name='phi'),
    path('sampleschedules/phy/', views.phy, name='phy'),
    path('sampleschedules/pol/', views.pol, name='pol'),
    path('sampleschedules/psy/', views.psy, name='psy'),
    path('sampleschedules/rel/', views.rel, name='rel'),
    path('sampleschedules/sla/', views.sla, name='sla'),
    path('sampleschedules/soc/', views.soc, name='soc'),
    path('sampleschedules/spa/', views.spa, name='spa'),
    path('sampleschedules/wws/', views.wws, name='wws'),
    path('logout/', views.logout, name='logout')
]