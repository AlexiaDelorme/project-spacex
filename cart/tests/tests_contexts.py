from django.test import TestCase
from trips.models import TripCategory, Trip, DepartureSite


class TestCartContext(TestCase):

    def setUp(self):

        # create dummy instance of the trip object
        self.cat_1 = TripCategory.objects.create(
            title='Trip to the Moon',
            destination='Moon',
            destination_code='MNX',
            duration=1,
            distance=400000,
            price=10000,
            description='bla bla bla'
        )
        self.dep_site_1 = DepartureSite.objects.create(
            site_name='Kourou',
            country='French Guiana',
            site_code='CSG'
        )
        self.trip_1 = Trip.objects.create(
            category=self.cat_1, departure_site=self.dep_site_1,
            departure_date='2020-07-15', departure_time='06:00:00',
            return_time='12:00:00', slot='15'
        )

    def test_get_cart_contents(self):

        # add a trip to the cart
        url = "/cart/add/" + str(self.trip_1.id) + "/"
        self.client.post(url, data={'passenger': '1'})

        # get cart view
        response = self.client.get('/cart/')
        expected_cart_items = [
            {
                'id': str(self.trip_1.id),
                'trip': self.trip_1,
                'passenger': 1,
                'passenger_range': range(0, 1),
                'sub_total': self.trip_1.category.price
            }
        ]

        self.assertEqual(response.context['cart_items'], expected_cart_items)
        self.assertEqual(response.context['total'], 10000)
        self.assertEqual(response.context['trip_count'], 1)
        self.assertEqual(response.context['per_id_count'], 1)
