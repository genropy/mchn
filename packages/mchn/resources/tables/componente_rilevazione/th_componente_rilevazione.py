#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):
    def th_hiddencolumns(self):
        return '#BAGCOLS($rilevazioni)'

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ts',name_long='TS',width='10em')
        r.fieldcell('componente_id')
        r.fieldcell('rilevazioni')

    def th_order(self):
        return 'ts:d'

    def th_query(self):
        return dict(column='componente_id', op='contains', val='')


class ViewFromEmulatore(View):
    pass
    

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('componente_id')
        fb.field('ts')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
