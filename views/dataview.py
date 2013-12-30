#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DBView(object):

    def view_data_list(self, product_list):
        print 'PRODUCT LIST:'
        for product in product_list:
            print(product)
        print('')

    def view_data_info(self, product, product_info):
        print 'PRODUCT INFORMATION:'
        print 'Name: {0}, Price: {1}, Quantity: {2}\n'.format(
               product.title(), product_info.get('price', 0),
               product_info.get('quantity', 0))

    def data_not_found(self, product):
        print 'That product "%s" does not exist in the records' % product
