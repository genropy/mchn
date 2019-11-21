#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):
    

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count')
        r.fieldcell('codice')
        r.fieldcell('identificativo')
        r.fieldcell('descrizione')
        r.fieldcell('componente_tipo_id')
        r.fieldcell('dati_componente_tipo')
        r.fieldcell('data_installazione')
        r.fieldcell('struttura_id')

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='_row_count', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('componente_tipo_id')
        fb.field('descrizione',colspan=2)
        fb.field('identificativo')
        fb.field('data_installazione')
        fb.field('struttura_id')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')


class FormFromStruttura(BaseComponent):
    py_requires="""gnrcomponents/dynamicform/dynamicform:DynamicForm"""

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('componente_tipo_id')
        fb.field('descrizione',colspan=2)
        fb.field('identificativo')
        fb.field('data_installazione')
        fb.appendDynamicFields('dati_componente_tipo')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')


class FormFromTipo(BaseComponent):
    py_requires="""gnrcomponents/dynamicform/dynamicform:DynamicForm"""
                   #gnrcomponents/attachmanager/attachmanager:AttachManager"""

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('struttura_id')
        fb.field('descrizione',colspan=2)
        fb.field('identificativo')
        fb.field('data_installazione')
        fb.appendDynamicFields('dati_componente_tipo')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')