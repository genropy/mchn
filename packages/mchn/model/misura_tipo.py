# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('misura_tipo', pkey='id', name_long='!!Tipo Misura', name_plural='!!Tipi Misure',caption_field='descrizione')
        self.sysFields(tbl,df=True)
        tbl.column('codice',size=':10', name_long='!!Codice')
        tbl.column('descrizione', name_long='!!Descrizione')
        tbl.column('um', name_long='!!Unità di misura')
        tbl.column('tipo_dato', name_long='!!Tipo di dato', values="I:Intero,D:Decimale,B:Booleano")
        tbl.column('valore_minimo', dtype='dec', name_long='!!Valore minimo')
        tbl.column('valore_massimo', dtype='dec', name_long='!!Valore massimo')
        tbl.column('step', dtype='dec', name_long='!!Step')