#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.dbmodel import DBModel
from views.dataview import DBView

class Controller(object):

    def __init__(self):
        self.model = DBModel()
        self.view = DBView()

    def get_product_list(self):
        product_list = self.model.products.keys()
        self.view.view_data_list(product_list)

    def get_product_information(self, product):
        product_info = self.model.products.get(product, None)
        if product_info is not None:
            self.view.view_data_information(product, product_info)
        else:
            self.view.data_not_found(product)
