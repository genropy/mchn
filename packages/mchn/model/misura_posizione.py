# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('misura_posizione', pkey='codice', 
                        name_long='Misura posizione', name_plural='Posizioni',
                        caption_field='descrizione',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('codice',size=':10', name_long='!!Codice')
        tbl.column('descrizione', name_long='!!Descrizione')

    @metadata(mandatory=True)
    def sysRecord_IN(self):
        return self.newrecord(codice='IN',descrizione='Ingresso')

    @metadata(mandatory=True)
    def sysRecord_OUT(self):
        return self.newrecord(codice='OUT',descrizione='Uscita')
