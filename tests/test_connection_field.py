"""`AdvancedDjangoFilterConnectionField` class tests."""

from django.test import TestCase
from django_filters import FilterSet
from graphene_django_filter import AdvancedDjangoFilterConnectionField

from .filter_sets import TaskFilter
from .object_types import TaskFilterSetClassType


class AdvancedDjangoFilterConnectionFieldTest(TestCase):
    """AdvancedDjangoFilterConnectionField tests."""

    def test_init(self) -> None:
        """Test `__init__` method."""
        AdvancedDjangoFilterConnectionField(TaskFilterSetClassType)
        AdvancedDjangoFilterConnectionField(TaskFilterSetClassType, filterset_class=TaskFilter)
        self.assertRaisesMessage(
            lambda: AdvancedDjangoFilterConnectionField(
                TaskFilterSetClassType,
                filterset_class=FilterSet,
            ), 'Use the `AdvancedFilterSet` class with the `AdvancedDjangoFilterConnectionField`',
        )

    def test_filtering_args(self) -> None:
        """Test the `filtering_args` property."""
        tasks = AdvancedDjangoFilterConnectionField(
            TaskFilterSetClassType,
            description='Advanced filter field',
        )
        filtering_args = tasks.filtering_args
        self.assertEqual(('filter',), tuple(filtering_args.keys()))
        self.assertEqual(
            'TaskFilterSetClassFilterInputType',
            filtering_args['filter'].type.__name__,
        )
