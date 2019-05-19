from django.test import TestCase

from .models import Foo


class FooTestCase(TestCase):
    def test_foo(self):
        """
        We should receive 'bar' as the value of 'foo' from the first and only row of Foo
        """
        qs = Foo.objects.all()
        print(qs.query)

        self.assertEqual(qs.first().foo, 'bar')
