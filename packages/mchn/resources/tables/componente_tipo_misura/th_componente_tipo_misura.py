#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('componente_tipo_id')
        r.fieldcell('codice')
        r.fieldcell('descrizione')
        r.fieldcell('misura_tipo_id')

    def th_order(self):
        return 'componente_tipo_id'

    def th_query(self):
        return dict(column='componente_tipo_id', op='contains', val='')


class ViewFromTipo(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('misura_tipo_id',edit=True,width='15em')
        r.fieldcell('descrizione',edit=True,width='20em')

    def th_order(self):
        return 'misura_tipo_id'


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('componente_tipo_id')
        fb.field('codice')
        fb.field('descrizione')
        fb.field('misura_tipo_id')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
