#!/usr/bin/env python
# encoding: utf-8




class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('componente', pkey='id', name_long='!![it]Componente', 
                    name_plural='!![it]Componenti',caption_field='descrizione')
        self.sysFields(tbl,counter='struttura_id')
        tbl.column('codice',size=':6',name_long='Codice',unique=True)
        tbl.column('identificativo', size=':30', name_long='Identificativo')
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('componente_tipo_id',size='22',name_long='Tipo').relation('componente_tipo.id',
                    relation_name='componenti',mode='foreignkey')
        tbl.column('dati_componente_tipo',dtype='X',name_long='!![it]Dati componente',subfields='componente_tipo_id')
        tbl.column('data_installazione','D',name_long='!![it]Data installazione')

        tbl.column('struttura_id',size='22', group='_', name_long='Struttura'
                    ).relation('componente_struttura.id', relation_name='componenti',
                                mode='foreignkey',onDelete='raise')
    
    def counter_codice(self,record=None):
        #F14/000001
        return dict(format='$NNNNNN',showOnLoad=True,code='*')



    
