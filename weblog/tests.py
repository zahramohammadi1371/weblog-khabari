from email.policy import HTTP
from urllib import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from weblog.views import PostList
from .models import Post,Category,Comment
from django.test import SimpleTestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status


class ApiUrlTests(SimpleTestCase):

    def test_get_postlist_is_resolve(self):
        url=reverse('post list')
        print(resolve(url).func)
        self.assertEqual(resolve(url).func.view_class,PostList)
        # print(url)


class PostListApiViewTests(APITestCase):
    PostList_url=reverse('post list')

    def setUp(self) :
        self.user=User.objects.create_user(
            username='admin',
            password="1234567")
            
        self.token=Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token'+self.token.key)


    # def test_get_postlist(self):
    #     response=self.client.get(self.PostList_url)
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)

class weblogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'zahra mohammadi',
            password = "1234"
        )
        
        self.post = Post.objects.create(
            title = 'post title',
            body = 'post body',
            author=self.user,
            status='published',
            is_enabled='True',
            Featured='True', 
        )
        
    def test_string_model(self):
        post = Post(title='hello from test')
        self.assertEqual(str(post),post.title)

    def test_post_model(self):
        self.assertEqual(f"{self.post.title}", "post title")
        self.assertEqual(f"{self.post.body}", "post body")
        self.assertEqual(f"{self.post.author}", "zahra mohammadi")



     



      
       
        