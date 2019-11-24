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
    py_requires="""gnrcomponents/dynamicform/dynamicform:DynamicForm"""

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record'
                        ).div(margin='10px',
                        margin_right='20px').formbuilder(cols=2, border_spacing='4px',
                                                    colswidth='auto',fld_width='100%')
        fb.field('codice',max_width='7em',readOnly=True)
        fb.field('descrizione')
        fb.field('componente_tipo_id',tag='hdbselect')
        fb.field('struttura_id')
        fb.field('data_installazione',max_width='7em')
        fb.field('identificativo')
        tc = bc.tabContainer(margin='2px',region='center')
        self.rilevazioniComponente(tc.contentPane(title='Rilevazioni'))

        tc.contentPane(title='Caratteristiche componente',
                    datapath='.record'
                    ).dynamicFieldsPane('dati_componente_tipo')
    
    def rilevazioniComponente(self,pane):
        pane.plainTableHandler(relation='@rilevazioni',
                                viewResource='ViewFromComponente',
                                grid_structpath='#FORM.record.struttura_rilevazioni',
                                view_store_limit=1000)


    def th_options(self):
        return dict(dialog_windowRatio=.8)
    
    @public_method
    def th_onLoading(self, record, newrecord, loadingParameters, recInfo):
        record['struttura_rilevazioni'] = self.db.table('mchn.componente_tipo'
                        ).getStrutturaRipartizioni(tipo_id=record['componente_tipo_id'],
                                                    colonnaComponente=False)

class FormFromStruttura(Form):
    pass

class FormFromTipo(Form):
    pass