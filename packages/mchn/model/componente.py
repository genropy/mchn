#!/usr/bin/env python
# encoding: utf-8




class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('componente', pkey='id', name_long='!![it]Componente', 
                    name_plural='!![it]Componenti',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('codice',size=':6',name_long='Codice',unique=True)
        tbl.column('identificativo', size=':30', name_long='Identificativo')
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('componente_tipo_id',size='22',name_long='Tipo').relation('componente_tipo.id',
                    relation_name='cespiti',mode='foreignkey')
        tbl.column('dati_componente_tipo',dtype='X',name_long='!![it]Dati componente',subfields='componente_tipo_id')
        tbl.column('data_installazione','D',name_long='!![it]Data installazione')

        tbl.column('componente_ubicazione_id',size='22', group='_', name_long='Ubicazione'
                    ).relation('componente_ubicazione.id', 
                                relation_name='componenti',
                                mode='foreignkey', 
                                onDelete='raise')

    
