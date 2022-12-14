from django.urls import path

from . import views

app_name = 'qa_rpg'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('template/', views.TemplateChooseView.as_view(), name='template'),
    path('template/choose', views.choose, name='choose'),
    path('template/summon/', views.SummonView.as_view(), name='summon'),
    path('template/summon/create', views.create, name='create'),
    path('dungeon/', views.DungeonView.as_view(), name='dungeon'),
    path('dungeon/report_previous', views.report_previous, name='report_previous'),
    path('dungeon/action', views.action, name='action'),
    path('dungeon/battle', views.BattleView.as_view(), name='battle'),
    path('dungeon/battle/item', views.item, name='item'),
    path('dungeon/battle/check/<int:question_id>', views.check, name='check'),
    path('dungeon/battle/run_away/<int:question_id>', views.run_away, name='run_away'),
    path('dungeon/treasure', views.TreasureView.as_view(), name='treasure'),
    path('dungeon/treasure/treasure_action', views.treasure_action, name='treasure_action'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/buy/', views.buy, name='buy'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/claim/<int:question_id>', views.claim_coin, name='claim'),
    path('profile/select_template', views.select, name='select'),
    path('profile/upgrade/', views.UpgradeView.as_view(), name='upgrade'),
    path('profile/upgrade/upgrade_action', views.upgrade, name='upgrade_action'),
    path('profile/upgrade/awake', views.awake, name='awake'),
    path('select/select_items', views.select_items, name='select_items'),
    path('select/', views.SelectItemsView.as_view(), name="select_dg"),
    path('', views.HomeView.as_view(), name='home')
]
