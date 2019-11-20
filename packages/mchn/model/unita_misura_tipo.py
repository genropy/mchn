#!/usr/bin/env python
# encoding: utf-8
# VISTOAL: 291008
from builtins import object
from gnr.core.gnrdecorator import metadata

class Table(object):
    """ """
    def config_db(self, pkg):
        """erpy_base.tipo_unita_misura"""
        tbl =  pkg.table('unita_misura_tipo', pkey='codice',name_plural = u'!![it]Tipi unità misura',
                         name_long=u'!![it]Tipo unità misura',lookup=True,caption_field='descrizione')
        self.sysFields(tbl, id=False)
        tbl.column('codice',size=':12',name_long='!![it]Codice')
        tbl.column('relazione',name_long='!![it]Relazione')
        tbl.column('descrizione',name_long='!![it]Descizione')
        tbl.formulaColumn('descrizione_completa',"$codice||' - '||$descrizione",group='_') 
    
    @metadata(mandatory=True)
    def sysRecord_N(self):
        return self.newrecord(codice='N',descrizione='Numero')

    @metadata(mandatory=True)
    def sysRecord_P(self):
        return self.newrecord(codice='P',descrizione='Peso')

    @metadata(mandatory=True)
    def sysRecord_L(self):
        return self.newrecord(codice='L',descrizione='Lunghezza')

    @metadata(mandatory=True)
    def sysRecord_S(self):
        return self.newrecord(codice='S',descrizione='Superficie')

    @metadata(mandatory=True)
    def sysRecord_V(self):
        return self.newrecord(codice='V',descrizione='Volume')




