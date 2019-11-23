#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):
    def th_hiddencolumns(self):
        return '$_h_count'

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('hierarchical_codice',width='10em')
        r.fieldcell('hierarchical_descrizione',width='30em')

    def th_order(self):
        return '_h_count'

    def th_query(self):
        return dict(column='hierarchical_descrizione', op='contains', val='')



class Form(BaseComponent):
    py_requires = 'gnrcomponents/dynamicform/dynamicform:DynamicForm'

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('descrizione')
        tc = bc.tabContainer(region='center',margin='2px')
        th = tc.contentPane(title='Componenti').dialogTableHandler(relation='@componenti',formResource='FormFromTipo')
        form.htree.relatedTableHandler(th,dropOnRoot=False,inherited=True)
        tc.contentPane(title='Campi').fieldsGrid(margin='2px',rounded=6,border='1px solid silver')
        tc.contentPane(title='Valori misurabili').inlineTableHandler(relation='@valori_misurabili',viewResource='ViewFromTipo',
                                                                    picker='misura_tipo',
                                                                    grid_selfDragRows=True,
                                                                    picker_uniqueRow=False)

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px',hierarchical=True)
