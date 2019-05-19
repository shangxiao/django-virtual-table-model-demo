from django.db import models


class FooVirtualTable:
    """
    Replaces Django's BaseTable
    """
    table_name = 't'
    table_alias = 't'
    join_type = None
    parent_alias = None
    filtered_relation = None

    def as_sql(self, compiler, connection):
        # this is where BaseTable would normally just return the table's name
        return "(select 1 as id, 'bar' as foo) t", []


class FooManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        # The goal here is to replace the base physical table in qs.query.alias_map with our virtual table.
        # (alias_map is used to construct the from clause)
        # This is the line that the SQL compiler uses to initialise alias_map, as at this point it's an empty ordered dict.
        qs.query.join(FooVirtualTable())
        return qs


class Foo(models.Model):
    objects = FooManager()

    foo = models.CharField(max_length=255)

    class Meta:
        managed = False
