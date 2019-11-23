# encoding: utf-8
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('misura_tipo', pkey='codice', name_long='!!Tipo Misura', 
                        name_plural='!!Tipi Misure',caption_field='descrizione',
                        lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('codice',size=':10', name_long='!!Codice')
        tbl.column('descrizione', name_long='!!Descrizione')
        tbl.column('um', name_long='!!Unità di misura').relation('unita_misura.codice',
                                                                mode='foreignkey')
        tbl.column('tipo_dato', name_long='!!Tipo di dato', 
                values="L:Intero,N:Decimale,B:Booleano")
        tbl.column('valore_minimo', dtype='dec', 
                name_long='!!Valore minimo')
        tbl.column('valore_massimo', dtype='dec',
                    name_long='!!Valore massimo')
        tbl.column('step', dtype='dec', 
                    name_long='!!Step')
        tbl.column('impostabile', dtype='B', 
                    name_long='!!Impostabile')

