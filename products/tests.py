from django.test import TestCase
from django.urls import reverse


class ProductListViewTest(TestCase):
    
    def test_should_return_200(self):
        # Given a URL
        url = reverse('list_product')
        
        # When call the endpoint
        response = self.client.get(url)
        
        # breakpoint()
        
        # Expect 200 response
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.context['products'])
