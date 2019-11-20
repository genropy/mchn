#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):
    def th_hiddencolumns(self):
        return '$_h_count'

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('hierarchical_descrizione',width='30em')
        r.fieldcell('geocoder',width='10em')

    def th_order(self):
        return '_h_count'

    def th_query(self):
        return dict(column='hierarchical_descrizione', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('descrizione')
        fb.field('geocoder')
        tc = bc.tabContainer(region='center',margin='2px')
        th = tc.contentPane(title='Componenti').dialogTableHandler(relation='@componenti',formResource='FormFromStruttura')
        form.htree.relatedTableHandler(th,dropOnRoot=False,inherited=True)

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px',hierarchical=True)
