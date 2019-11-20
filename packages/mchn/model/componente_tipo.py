# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('componente_tipo', pkey='id', name_long='!!Tipo Componente', name_plural='!!Tipi Componenti',caption_field='descrizione')
        self.sysFields(tbl,df=True)
        tbl.column('codice',size=':10', name_long='!!Codice')
        tbl.column('descrizione', name_long='!!Descrizione')
