from django.urls import path

from . views import mentee, mentor
from django.contrib.auth import views as auth_views





"""Mentor and Mentee URLs"""
urlpatterns = [

    path('', mentee.home, name="home"),

    #mentee url
    path('account/', mentee.AccountList.as_view(), name="account"),
    path('register/', mentee.register, name="register"),
    path('profile/', mentee.profile, name="profile"),
    path('message-module/', mentee.MessageView.as_view(), name="module-message"),
    #path('message-module/', mentee.messege_view, name="module-message"),
    path('message/', mentee.MessageCreateView.as_view(), name="Message"),
    path('<int:pk>', mentee.SentDetailView.as_view(), name="sent"),
    path('inbox/<int:pk>', mentee.InboxDetailView.as_view(), name="detail-inbox"),
    #path('reply/<int:pk>', mentee.ReplyCreateView.as_view(), name="reply"),
    #path('login/', auth_views.LoginView.as_view(template_name='menti/login.html'), name='login'),
    path('login/', mentee.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='menti/logout.html'), name='logout'),
    path('list-message/', mentee.MessageListView.as_view(), name='list'),
    path('inbox-message/', mentee.InboxView.as_view(), name='inbox1'),
    path('delete/<int:pk>', mentee.SentMessageDelete.as_view(), name='delete'),
    path('approved/', mentee.Approved.as_view(), name='approved'),
    path(r'^send/(?P<pk>[-\w]+)/$', mentee.CreateMessageView.as_view(), name='send'),
    path('profile/<int:pk>', mentee.ProfileDetailView.as_view(), name="profile-detail"),
    path('conversation/', mentee.ConversationListView.as_view(), name='conv'),
    path('conv1/<int:pk>', mentee.ConversationDetailView.as_view(), name='conv1-reply'),
    path('conv2/<int:pk>', mentee.con, name='conv2-reply'),
    path('reply/<int:pk>', mentee.ReplyCreateView.as_view(), name='reply'),
    path('chat-delete1/<int:pk>', mentee.ConversationDeleteView.as_view(), name='chat-delete1'),
    path('search-results/', mentee.search, name="search-user"),
    path('create-indv-msg/<int:pk>', mentee.CreateIndividualMessageView.as_view(), name="create-individual"),
    path('profile2/<int:pk>', mentee.Profile2DetailView.as_view(), name="profile-detail2"),
    path('reply-indiv/<int:pk>', mentee.Reply1CreateView.as_view(), name='reply3'),
    path('conv3/<int:pk>', mentee.con1, name='conv3-reply'),
    path('pdf/', mentee.Pdf.as_view(), name="pdf"),





    #mentor urls
    path('account1/', mentor.AccountView.as_view(), name="account1"),
    path('register1/', mentor.register1, name="register1"),
    path('profile1/', mentor.profile1, name="profile1"),
    #path('login1/', mentor.login1, name="login1"),
    path('login1/', mentor.user_login, name='login1'),
    path('logout1/', auth_views.LogoutView.as_view(template_name='mentor/logout1.html'), name='logout1'),
    path('message-module1/', mentor.MessageView.as_view(), name="module-message1"),
    path('message-mentor/', mentor.MessageCreateView.as_view(), name="Message1"),
    path('inbox-message1/', mentor.InboxView.as_view(), name='inbox2'),
    path('inbox-mentor/<int:pk>', mentor.InboxDetailView.as_view(), name="detail-inbox1"),
    path('list-message1/', mentor.MessageListView.as_view(), name='list1'),
    path('delete-mentor/<int:pk>', mentor.SentMessageDelete.as_view(), name='delete1'),
    #path('comment/<int:pk>', mentor.reply_message, name='comment'),
    path(r'^comment/(?P<pk>[-\w]+)/$', mentor.reply_message, name='comment'),
    path('sent-detail/<int:pk>', mentor.SentDetailView.as_view(), name="sent1"),
    path('approved1/', mentor.Approved.as_view(), name='approved1'),
    path('profile1/<int:pk>', mentor.ProfileDetailView.as_view(), name="profile-detail1"),
    path('chat1/<int:pk>', mentor.ConversationCreateView.as_view(), name="start-chat1"),
    path('conversation1/', mentor.ConversationListView.as_view(), name='conv1'),
    #path('conversation-messo1/<int:pk>', mentor.ConverationListView.as_view(), name='conv-messo1'),
    path('reply1/<int:pk>', mentor.ReplyCreateView.as_view(), name='reply1'),
    path('conv/<int:pk>', mentor.ConversationDetailView.as_view(), name='conv-reply'),
    path('chat-delete/<int:pk>', mentor.ConversationDeleteView.as_view(), name='chat-delete'),
    path('conversation-delete/<int:pk>', mentor.Conversation2DeleteView.as_view(), name='conversation-delete'),
    path('pdf1/', mentor.Pdf.as_view(), name="pdf1"),




]



