#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    """ """
    def config_db(self, pkg):
        tbl =  pkg.table('unita_misura', pkey='codice',name_plural = u'!![it]Unità misura',
                         name_long=u'!![it]Unità misura', 
                         caption_field='codice',lookup=True)
        self.sysFields(tbl, id=False)
        tbl.column('codice',size=':6',name_long='!![it]Codice')
        tbl.column('descrizione',size=':32',name_long='!![it]Descrizione')
        tbl.column('tipo',size=':12',name_long='!![it]Tipo',group='_').relation('unita_misura_tipo.codice',mode='foreignkey')
        tbl.column('dimensioni',name_long='!![it]Dimensioni')
        tbl.formulaColumn('descrizione_completa',"$codice||' - '||$descrizione",group='_') 

