from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class Custompagination(PageNumberPagination):
    page_size=4
    max_page_size=20
    page_query_param='page'
    page_size_query_param='page_size'

    def get_paginated_response(self, data):
        return Response({
            'total_records':self.page.paginator.count,
            'total_pages':self.page.paginator.num_pages,
            'previous_page':self.get_previous_link(),
            'next_page':self.get_next_link(),
            'current_page':self.page.number,
            'data':data
        })